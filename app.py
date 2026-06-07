import streamlit as st
import pdfplumber
import re
import unicodedata
from datetime import datetime
import plotly.graph_objects as go

from data.keywords_db import KEYWORD_CATALOG, CATEGORY_LABELS
from data.jobs_db import JOBS, get_categories_with_jobs, get_job_by_id


#Pagina
st.set_page_config(
    page_title="ATS CV Checker",
    page_icon=":material/contract:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS personalizado
st.markdown("""
<style>
    .hero-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 45%, #ec4899 100%);
        padding: 32px 28px;
        border-radius: 18px;
        color: white;
        margin: 4px 0 28px 0;
        box-shadow: 0 12px 32px rgba(118, 75, 162, 0.28);
    }
    .hero-card h1 {
        color: white !important;
        font-size: 38px !important;
        font-weight: 800 !important;
        margin: 0 0 8px 0 !important;
        padding: 0 !important;
        letter-spacing: -0.5px;
    }
    .hero-card p {
        color: rgba(255,255,255,0.95) !important;
        font-size: 17px !important;
        margin: 0 !important;
        font-weight: 400;
    }

    .keyword-chip {
        display: inline-block;
        padding: 6px 14px;
        margin: 4px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        color: white;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }
    .chip-found    { background: linear-gradient(135deg, #10b981, #059669); }
    .chip-missing  { background: linear-gradient(135deg, #fb7185, #be123c); }
    .chip-critical {
        background: linear-gradient(135deg, #f59e0b, #d97706);
        font-weight: 700;
        box-shadow: 0 2px 8px rgba(245, 158, 11, 0.45);
    }

    .level-badge {
        display: inline-block;
        padding: 5px 14px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        color: white;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }
    .level-junior    { background: linear-gradient(135deg, #3b82f6, #1d4ed8); }
    .level-mid       { background: linear-gradient(135deg, #14b8a6, #0d9488); }
    .level-senior    { background: linear-gradient(135deg, #8b5cf6, #6d28d9); }
    .level-executive { background: linear-gradient(135deg, #ec4899, #be185d); }

    .job-card {
        padding: 18px;
        border-radius: 12px;
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.10) 0%, rgba(236, 72, 153, 0.06) 100%);
        border-left: 5px solid #8b5cf6;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.08);
    }

    h2, h3 {
        color: #a78bfa !important;
    }

    .stButton button, .stDownloadButton button {
        background: linear-gradient(135deg, #7c3aed, #ec4899) !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        padding: 8px 20px !important;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.35) !important;
    }
    .stButton button:hover, .stDownloadButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(124, 58, 237, 0.45) !important;
    }

    [data-testid="stMetricValue"] {
        font-weight: 800 !important;
        color: #a78bfa !important;
        font-size: 32px !important;
    }

    .stAlert {
        border-radius: 12px !important;
        border-left-width: 4px !important;
    }

    [data-testid="stFileUploader"] {
        background: rgba(139, 92, 246, 0.06);
        border-radius: 12px;
        padding: 8px;
        border: 2px dashed #a78bfa;
    }

    [data-testid="stExpander"] {
        border-radius: 12px !important;
        border: 1px solid rgba(167, 139, 250, 0.25) !important;
    }
</style>
""", unsafe_allow_html=True)


#Extracción
def quitar_acentos(texto: str) -> str:
    nfkd = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


def normalizar(texto: str) -> str:
    """Limpia texto para matching. Maneja CIDs de PDFs LaTeX."""
    cid_map = {
        '(cid:27)': 'ff', '(cid:28)': 'fi', '(cid:29)': 'fl',
        '(cid:30)': 'ffi', '(cid:31)': 'ffl',
    }
    for cid, repl in cid_map.items():
        texto = texto.replace(cid, repl)
    texto = quitar_acentos(texto.lower())
    # Conservar + y # para C++, C#, etc.
    texto = re.sub(r'[^a-z0-9+#\s\-/]', ' ', texto)
    return re.sub(r'\s+', ' ', texto).strip()


def extraer_texto_pdf(archivo) -> str:
    """Extrae texto de un PDF subido."""
    try:
        with pdfplumber.open(archivo) as pdf:
            return ' '.join((p.extract_text() or '') for p in pdf.pages)
    except Exception as e:
        st.error(f"Error al leer el PDF: {e}")
        return ""


def detectar_idioma(texto: str) -> str:
    """Detección simple de idioma."""
    texto_low = texto.lower()
    es = sum(1 for w in [' el ', ' la ', ' de ', ' con ', ' para ', ' en ', ' los ', ' las ', ' una '] if w in texto_low)
    en = sum(1 for w in [' the ', ' of ', ' and ', ' with ', ' for ', ' in ', ' to ', ' a ', ' you '] if w in texto_low)
    return 'es' if es > en else 'en'


def extraer_keywords_de_jd(jd_texto: str, pool: dict) -> dict:
    """Encuentra qué keywords del pool aparecen en la descripción."""
    jd_norm = normalizar(jd_texto)
    return {kw: peso for kw, peso in pool.items() if normalizar(kw) in jd_norm}


def calificar_cv(cv_texto: str, keywords: dict) -> dict:
    """Califica el CV contra keywords ponderadas."""
    cv_norm = normalizar(cv_texto)
    encontradas, faltantes = {}, []
    obt, total = 0, sum(keywords.values())

    for kw, peso in keywords.items():
        kw_norm = normalizar(kw)
        if ' ' in kw_norm:
            n = cv_norm.count(kw_norm)
        else:
            n = len(re.findall(r'\b' + re.escape(kw_norm) + r'\b', cv_norm))
        if n > 0:
            obt += peso
            encontradas[kw] = (peso, n)
        else:
            faltantes.append((kw, peso))

    return {
        'score': round(obt / total * 100, 1) if total > 0 else 0,
        'obtenido': obt,
        'total': total,
        'encontradas': encontradas,
        'faltantes': sorted(faltantes, key=lambda x: -x[1]),
    }


def generar_sugerencias(resultado: dict, cv_texto: str, jd_texto: str) -> list:
    """Sugerencias accionables."""
    sugs = []
    score = resultado['score']
    faltantes_criticas = [kw for kw, peso in resultado['faltantes'] if peso >= 4]
    faltantes_importantes = [kw for kw, peso in resultado['faltantes'] if peso == 3]

    if score < 50:
        sugs.append((":material/crisis_alert:", "Score crítico",
                     "Tu CV cubre menos del 50% de las keywords clave de este puesto. "
                     "Considera reescribir secciones para incluir terminología relevante "
                     "o aplicar a un puesto más alineado con tu experiencia actual."))
    elif score < 70:
        sugs.append((":material/warning:", "Score mejorable",
                     "Estás cerca, pero faltan keywords importantes para pasar filtros estrictos. "
                     "Pequeñas adiciones podrían marcar la diferencia."))
    elif score < 85:
        sugs.append((":material/check_circle:", "Buen ajuste",
                     "Tu CV tiene buen match. Pequeños ajustes pueden llevarte al rango óptimo "
                     "(85%+) donde típicamente los CVs pasan filtros ATS."))
    else:
        sugs.append((":material/target:", "Excelente ajuste",
                     "Tu CV está muy bien alineado a este puesto. Considera personalizar el "
                     "resumen profesional para resaltar la conexión específica."))

    if faltantes_criticas:
        kws_str = ", ".join(f"**{k}**" for k in faltantes_criticas[:5])
        sugs.append((":material/pin:", "Keywords críticas faltantes (peso 4-5)",
                     f"Considera agregar (con contexto real, NO relleno): {kws_str}. "
                     "Estas son las más importantes para este puesto."))

    if faltantes_importantes and len(faltantes_importantes) >= 3:
        kws_str = ", ".join(f"**{k}**" for k in faltantes_importantes[:5])
        sugs.append((":material/attach_file:", "Keywords importantes faltantes (peso 3)",
                     f"Si tienes experiencia con: {kws_str}, menciónalas explícitamente."))

    # Mismatch de idioma
    cv_lang = detectar_idioma(cv_texto)
    jd_lang = detectar_idioma(jd_texto)
    if cv_lang != jd_lang:
        idioma_cv = 'español' if cv_lang == 'es' else 'inglés'
        idioma_jd = 'español' if jd_lang == 'es' else 'inglés'
        sugs.append((":material/language:", "Mismatch de idioma",
                     f"Tu CV parece estar en **{idioma_cv}** pero la oferta está en "
                     f"**{idioma_jd}**. Considera traducir tu CV o aplicar a una versión "
                     "en tu idioma. Esto puede estar bajando significativamente tu score."))

    # Longitud
    palabras = len(cv_texto.split())
    if palabras < 200:
        sugs.append((":material/description:", "CV muy corto",
                     f"Tu CV tiene solo ~{palabras} palabras. Un CV típico tiene 400-700. "
                     "Considera detallar más tu experiencia con bullets cuantificados."))
    elif palabras > 1200:
        sugs.append((":material/scissors:", "CV muy largo",
                     f"Tu CV tiene ~{palabras} palabras. Considera condensarlo a 1-2 páginas "
                     "(400-700 palabras) priorizando lo más relevante para este puesto."))

    # CIDs detectados (indicador de PDF LaTeX mal configurado)
    if '(cid:' in cv_texto:
        sugs.append((":material/settings:", "Problema técnico en el PDF",
                     "Detectamos ligaduras tipográficas mal mapeadas (`(cid:NN)`) en tu PDF. "
                     "Si lo generaste con LaTeX, agrega al preámbulo: `\\usepackage{cmap}` "
                     "y `\\input{glyphtounicode}\\pdfgentounicode=1` con `\\usepackage{lmodern}`. "
                     "Esto afecta la extracción del texto por algunos ATS."))

    return sugs


#Visualizaciones de resultados
def gauge_chart(score: float) -> go.Figure:
    if score < 50:
        color = "#f43f5e"
    elif score < 70:
        color = "#f59e0b"
    elif score < 85:
        color = "#3b82f6"
    else:
        color = "#10b981"

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Score ATS", 'font': {'size': 18}},
        number={'suffix': "%", 'font': {'size': 44}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1},
            'bar': {'color': color, 'thickness': 0.7},
            'steps': [
                {'range': [0, 50], 'color': '#fee2e2'},
                {'range': [50, 70], 'color': '#fef3c7'},
                {'range': [70, 85], 'color': '#dbeafe'},
                {'range': [85, 100], 'color': '#d1fae5'},
            ],
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 75,
            },
        },
    ))
    fig.update_layout(height=280, margin=dict(l=20, r=20, t=40, b=20))
    return fig


