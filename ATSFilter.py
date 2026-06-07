import pdfplumber
import re
import unicodedata
from collections import Counter

def quitar_acentos(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))

def extraer_texto(ruta_pdf):
    texto = ""
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto += (pagina.extract_text() or "") + " "
    return texto

def normalizar(texto):
    # Limpiar ligaduras tipográficas que algunos PDFs producen como (cid:NN)
    cid_map = {
        '(cid:27)': 'ff', '(cid:28)': 'fi', '(cid:29)': 'fl',
        '(cid:30)': 'ffi', '(cid:31)': 'ffl',
    }
    for cid, repl in cid_map.items():
        texto = texto.replace(cid, repl)
    texto = quitar_acentos(texto.lower())
    texto = re.sub(r'[^a-z0-9\s]', ' ', texto)
    return re.sub(r'\s+', ' ', texto).strip()

def calificar_cv(ruta_pdf, keywords_ponderadas):
    texto = normalizar(extraer_texto(ruta_pdf))
    palabras = texto.split()
    conteo = Counter(palabras)

    puntos_obtenidos = 0
    puntos_maximos = sum(keywords_ponderadas.values())
    encontradas = {}
    faltantes = []

    for kw, peso in keywords_ponderadas.items():
        kw_norm = normalizar(kw)
        if " " in kw_norm:
            apariciones = texto.count(kw_norm)
        else:
            apariciones = conteo.get(kw_norm, 0)

        if apariciones > 0:
            puntos_obtenidos += peso
            encontradas[kw] = apariciones
        else:
            faltantes.append(kw)

    calificacion = (puntos_obtenidos / puntos_maximos) * 100
    return {
        "calificacion": round(calificacion, 2),
        "puntos": f"{puntos_obtenidos}/{puntos_maximos}",
        "encontradas": encontradas,
        "faltantes": faltantes,
    }


# Diccionario de keywords para gobernanza de datos
keywords_governance = {
    # Core data governance (peso alto)
    "data governance": 5,
    "data quality": 4,
    "master data management": 4,
    "metadata": 3,
    "data lineage": 3,
    "data catalog": 3,
    "data stewardship": 3,
    "data privacy": 3,
    "compliance": 3,

    # Frameworks y estándares
    "DAMA": 3,
    "DMBOK": 3,
    "DCAM": 2,
    "GDPR": 2,
    "ISO 27001": 2,

    # Herramientas
    "Collibra": 3,
    "Informatica": 3,
    "Alation": 2,
    "Snowflake": 2,
    "Databricks": 2,
    "Power BI": 2,

    # Skills técnicos
    "SQL": 2,
    "Python": 2,
    "ETL": 2,
    "Azure": 1,
    "AWS": 1,

    # Certificaciones / dominio
    "CDMP": 2,
    "data architecture": 2,
    "data modeling": 1,
}

resultado = calificar_cv("ATSExampleResumeDataGovernance.pdf", keywords_governance)

print(f"Resultados de la evaluación del CV:")
print(f"Calificación: {resultado['calificacion']}%")
print(f"Puntos: {resultado['puntos']}")
print(f"\nEncontradas ({len(resultado['encontradas'])}):")
for kw, count in resultado['encontradas'].items():
    print(f"  OK {kw}: {count}x")
print(f"\nFaltantes ({len(resultado['faltantes'])}):")
for kw in resultado['faltantes']:
    print(f"  OK {kw}")