def keywords_bar_chart(resultado: dict) -> go.Figure:
    encontradas = [(kw, peso) for kw, (peso, _) in resultado['encontradas'].items()]
    faltantes = [(kw, peso) for kw, peso in resultado['faltantes']]
    all_kw = sorted(encontradas + faltantes, key=lambda x: -x[1])[:15]

    kws = [x[0] for x in all_kw]
    pesos = [x[1] for x in all_kw]
    encontradas_set = {kw for kw, _ in encontradas}
    colors = ['#28a745' if kw in encontradas_set else '#dc3545' for kw in kws]

    fig = go.Figure(go.Bar(
        y=kws[::-1],
        x=pesos[::-1],
        orientation='h',
        marker_color=colors[::-1],
        text=[f"✓" if kw in encontradas_set else f"✗" for kw, p in zip(kws[::-1], pesos[::-1])],
        textposition='outside',
    ))
    fig.update_layout(
        height=450,
        title="Keywords del puesto: las más importantes (peso)",
        xaxis_title="Peso (importancia)",
        yaxis_title=None,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20),
    )
    return fig


def render_chips(items: list, tipo: str = 'found'):
    if not items:
        st.caption("_(ninguna)_")
        return
    chips = ' '.join(f'<span class="keyword-chip chip-{tipo}">{item}</span>' for item in items)
    st.markdown(chips, unsafe_allow_html=True)


def render_level_badge(level: str) -> str:
    labels = {'junior': 'JUNIOR', 'mid': 'MID-LEVEL', 'senior': 'SENIOR', 'executive': 'EXECUTIVE'}
    return f'<span class="level-badge level-{level}">{labels.get(level, level.upper())}</span>'


# Header
def render_header():
    st.markdown("""
    <div class="hero-card">
        <h1>Filtro ATS</h1>
        <p>Prueba tu CV contra ofertas de trabajo realistas y descubre un aproximado de cómo te calificaría un filtro ATS antes de aplicar.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("¿Cómo funciona y para qué sirve?"):
        st.markdown("""
        **Instrucciones:**
        1. Elige una **oferta ficticia** (inspirada en patrones reales de Databricks, Amazon,
           Mercado Libre, Stripe, etc.) o **pega una descripción real** que tú quieras usar.
        2. **Sube tu CV en PDF**.
        3. La app extrae el texto, identifica qué keywords técnicas aparecen en la oferta,
           y las busca en tu CV.
        4. Recibes un **score ponderado**, **visualización** de keywords encontradas/faltantes
           y **sugerencias específicas** para mejorar.         
                    
        **IMPORTANTE:**
                    
        **Este software no:**
        - No es un ATS real. Los ATS comerciales (Workday, Greenhouse, Lever) usan algoritmos
          más sofisticados con NLP y pesos propietarios.
        - Un score alto aquí no garantiza pasar todos los ATS, pero indica buen alineamiento.

        **Este software es:**
        - Una aproximación útil para **identificar gaps obvios** entre tu CV y un puesto.
        - Una forma de **practicar el ejercicio** de adaptar tu CV a cada oferta.
        - Un detector de **problemas técnicos del PDF** (ligaduras, letter-spacing, OCR).
        """)


#Sidebar
def render_sidebar():
    with st.sidebar:
        st.markdown("### Configuración")

        modo = st.radio(
            "Origen de la descripción de trabajo:",
            ["Elegir oferta del catálogo", "Pegar mi propia descripción"],
            key="modo_fuente",
        )

        st.markdown("---")
        st.caption(f"Catálogo: **{len(JOBS)} puestos ficticios**")

        return modo


#Catálogo de ofertas
def flujo_catalogo():
    st.markdown("### Catálogo de ofertas")
    st.caption("Ofertas ficticias inspiradas en patrones reales de la industria.")

    categorias = get_categories_with_jobs()

    # Selector de categoría
    cat = st.selectbox(
        "Categoría:",
        list(categorias.keys()),
        format_func=lambda k: f"{CATEGORY_LABELS.get(k, k)} ({len(categorias[k])} oferta(s))",
    )

    # Lista visual de ofertas en esa categoría
    st.markdown("**Ofertas disponibles:**")
    opciones = {}
    for job in categorias[cat]:
        idioma_flag = "🇲🇽" if job['language'] == 'es' else "🇺🇸"
        label = f"{job['title']} — {job['company']} {idioma_flag}"
        opciones[label] = job

    seleccion = st.radio(
        "Selecciona una oferta:",
        list(opciones.keys()),
        label_visibility="collapsed",
    )
    job = opciones[seleccion]

    # Tarjeta del job
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### {job['title']}")
        st.markdown(f"**{job['company']}** — {job['location']}")
    with col2:
        st.markdown(render_level_badge(job['level']), unsafe_allow_html=True)
        st.caption(f"Idioma: {'Español' if job['language'] == 'es' else 'Inglés'}")

    with st.expander(":material/description: Ver descripción completa del puesto", expanded=False):
        st.markdown(job['description'])

    pool = KEYWORD_CATALOG.get(job['category'], {})
    return job['description'], pool, job


def flujo_pegar_descripcion():
    st.markdown("### Pega la descripción del puesto")
    jd = st.text_area(
        "Copia y pega aquí la descripción completa del puesto al que quieres aplicar:",
        height=280,
        placeholder="Ejemplo: We're looking for a Data Scientist with 3+ years of experience in Python, machine learning, and A/B testing...",
    )

    cat = st.selectbox(
        "¿A qué categoría pertenece este puesto?",
        list(CATEGORY_LABELS.keys()),
        format_func=lambda k: CATEGORY_LABELS[k],
        help="Esto determina qué pool de keywords usar para evaluar.",
    )

    pool = KEYWORD_CATALOG.get(cat, {})
    return jd, pool, None


#Análisis final
def flujo_cv_y_analisis(jd_texto: str, pool: dict, job_info: dict | None):
    if not jd_texto or len(jd_texto) < 100:
        st.info("Selecciona o pega una descripción de trabajo (al menos 100 caracteres) para continuar.")
        return

    keywords_jd = extraer_keywords_de_jd(jd_texto, pool)
    if not keywords_jd:
        st.warning("No se detectaron keywords técnicas conocidas en esta descripción. "
                   "Prueba con una categoría diferente o una oferta más técnica.")
        return

    st.success(f"Detectamos **{len(keywords_jd)} keywords técnicas** en esta descripción. "
               f"Suma total ponderada: **{sum(keywords_jd.values())} puntos posibles**.")

    st.markdown("---")
    st.markdown("### Sube tu CV")
    archivo = st.file_uploader(
        "Arrastra tu CV en PDF (LaTeX, Word, etc.)",
        type=['pdf'],
    )

    if archivo is None:
        return

    with st.spinner("Analizando tu CV..."):
        cv_texto = extraer_texto_pdf(archivo)

    if not cv_texto:
        return

    resultado = calificar_cv(cv_texto, keywords_jd)
    sugerencias = generar_sugerencias(resultado, cv_texto, jd_texto)

    #Despliegue de resultados
    st.markdown("---")
    st.markdown("## Resultados")

    col_gauge, col_metrics = st.columns([1, 1])
    with col_gauge:
        st.plotly_chart(gauge_chart(resultado['score']), use_container_width=True)
    with col_metrics:
        st.markdown(f"### {resultado['obtenido']}/{resultado['total']} puntos")
        st.metric("Keywords encontradas", f"{len(resultado['encontradas'])} de {len(keywords_jd)}")
        if resultado['score'] >= 85:
            st.success("Excelente match para este puesto")
        elif resultado['score'] >= 70:
            st.info("Buen match para este puesto")
        elif resultado['score'] >= 50:
            st.warning("Match mejorable")
        else:
            st.error("Match crítico — considera reescribir el CV")

    # Gráficas
    st.markdown("### Comparativa visual de keywords")
    st.plotly_chart(keywords_bar_chart(resultado), use_container_width=True)

    # Chips (keywords encontradas/faltantes)
    col_f, col_m = st.columns(2)
    with col_f:
        st.markdown(f"#### Encontradas ({len(resultado['encontradas'])})")
        render_chips(list(resultado['encontradas'].keys()), 'found')

    with col_m:
        st.markdown(f"#### Faltantes ({len(resultado['faltantes'])})")
        criticas = [kw for kw, peso in resultado['faltantes'] if peso >= 4]
        importantes = [kw for kw, peso in resultado['faltantes'] if peso == 3]
        menores = [kw for kw, peso in resultado['faltantes'] if peso < 3]
        if criticas:
            st.caption("**Críticas (peso ≥ 4):**")
            render_chips(criticas, 'critical')
        if importantes:
            st.caption("**Importantes (peso 3):**")
            render_chips(importantes, 'missing')
        if menores:
            st.caption("**Menores (peso ≤ 2):**")
            render_chips(menores, 'missing')

    # ===== SUGERENCIAS =====
    st.markdown("### Sugerencias específicas")
    for icono, titulo, texto in sugerencias:
        with st.container():
            st.markdown(f"**{icono} {titulo}**")
            st.markdown(texto)
            st.markdown("")

    # Reporte
    st.markdown("---")
    reporte = generar_reporte_md(resultado, sugerencias, keywords_jd, job_info)
    nombre_archivo = f"reporte_ats_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
    st.download_button(
        "Descargar reporte completo en Markdown",
        reporte,
        file_name=nombre_archivo,
        mime="text/markdown",
        use_container_width=True,
    )


def generar_reporte_md(resultado: dict, sugerencias: list, keywords_jd: dict,
                       job_info: dict | None) -> str:
    lines = ["# Reporte de evaluación ATS",
             f"_Generado el {datetime.now().strftime('%Y-%m-%d %H:%M')}_", ""]
    if job_info:
        lines += [f"## Puesto evaluado", f"**{job_info['title']}** — {job_info['company']}",
                  f"_{job_info['location']}_", ""]
    lines += ["## Resumen",
              f"- **Score:** {resultado['score']}%",
              f"- **Puntos:** {resultado['obtenido']}/{resultado['total']}",
              f"- **Keywords encontradas:** {len(resultado['encontradas'])}/{len(keywords_jd)}",
              "",
              "## Keywords encontradas en tu CV"]
    for kw, (peso, n) in sorted(resultado['encontradas'].items(), key=lambda x: -x[1][0]):
        lines.append(f"- **{kw}** (peso {peso}, aparece {n}x)")
    lines += ["", "## Keywords faltantes"]
    for kw, peso in resultado['faltantes']:
        marker = ":material/alert:" if peso >= 4 else (":material/warning:" if peso == 3 else "·")
        lines.append(f"- {marker} **{kw}** (peso {peso})")
    lines += ["", "## Sugerencias"]
    for icono, titulo, texto in sugerencias:
        lines.append(f"### {icono} {titulo}")
        lines.append(texto)
        lines.append("")
    return "\n".join(lines)


def main():
    render_header()
    modo = render_sidebar()

    if "catálogo" in modo or "catalogo" in modo.lower():
        jd, pool, job = flujo_catalogo()
    else:
        jd, pool, job = flujo_pegar_descripcion()

    if jd:
        flujo_cv_y_analisis(jd, pool, job)


if __name__ == "__main__":
    main()