"""
Base de datos de ofertas de trabajo ficticias pero realistas.
Inspiradas en patrones reales de Databricks, Amazon, Google, Stripe, Spotify,
Mercado Libre, HSBC, Rappi, OpenAI, etc.

Cada oferta tiene:
- id: identificador único
- title: título del puesto
- company: empresa (ficticia o estilo de empresa real)
- location: ubicación
- level: senior/mid/junior
- category: una de las categorías de keywords_db.py
- language: 'en' o 'es'
- description: descripción completa (con todas las keywords integradas naturalmente)
"""

JOBS = [

    # ========================================================================
    # 1. DATA SCIENTIST en Databricks (EN, senior)
    # ========================================================================
    {
        'id': 'databricks_ds_senior',
        'title': 'Senior Data Scientist, Generative AI Platform',
        'company': 'Databricks',
        'location': 'San Francisco, CA / Remote',
        'level': 'senior',
        'category': 'data-science',
        'language': 'en',
        'description': """
About the Role

Databricks is the Data and AI company. As a Senior Data Scientist on our Generative AI
Platform team, you will design, build, and ship machine learning systems that power
recommendations, search, and personalization across the Databricks platform. You will
work side-by-side with engineering teams to take models from prototype to production at
massive scale.

What You'll Do
- Design and deploy machine learning and deep learning models for ranking, retrieval,
  and recommendation systems serving millions of users.
- Apply NLP techniques and transformers (Hugging Face, PyTorch) to power conversational
  AI features on the platform.
- Run rigorous A/B tests and experimentation to measure business impact; partner with
  product to interpret results.
- Build robust MLOps pipelines using MLflow, Airflow, and Spark on Databricks itself.
- Mentor junior data scientists and influence the team's research roadmap.
- Publish findings internally and externally where appropriate (papers, blog posts).

What We're Looking For
- 5+ years of experience as a data scientist or ML engineer in production environments.
- Strong fluency in Python and SQL; familiarity with Scala is a plus.
- Deep expertise in machine learning fundamentals: classification, regression,
  clustering, deep learning, feature engineering, hyperparameter tuning.
- Hands-on experience with PyTorch or TensorFlow for model training and fine-tuning.
- Practical experience deploying models with MLflow, MLOps best practices, and
  CI/CD for ML.
- Comfort with big data tooling: Spark, Databricks notebooks, Delta Lake.
- Experience designing and analyzing A/B tests; understanding of statistics and
  hypothesis testing.
- Excellent written and verbal communication skills.

Nice to Have
- PhD in Computer Science, Statistics, or related field.
- Publications at top ML venues (NeurIPS, ICML, ACL, EMNLP).
- Experience with AWS or GCP (we use both).
- Open source contributions to PyTorch, scikit-learn, or related projects.
""",
    },

    # ========================================================================
    # 2. DATA ENGINEER en Amazon Web Services (EN)
    # ========================================================================
    {
        'id': 'aws_data_engineer',
        'title': 'Data Engineer II, Data Platform Services',
        'company': 'Amazon Web Services',
        'location': 'Seattle, WA',
        'level': 'mid',
        'category': 'data-engineering',
        'language': 'en',
        'description': """
About the Team

The Data Platform Services team at AWS builds and operates the data infrastructure
powering critical business decisions across Amazon's retail, ads, and devices
organizations. We move petabytes daily and serve thousands of internal analysts,
data scientists, and ML engineers.

What You'll Do
- Design, build, and maintain large-scale ETL and ELT data pipelines using
  Apache Airflow, dbt, and Spark on EMR.
- Develop streaming pipelines with Kafka and Kinesis to power real-time analytics
  and ML feature stores.
- Architect data lakes on S3 with Parquet and Delta Lake; build data warehouse layers
  on Redshift and Snowflake.
- Implement data modeling best practices (Kimball, Data Vault) and rigorous data
  quality checks.
- Own end-to-end orchestration of complex multi-stage pipelines with strong SLAs.
- Partner with software engineers to ingest data from microservices via CDC
  (Debezium, DMS).
- Optimize query performance and storage cost; tune partitioning and clustering.

Basic Qualifications
- 4+ years of experience in data engineering.
- Strong programming in Python and expert-level SQL.
- Production experience with at least one data warehouse: Snowflake, BigQuery,
  or Redshift.
- Hands-on experience with Spark and orchestration tools like Airflow.
- Experience building cloud-native pipelines on AWS (S3, EMR, Glue, Lambda).
- Solid understanding of data modeling and dimensional design.

Preferred Qualifications
- Experience with dbt for analytics engineering.
- Knowledge of streaming systems (Kafka, Flink, Kinesis).
- Familiarity with Docker, Kubernetes, and Terraform for infrastructure as code.
- Experience with data observability tools and pipeline monitoring (Datadog,
  Grafana).
- AWS certifications (Solutions Architect, Big Data Specialty).
""",
    },

    # ========================================================================
    # 3. CLOUD ENGINEER en Google Cloud (EN)
    # ========================================================================
    {
        'id': 'gcp_cloud_architect',
        'title': 'Cloud Solutions Architect, Enterprise',
        'company': 'Google Cloud',
        'location': 'New York, NY / Hybrid',
        'level': 'senior',
        'category': 'cloud-engineering',
        'language': 'en',
        'description': """
The Role

As a Cloud Solutions Architect at Google Cloud, you will partner with enterprise
customers to design, build, and migrate workloads to GCP. You will be a trusted
advisor on cloud architecture, security, and operational excellence.

Responsibilities
- Design highly available, multi-region cloud architectures on GCP using
  GKE, Cloud Run, Cloud Functions, and BigQuery.
- Lead migrations from on-premises and other cloud providers (AWS, Azure) to GCP.
- Build infrastructure as code using Terraform; advise customers on best practices
  for CI/CD with Cloud Build and ArgoCD.
- Architect containerized microservices on Kubernetes (GKE) with Helm,
  Istio service mesh, and Envoy proxies.
- Implement serverless and event-driven patterns using Cloud Functions and Pub/Sub.
- Establish high availability and disaster recovery strategies with multi-region
  failover.
- Conduct architectural reviews and design workshops with customer engineering teams.
- Collaborate with security teams on IAM policies, encryption at rest and in transit,
  and compliance frameworks (SOC 2, ISO 27001, PCI-DSS).

Minimum Qualifications
- 7+ years of experience designing cloud architectures.
- Deep expertise in at least one major cloud provider; GCP strongly preferred,
  experience with AWS or Azure also valued.
- Production experience with Kubernetes, Docker, and Terraform.
- Strong programming in Python, Go, or Bash.
- Excellent customer-facing communication skills.
- Familiarity with networking concepts: VPN, DNS, load balancer, TCP/IP.

Preferred Qualifications
- Google Cloud Professional Cloud Architect certification.
- AWS Certified Solutions Architect Professional or equivalent.
- Certified Kubernetes Administrator (CKA) or CKAD.
- Experience with observability stacks: Prometheus, Grafana, Datadog,
  OpenTelemetry.
- Track record speaking at industry conferences or contributing to open source.
""",
    },

    # ========================================================================
    # 4. SRE/DevOps en Stripe (EN)
    # ========================================================================
    {
        'id': 'stripe_sre_senior',
        'title': 'Senior Site Reliability Engineer, Payments Infrastructure',
        'company': 'Stripe',
        'location': 'Remote (US)',
        'level': 'senior',
        'category': 'devops-sre',
        'language': 'en',
        'description': """
About the Team

Stripe processes over $1 trillion in payment volume annually. The Payments
Infrastructure SRE team keeps the core systems running at 99.999% availability.
We are looking for a Senior SRE who is passionate about distributed systems,
incident response, and building tools that make engineering teams move faster.

What You'll Do
- Operate and improve the reliability of Stripe's payment processing systems,
  serving millions of API requests per minute.
- Lead incident response for high-severity production issues; conduct blameless
  postmortems and drive systemic fixes.
- Define and enforce SLOs and SLIs across critical services; manage error budgets
  in partnership with product teams.
- Build observability tooling using Prometheus, Grafana, Datadog, and
  OpenTelemetry; instrument new services for tracing with Jaeger.
- Design and run chaos engineering exercises to surface resilience gaps before
  they cause outages.
- Improve CI/CD pipelines (Buildkite, GitHub Actions) for faster, safer deploys.
- Mentor engineers on SRE best practices: on-call hygiene, MTTR reduction,
  capacity planning.

What We're Looking For
- 6+ years of experience in DevOps, SRE, or platform engineering roles.
- Deep production experience operating Kubernetes at scale: kubectl, Helm,
  GitOps with ArgoCD.
- Strong programming skills in Go or Python; comfort with Bash scripting.
- Expertise in Linux internals, networking, and distributed systems.
- Hands-on experience with Terraform and infrastructure as code best practices.
- Track record of leading incident response and reducing MTTR.
- Experience with Kafka, Redis, PostgreSQL in high-throughput environments.

Bonus Points
- Open source contributions to Kubernetes, Prometheus, OpenTelemetry, or
  similar projects.
- Speaker at SRECon, KubeCon, or similar.
- Familiarity with DevSecOps practices and secrets management (Vault).
- Experience with multi-region high availability and fault tolerance.
""",
    },

    # ========================================================================
    # 5. DATA ANALYST en Spotify (EN)
    # ========================================================================
    {
        'id': 'spotify_data_analyst',
        'title': 'Senior Data Analyst, Product & Growth',
        'company': 'Spotify',
        'location': 'New York, NY / Hybrid',
        'level': 'senior',
        'category': 'data-analytics',
        'language': 'en',
        'description': """
About the Role

The Product & Growth Analytics team at Spotify drives data-informed decisions for
some of our most-loved features: Discover Weekly, Daily Mix, and personalized
podcast recommendations. We're hiring a Senior Data Analyst who can translate
ambiguous business questions into rigorous analyses that change product direction.

What You'll Do
- Partner with product managers and engineers on the Personalization team to
  design and analyze A/B tests on recommendation surfaces serving 600M+ users.
- Define and own KPIs and business intelligence dashboards in Looker, ensuring
  one source of truth across the org.
- Conduct deep-dive analyses on user behavior using SQL on BigQuery; surface
  insights about retention, engagement, and growth.
- Build cohort analysis, funnel analysis, and attribution models to understand
  user journeys.
- Use Python (pandas, scikit-learn) for ad-hoc statistical analysis and
  forecasting.
- Communicate findings clearly to executives through written reports and live
  presentations; storytelling with data is essential.
- Maintain dbt models in our analytics layer; collaborate with data engineering
  on data pipeline improvements.

What We're Looking For
- 5+ years of experience in analytics, business intelligence, or data science.
- Expert-level SQL skills; comfort working with large datasets in BigQuery,
  Snowflake, or similar.
- Strong experience with Tableau, Looker, Mode, or similar BI tools; you've
  built dashboards used by stakeholders.
- Deep understanding of A/B testing, hypothesis testing, and experimentation
  methodology.
- Proficiency in Python or R for data manipulation and statistical analysis.
- Track record of driving business decisions through analysis; comfortable
  communicating with executives.
- Experience working cross-functional with product, engineering, and design teams.

Nice to Have
- Prior experience in product analytics at a consumer tech company.
- Familiarity with dbt for analytics engineering.
- Tableau Certified Professional, PL-300, or Google Data Analytics certification.
- Experience with causal inference techniques and quasi-experimental designs.
""",
    },

    # ========================================================================
    # 6. DATA SCIENTIST SENIOR en Mercado Libre (ES)
    # ========================================================================
    {
        'id': 'meli_data_scientist',
        'title': 'Senior Data Scientist - Fraud & Risk',
        'company': 'Mercado Libre',
        'location': 'Ciudad de México, MX / Remoto LATAM',
        'level': 'senior',
        'category': 'data-science',
        'language': 'es',
        'description': """
Sobre el Rol

En Mercado Libre, el equipo de Fraud & Risk Data Science protege a millones de
compradores y vendedores en Latinoamérica. Buscamos un Data Scientist Senior
con experiencia en modelos de detección de fraude transaccional, machine learning
en producción y MLOps a escala.

¿Qué harás?
- Diseñar y desplegar modelos de machine learning para detección de fraude en
  tiempo real sobre billones de transacciones anuales.
- Implementar técnicas avanzadas de classification, feature engineering y
  ensemble learning con XGBoost, LightGBM y deep learning donde aplique.
- Construir pipelines de MLOps robustos utilizando MLflow, Airflow y Spark sobre
  nuestra plataforma de Databricks.
- Realizar A/B tests rigurosos para evaluar el impacto de nuevos modelos en
  métricas de negocio (tasa de fraude, falsos positivos, GMV protegido).
- Colaborar con equipos de producto, ingeniería y compliance para llevar modelos
  de prototipo a producción.
- Mentorizar a 2-3 data scientists junior del equipo.

Requisitos
- Más de 5 años de experiencia como Data Scientist, idealmente en fintech,
  e-commerce o banca.
- Dominio avanzado de Python y SQL; conocimiento de Scala es un plus.
- Experiencia comprobada con machine learning supervisado y técnicas de
  clustering aplicadas a fraude o riesgo.
- Práctica con scikit-learn, XGBoost, TensorFlow o PyTorch en producción.
- Experiencia con MLOps: model deployment, monitoreo de drift, retraining
  automatizado.
- Experimentation y A/B testing: diseño, ejecución, análisis estadístico,
  hypothesis testing.
- Manejo de big data: Spark, Databricks, data lake.
- Buena comunicación en español e inglés.

Deseable
- Maestría o PhD en estadística, computación, matemáticas o áreas afines.
- Experiencia previa con NLP o computer vision para casos de fraude documental.
- Conocimiento de AWS o GCP (usamos ambos), SageMaker o Vertex AI.
- Publication en venues de research o speaker en conferencias técnicas.
- Conocimiento de regulación financiera en LATAM.
""",
    },

    # ========================================================================
    # 7. CHIEF DATA OFFICER / Director en HSBC México (ES)
    # ========================================================================
    {
        'id': 'hsbc_director_governance',
        'title': 'Director de Gobierno de Datos / Chief Data Officer',
        'company': 'HSBC México',
        'location': 'Ciudad de México, MX',
        'level': 'executive',
        'category': 'data-governance',
        'language': 'es',
        'description': """
Resumen del Puesto

HSBC México busca un Director de Gobierno de Datos / Chief Data Officer (CDO)
para liderar la estrategia, gobernanza y arquitectura de datos a nivel
organizacional. Este rol reporta al COO y trabajará directamente con el C-suite
para transformar HSBC México en una organización verdaderamente data-driven.

Responsabilidades
- Definir e implementar la estrategia de datos (data strategy) a 5 años,
  alineada con los objetivos del negocio y la regulación bancaria.
- Liderar un equipo de más de 80 personas entre data stewards, arquitectos de
  datos, analistas de calidad y especialistas en compliance.
- Establecer y mantener el framework de data governance alineado a DAMA-DMBOK,
  DCAM y mejores prácticas internacionales.
- Asegurar el cumplimiento (compliance) con regulaciones aplicables: LFPDPPP,
  GDPR (operaciones internacionales), CCPA, ISO 27001, SOX y normativa de la CNBV.
- Implementar y mantener el data catalog y procesos de data lineage usando
  Collibra; consolidar metadata management para 15,000+ data elements críticos.
- Liderar el programa de data quality y master data management (MDM) con
  Informatica.
- Desarrollar la disciplina de data stewardship a través de la organización.
- Establecer políticas de data privacy, data classification y data protection
  (PII), incluyendo controles para responsible AI.
- Gestionar un budget anual de más de USD 25M; reportar mensualmente al Board
  sobre risk management, data quality y madurez del gobierno de datos.
- Liderar la transformation digital del área de datos hacia arquitectura moderna
  (data lakehouse, Snowflake, Databricks).

Requisitos
- Más de 15 años de experiencia en data leadership, con al menos 7 años en
  roles ejecutivos de gobierno de datos o estrategia de datos.
- Experiencia comprobada implementando data governance en instituciones
  financieras o sectores regulados.
- Certificación CDMP (DAMA International) o equivalente; familiaridad profunda
  con DAMA-DMBOK, DCAM, COBIT.
- Track record liderando transformation y change management a gran escala.
- Experiencia gestionando relaciones con reguladores (CNBV, Banxico).
- Conocimiento de herramientas: Collibra, Informatica, Alation, Atlan.
- Familiaridad con arquitecturas modernas: data mesh, lakehouse, cloud
  (AWS, Azure).
- Habilidades excepcionales de stakeholder management y comunicación con C-suite.
- Maestría en disciplinas relacionadas (MBA preferido).
- Español e inglés fluentes.

Deseable
- Experiencia previa como CDO o Director de Datos.
- Conocimientos básicos de SQL, Python, Power BI o Tableau (no es rol técnico,
  pero la fluidez técnica es valorada).
- Publication o speaking en foros de la industria.
""",
    },

    # ========================================================================
    # 8. JUNIOR DATA ANALYST en Rappi (ES, entry-level)
    # ========================================================================
    {
        'id': 'rappi_data_analyst_jr',
        'title': 'Data Analyst Junior - Operaciones',
        'company': 'Rappi',
        'location': 'Ciudad de México, MX',
        'level': 'junior',
        'category': 'data-analytics',
        'language': 'es',
        'description': """
Sobre el Rol

En Rappi, el equipo de Operaciones está buscando un Data Analyst Junior para
apoyar la toma de decisiones del negocio mediante análisis de datos, dashboards
y reportes. Este es un excelente rol de entrada para alguien con sólida formación
cuantitativa que quiera crecer en analytics dentro de una de las empresas tech
más importantes de LATAM.

¿Qué harás?
- Construir y mantener dashboards de business intelligence en Tableau y Looker
  para los equipos de operaciones, courier y customer support.
- Escribir queries de SQL complejas sobre BigQuery y Snowflake para extraer
  insights operativos.
- Apoyar en el diseño, ejecución y análisis de A/B tests para mejorar la
  experiencia del usuario y la eficiencia operativa.
- Realizar análisis de cohort analysis, funnel analysis y segmentation para
  entender el comportamiento de usuarios y couriers.
- Definir y reportar KPIs operativos clave: tiempo de entrega, tasa de
  cancelación, satisfacción del courier.
- Trabajar cross-functional con product managers, ingeniería y operaciones.
- Crear reportes ejecutivos con storytelling claro para el liderazgo.
- Usar Python (pandas) y Excel avanzado para análisis ad-hoc.

Requisitos
- Recién egresado o hasta 2 años de experiencia en roles de Data Analyst,
  Business Intelligence o similar.
- Licenciatura en Actuaría, Estadística, Matemáticas, Economía, Ingeniería
  Industrial o áreas afines.
- SQL intermedio-avanzado (queries con joins, subqueries, window functions).
- Manejo de al menos una herramienta de BI: Tableau, Power BI, Looker o Mode.
- Excel avanzado: pivot tables, fórmulas, idealmente algo de VBA.
- Python básico (pandas, matplotlib) para análisis ad-hoc.
- Conocimientos de statistics e hypothesis testing.
- Pensamiento analítico y atención al detalle.
- Capacidad de comunicación clara con stakeholders no técnicos.
- Español nativo, inglés intermedio (lectura técnica).

Deseable
- Certificaciones: Google Data Analytics, PL-300 (Power BI), Tableau Certified.
- Experiencia con dbt o Airflow.
- Conocimiento de metric frameworks tipo AARRR, North Star metric, etc.
- Experiencia trabajando con datos de operaciones, marketplaces o e-commerce.
""",
    },
    # ========================================================================
    # 9. SOFTWARE ENGINEERING INTERN en Google (EN)
    # ========================================================================
    {
        'id': 'google_swe_intern',
        'title': 'Software Engineering Intern, Cloud Infrastructure',
        'company': 'Google',
        'location': 'Mountain View, CA / Multiple US locations',
        'level': 'junior',
        'category': 'cloud-engineering',
        'language': 'en',
        'description': """
About the Internship

Google's Software Engineering Internship is a 12-14 week paid program for current
undergraduate and graduate students. As an SWE Intern on a Cloud Infrastructure
team, you'll work alongside experienced engineers on systems powering Google Cloud
(GCP) at planetary scale, with strong potential to convert to a full-time SWE
role after graduation.

What You'll Do
- Contribute production code to backend services on Google Cloud Platform.
- Build and improve tooling around Kubernetes (GKE), Docker, and microservices.
- Write automated tests, participate in code review, and ship features to
  production with your mentor's guidance.
- Use Python, Go, or Java depending on your team's stack.
- Participate in design reviews and propose technical improvements.

Minimum Qualifications
- Currently pursuing a Bachelor's or Master's degree in Computer Science,
  Computer Engineering, or related technical field. Expected graduation in 2026
  or 2027.
- Programming experience in Python, Go, Java, C++, or similar.
- Familiarity with Linux, Git, and networking concepts (TCP/IP, DNS).
- Coursework in data structures, algorithms, and operating systems.

Preferred Qualifications
- Prior internship, research, or open-source experience.
- Familiarity with Docker, Kubernetes, CI/CD pipelines, or Terraform.
- Experience with at least one cloud platform: GCP, AWS, or Azure.
- Strong problem-solving skills and ability to learn quickly.

Program Highlights
- Competitive intern salary plus relocation/housing support.
- Direct mentorship from senior engineers.
- Performance-based conversion to full-time SWE role.
""",
    },

    # ========================================================================
    # 10. DATA SCIENCE INTERN en Oracle (EN)
    # ========================================================================
    {
        'id': 'oracle_ds_intern',
        'title': 'Data Science Intern, Oracle Cloud AI Services',
        'company': 'Oracle',
        'location': 'Austin, TX / Remote (US)',
        'level': 'junior',
        'category': 'data-science',
        'language': 'en',
        'description': """
The Opportunity

Oracle Cloud Infrastructure (OCI) is hiring Data Science Interns for our summer
program (12 weeks). You'll work on Oracle's AI Services platform, building and
evaluating machine learning models that power features used by enterprise customers
worldwide. This is an ideal opportunity for students looking to gain production
ML experience.

What You'll Do
- Develop machine learning prototypes using Python, scikit-learn, TensorFlow,
  or PyTorch for real customer use cases.
- Run statistical analysis and A/B tests to evaluate model performance.
- Work with feature engineering pipelines and explore approaches in NLP and
  classification.
- Use SQL to extract and analyze data from Oracle databases and OCI data warehouses.
- Present findings to your team and senior data scientists in weekly research
  reviews.

Minimum Qualifications
- Currently pursuing an MS or PhD in Computer Science, Statistics, Mathematics,
  Data Science, or related quantitative field.
- Strong programming in Python and pandas; experience with at least one ML
  framework (scikit-learn, TensorFlow, PyTorch).
- Solid foundation in statistics, hypothesis testing, and probability.
- Working knowledge of SQL.
- Coursework or projects in machine learning.

Preferred Qualifications
- Familiarity with deep learning and neural networks.
- Experience with cloud platforms (AWS, GCP, Azure) or MLOps tooling
  (MLflow, Airflow).
- Exposure to big data tools (Spark, Snowflake, BigQuery).
- Publication, research, or open-source contributions in ML.

Why Oracle?
- Work on infrastructure used by Fortune 500 enterprises and governments.
- Mentorship from PhD-level data scientists.
- Conversion to full-time Data Scientist role for top performers.
""",
    },

    # ========================================================================
    # 11. BECARIO ACTUARIAL en Deloitte México (ES)
    # ========================================================================
    {
        'id': 'deloitte_actuarial_intern',
        'title': 'Becario Actuarial - Consultoría en Riesgos',
        'company': 'Deloitte México',
        'location': 'Ciudad de México, MX',
        'level': 'junior',
        'category': 'data-analytics',
        'language': 'es',
        'description': """
Sobre la Posición

Deloitte México está buscando Becarios Actuariales para integrarse a nuestro
equipo de Consultoría Actuarial y Gestión de Riesgos. Es un programa de 6 meses
(con posibilidad de extensión y contratación) dirigido a estudiantes de Actuaría,
Matemáticas, Estadística o Economía en últimos semestres.

¿Qué harás?
- Apoyar en proyectos de valuación actuarial, reservas técnicas y estudios de
  experiencia para clientes del sector asegurador y financiero.
- Realizar análisis cuantitativo y modelación estadística usando Excel avanzado
  (incluyendo VBA y pivot tables), R y Python.
- Construir dashboards y reporting ejecutivo en Power BI y Tableau para
  presentar hallazgos a clientes.
- Escribir queries de SQL sobre bases de datos de pólizas y siniestros para
  analytics.
- Apoyar en estudios de cumplimiento regulatorio (Solvencia II, IFRS 17, CNSF).
- Colaborar cross-functional con consultores senior, gerentes y socios.
- Participar en presentaciones a stakeholders del cliente.

Requisitos
- Estudiante regular de Actuaría, Matemáticas Aplicadas, Estadística o Economía,
  cursando del 6° semestre en adelante.
- Promedio mínimo de 8.5/10.
- Excel avanzado: pivot tables, fórmulas complejas, idealmente VBA.
- Conocimientos sólidos de statistics, regression, hypothesis testing y
  probability.
- Familiaridad con al menos uno: R, Python (pandas), SQL.
- Excelentes habilidades de comunicación oral y escrita.
- Inglés intermedio o avanzado (B2+).

Deseable
- Experiencia previa con Power BI, Tableau o Looker.
- Conocimientos básicos de KPI financieros y métricas de seguros.
- Participación en concursos académicos o investigación.
- Disponibilidad de 30-40 horas semanales.

Lo que ofrecemos
- Beca económica competitiva.
- Mentoría directa de consultores senior y socios.
- Capacitación técnica en metodologías actuariales y herramientas de la firma.
- Alta posibilidad de incorporación de tiempo completo al egresar.
""",
    },

    # ========================================================================
    # 12. CLOUD ENGINEERING INTERN en Microsoft (EN)
    # ========================================================================
    {
        'id': 'microsoft_cloud_intern',
        'title': 'Cloud Engineering Intern, Azure Platform',
        'company': 'Microsoft',
        'location': 'Redmond, WA / Multiple US locations',
        'level': 'junior',
        'category': 'cloud-engineering',
        'language': 'en',
        'description': """
The Internship

Microsoft is hiring Cloud Engineering Interns for a 12-week summer program with
the Azure Platform organization. You'll work on services and tooling that power
Azure for millions of customers. This is a hands-on, project-based internship
with strong full-time conversion rates.

Responsibilities
- Build features and tooling for Azure services using C#, Python, or Go.
- Work with Kubernetes (AKS), Docker, and microservices architectures in
  production environments.
- Contribute to infrastructure as code using Terraform and ARM templates.
- Participate in code review, testing, and CI/CD pipeline development using
  Azure DevOps and GitHub Actions.
- Collaborate with senior engineers on system design and reliability
  improvements.
- Investigate and debug issues in distributed systems with the support of
  observability tools (Prometheus, Grafana, Datadog).

Minimum Qualifications
- Currently pursuing a BS, MS, or PhD in Computer Science, Computer Engineering,
  or related field. Expected graduation in 2026 or 2027.
- Programming experience in Python, C#, Go, Java, or similar.
- Familiarity with Linux, Git, and Bash scripting.
- Understanding of networking concepts: TCP/IP, DNS, load balancer.

Preferred Qualifications
- Hands-on experience with at least one cloud platform: Azure, AWS, or GCP.
- Familiarity with containers (Docker), Kubernetes, or serverless patterns.
- Experience with CI/CD tools and infrastructure as code.
- Prior internship, hackathon, or open-source contributions.
- Microsoft Certified: Azure Fundamentals (AZ-900) is a plus.

Benefits
- Competitive intern compensation plus housing/relocation support.
- Mentorship from senior cloud engineers and architects.
- Access to internal training on Azure services and certifications.
- Conversion path to Software Engineer or Cloud Engineer FTE role.
""",
    },

    # ========================================================================
    # 13. BECARIO CUANTITATIVO en Mercer México (ES)
    # ========================================================================
    {
        'id': 'mercer_quant_intern',
        'title': 'Becario de Análisis Cuantitativo - Beneficios y Pensiones',
        'company': 'Mercer México',
        'location': 'Ciudad de México, MX / Híbrido',
        'level': 'junior',
        'category': 'data-analytics',
        'language': 'es',
        'description': """
Sobre el Programa

Mercer, líder global en consultoría de capital humano, salud y patrimonio,
busca Becarios de Análisis Cuantitativo para su práctica de Wealth (Beneficios
y Pensiones). Programa de 6-12 meses para estudiantes de Actuaría, Estadística,
Matemáticas o áreas afines, con opción a contratación al egresar.

¿Qué harás?
- Realizar valuaciones actuariales de planes de pensiones, fondos de retiro y
  beneficios post-empleo para empresas multinacionales.
- Construir modelos de proyección y forecasting financiero en Excel avanzado
  (incluyendo VBA y pivot tables) y R.
- Analizar grandes volúmenes de datos demográficos y financieros usando SQL
  y Python (pandas).
- Crear reporting y dashboards en Power BI para presentar hallazgos a clientes.
- Apoyar estudios de benchmarking de compensación y métricas (KPI) de capital
  humano.
- Documentar metodologías y mantener la calidad y reproducibilidad del análisis.
- Participar en reuniones con clientes acompañando a consultores senior.

Requisitos
- Estudiante regular de Actuaría, Estadística, Matemáticas, Economía o
  Ingeniería Industrial, cursando entre el 5° y 9° semestre.
- Promedio mínimo de 8.5/10.
- Excel avanzado, incluyendo dominio de tablas dinámicas, fórmulas y
  preferentemente VBA.
- Sólida formación en statistics, regression, probability e hypothesis testing.
- Conocimientos básicos de SQL.
- Manejo básico de Python o R (pandas, dplyr, ggplot2).
- Pensamiento crítico, atención al detalle y capacidad de communication con
  stakeholders.
- Inglés intermedio (B2+) — los proyectos a menudo involucran equipos
  internacionales.

Deseable
- Experiencia previa con Power BI o Tableau.
- Conocimientos básicos de mercados financieros y matemáticas actuariales.
- Participación en concursos académicos, hackathons o investigación.

Beneficios
- Beca económica competitiva.
- Modalidad híbrida.
- Mentoría directa de consultores y actuarios certificados.
- Capacitación en metodologías Mercer y herramientas propietarias.
""",
    },

    # ========================================================================
    # 14. MACHINE LEARNING ENGINEERING INTERN en Meta (EN)
    # ========================================================================
    {
        'id': 'meta_mle_intern',
        'title': 'Machine Learning Engineering Intern, Ranking & Recommendations',
        'company': 'Meta',
        'location': 'Menlo Park, CA / New York, NY',
        'level': 'junior',
        'category': 'data-science',
        'language': 'en',
        'description': """
About the Role

Meta is hiring Machine Learning Engineering Interns for a 12-16 week program
embedded in production teams across Facebook, Instagram, WhatsApp, and Reality
Labs. You'll work on ML systems that affect billions of users daily. This
internship is geared toward MS and PhD students with a strong research and
engineering foundation.

What You'll Do
- Build and train deep learning models (using PyTorch) for ranking, retrieval,
  and recommendation systems.
- Run rigorous experimentation including A/B tests to evaluate model impact on
  user-facing metrics.
- Contribute to ML feature engineering pipelines and MLOps tooling on Meta's
  internal platforms.
- Explore approaches in NLP, computer vision, or large neural network
  architectures depending on team focus.
- Collaborate with research scientists and senior engineers on novel
  approaches; some interns publish their work.
- Present project results to senior leaders at the end of the internship.

Minimum Qualifications
- Currently pursuing an MS or PhD in Computer Science, Machine Learning,
  Statistics, Mathematics, or related field. Expected graduation 2026 or 2027.
- Strong programming in Python and SQL.
- Hands-on experience with PyTorch or TensorFlow for training deep learning
  models.
- Deep understanding of machine learning fundamentals: classification,
  regression, neural network architectures, feature engineering.
- Coursework or research in at least one of: NLP, computer vision, deep
  learning, recommendation systems.

Preferred Qualifications
- Publication at top-tier ML conferences (NeurIPS, ICML, ACL, EMNLP, CVPR).
- Experience with large-scale distributed training and MLOps tooling
  (MLflow, Airflow, Spark).
- Familiarity with Hugging Face transformers and modern foundation models.
- Prior internship experience at a tech company or research lab.
- Strong written communication for research papers and design docs.

Why Meta?
- Work on ML systems at unprecedented scale.
- Direct mentorship from senior research scientists and ML engineers.
- High conversion rate to full-time MLE roles.
- Industry-leading compensation for interns.
""",
    },

    # ========================================================================
    # 15. BECARIO DE INTELIGENCIA DE NEGOCIOS en Banorte (ES)
    # ========================================================================
    {
        'id': 'banorte_bi_intern',
        'title': 'Becario de Inteligencia de Negocios - Banca Digital',
        'company': 'Grupo Financiero Banorte',
        'location': 'Monterrey, NL / Ciudad de México, MX',
        'level': 'junior',
        'category': 'data-analytics',
        'language': 'es',
        'description': """
Sobre la Posición

Banorte, uno de los grupos financieros más grandes de México, está reclutando
Becarios de Inteligencia de Negocios para integrarse al área de Banca Digital.
Programa de 6-12 meses dirigido a estudiantes de últimos semestres en carreras
afines a datos, con alta probabilidad de contratación al concluir.

Responsabilidades
- Construir y mantener dashboards de business intelligence en Power BI y Tableau
  consultados por directivos del área digital.
- Escribir queries de SQL de complejidad media-alta sobre data warehouses
  internos (Snowflake y bases SQL Server) para extraer insights de negocio.
- Apoyar en el análisis de KPI clave: adopción de productos digitales,
  conversión de funnel, tasa de retención y crecimiento de usuarios activos.
- Realizar análisis ad-hoc usando Excel avanzado (pivot tables, VBA) y
  Python (pandas) para apoyar decisiones del equipo de producto.
- Diseñar y analizar pruebas A/B test para nuevas funcionalidades de banca
  móvil.
- Construir reporting periódico y storytelling con datos para presentar al
  liderazgo.
- Colaborar cross-functional con product managers, equipos de ingeniería y
  riesgo.

Requisitos
- Estudiante regular cursando 6° semestre en adelante de: Actuaría, Estadística,
  Matemáticas, Ingeniería Industrial, Sistemas, Economía o áreas afines.
- Promedio mínimo de 8.5/10.
- SQL nivel intermedio: joins, subqueries, window functions.
- Manejo de al menos una herramienta de BI: Power BI, Tableau o Looker.
- Excel avanzado.
- Conocimientos básicos de statistics, hypothesis testing y métodos de
  segmentation.
- Python básico (pandas, matplotlib) para análisis ad-hoc.
- Pensamiento analítico y atención al detalle.
- Buenas habilidades de communication con stakeholders no técnicos.

Deseable
- Certificaciones: PL-300 (Power BI), Google Data Analytics, Tableau Certified.
- Conocimientos básicos del sector financiero o banca.
- Experiencia previa en proyectos académicos con análisis de datos reales.
- Familiaridad con cohort analysis y attribution analysis.

Lo que ofrecemos
- Beca económica competitiva, vales de despensa y seguro de gastos médicos
  menores.
- Horario híbrido flexible (3 días oficina, 2 remoto).
- Mentoría de líderes del área de analytics y BI.
- Plan de carrera definido con oportunidad de contratación al egresar.
""",
    },
    # ========================================================================
    # 16. DATA ENGINEER (MID-LEVEL) en Grupo Bimbo (ES)
    # ========================================================================
    {
        'id': 'bimbo_data_engineer_mid',
        'title': 'Data Engineer - Plataforma de Datos Global',
        'company': 'Grupo Bimbo',
        'location': 'Ciudad de México, MX / Híbrido',
        'level': 'mid',
        'category': 'data-engineering',
        'language': 'es',
        'description': """
Sobre el Rol

Grupo Bimbo, la panificadora más grande del mundo con operaciones en más de 33
países, está expandiendo su equipo de Data Platform. Buscamos un Data Engineer
con 2-3 años de experiencia para construir y mantener pipelines de datos que
soportan analytics y machine learning a escala global.

¿Qué harás?
- Diseñar, desarrollar y mantener pipelines de ETL y ELT usando Apache Airflow,
  dbt y Spark para procesar datos de ventas, supply chain y manufactura.
- Modelar y mantener el data warehouse de la compañía en Snowflake (también
  evaluamos migrar a BigQuery en algunas regiones).
- Construir capas de data lake sobre AWS S3 usando Parquet y Delta Lake.
- Implementar pipelines de streaming con Kafka para casos de uso de telemetría
  de fábrica e inventario en tiempo real.
- Asegurar la calidad y observabilidad de los datos: monitoring, alerting,
  pruebas con dbt tests.
- Colaborar con analistas de BI y data scientists para entregar datasets
  confiables y bien documentados.
- Aplicar buenas prácticas de data modeling (Kimball, Data Vault).

Requisitos
- 2-4 años de experiencia como Data Engineer o role equivalente.
- Dominio avanzado de SQL y Python.
- Experiencia en producción con al menos un data warehouse: Snowflake,
  BigQuery o Redshift.
- Experiencia con orquestación: Airflow, Prefect o Dagster.
- Conocimiento práctico de Apache Spark.
- Manejo de Git y prácticas de code review.
- Cloud: AWS, GCP o Azure (idealmente AWS, pero todos cuentan).

Deseable
- Experiencia con dbt y analytics engineering.
- Familiaridad con Kafka, Kinesis o Pub/Sub.
- Docker, Kubernetes, Terraform para infrastructure as code.
- Observabilidad con Datadog, Grafana o monitoring tools similares.
- Inglés conversacional (B2+).
""",
    },

    # ========================================================================
    # 17. DEVOPS ENGINEER (MID) en Cloudflare (EN)
    # ========================================================================
    {
        'id': 'cloudflare_devops_mid',
        'title': 'DevOps Engineer, Edge Infrastructure',
        'company': 'Cloudflare',
        'location': 'Remote (Americas)',
        'level': 'mid',
        'category': 'devops-sre',
        'language': 'en',
        'description': """
About the Team

Cloudflare runs one of the world's largest networks, serving traffic for
millions of websites. The Edge Infrastructure team builds the platform and
automation that lets engineering teams ship safely to our global network. We're
hiring a mid-level DevOps Engineer (2-4 years experience) to join us.

What You'll Do
- Build and improve CI/CD pipelines using GitHub Actions, GitLab CI, and ArgoCD.
- Operate and harden internal Kubernetes platforms; build Helm charts and
  GitOps workflows for engineering teams.
- Write Terraform modules to automate cloud infrastructure provisioning on AWS
  and GCP.
- Improve observability across our services using Prometheus, Grafana, and
  OpenTelemetry; participate in monitoring and alerting design.
- Participate in the on-call rotation; help drive incident response, write
  postmortems, and reduce MTTR over time.
- Contribute to SLO/SLI definitions and error budget conversations with
  product teams.
- Write tooling in Go, Python, and Bash to automate repetitive ops work.

What We're Looking For
- 2-4 years of experience in DevOps, SRE, or platform engineering.
- Production experience operating Kubernetes (kubectl, Helm).
- Strong scripting and programming skills in Go, Python, or Bash.
- Hands-on experience with Terraform and infrastructure as code.
- Experience with at least one major cloud provider (AWS, GCP, or Azure).
- Familiarity with CI/CD design and pipeline tooling.
- Working knowledge of Linux internals and networking.

Nice to Have
- Experience with Istio service mesh, eBPF tooling, or chaos engineering.
- Familiarity with Datadog, ELK, or similar observability stacks.
- Open source contributions to Kubernetes, Terraform providers, or related
  projects.
- Certifications: CKA, CKAD, AWS DevOps Engineer Professional.
- DevSecOps experience: secrets management with Vault, SAST/DAST tooling.

Benefits
- Fully remote with quarterly team offsites.
- Competitive compensation and equity.
- Career growth in SRE/platform engineering.
""",
    },

    # ========================================================================
    # 18. DATA GOVERNANCE ANALYST (MID) en BBVA México (ES)
    # ========================================================================
    {
        'id': 'bbva_governance_mid',
        'title': 'Especialista en Gobierno de Datos - Banca de Inversión',
        'company': 'BBVA México',
        'location': 'Ciudad de México, MX',
        'level': 'mid',
        'category': 'data-governance',
        'language': 'es',
        'description': """
Sobre la Posición

BBVA México está creciendo su área de Gobierno de Datos para fortalecer la
calidad, trazabilidad y cumplimiento regulatorio de la información financiera.
Buscamos un Especialista con 3-5 años de experiencia que combine sensibilidad
técnica y conocimiento de la regulación bancaria.

Responsabilidades
- Implementar y mantener el framework de data governance del banco, alineado
  con DAMA-DMBOK y DCAM.
- Gestionar el data catalog en Collibra: cargar metadata, definir data
  lineage y mantener el business glossary para data elements críticos.
- Coordinar con data stewards de las áreas de negocio (riesgo, crédito,
  banca privada) para asegurar la calidad y completitud de los datos.
- Implementar reglas de data quality en Informatica IDQ y monitorear
  indicadores semanalmente.
- Apoyar en compliance con regulaciones aplicables: LFPDPPP, GDPR (operaciones
  internacionales), Basel III, CNBV, ISO 27001.
- Diseñar y aplicar políticas de data classification y data protection (PII).
- Documentar metadata management para 5,000+ data elements en sistemas core.
- Apoyar auditorías internas y externas relacionadas con gobierno de datos.

Requisitos
- 3-5 años de experiencia en data governance, data quality o data management.
- Conocimiento sólido de DAMA-DMBOK o DCAM (certificación CDMP es un plus).
- Experiencia hands-on con al menos una herramienta: Collibra, Informatica,
  Alation o Atlan.
- Conocimientos básicos de SQL para validar data lineage y queries de
  data quality.
- Familiaridad con regulación bancaria mexicana (CNBV, Banxico) o internacional.
- Buenas habilidades de communication; capacidad para trabajar cross-functional
  con áreas técnicas y de negocio.
- Licenciatura en Sistemas, Actuaría, Estadística, Economía, Derecho o
  equivalente.
- Inglés conversacional (B2+).

Deseable
- Certificación CDMP (DAMA International).
- Conocimiento de arquitecturas modernas: data mesh, lakehouse, Snowflake,
  Databricks.
- Experiencia previa en banca, seguros u otro sector altamente regulado.
- Familiaridad con cumplimiento de responsible AI y data ethics.
- Conocimientos básicos de Python o Power BI para análisis ad-hoc.

Lo que ofrecemos
- Salario competitivo + bonos por desempeño.
- Esquema híbrido (3 días oficina, 2 remoto).
- Plan de carrera dentro del área de Gobierno y Estrategia de Datos.
- Acceso a certificaciones técnicas y de gobierno (DAMA, etc.).
""",
    },

    # ========================================================================
    # 19. DATA SCIENTIST II en Snowflake (EN)
    # ========================================================================
    {
        'id': 'snowflake_ds_mid',
        'title': 'Data Scientist II, Customer Analytics',
        'company': 'Snowflake',
        'location': 'San Mateo, CA / Remote (US)',
        'level': 'mid',
        'category': 'data-science',
        'language': 'en',
        'description': """
About the Role

Snowflake is hiring a Data Scientist II to join our Customer Analytics team.
You'll partner with go-to-market, product, and engineering leaders to surface
insights and build predictive models that drive Snowflake's growth. This role
is ideal for a data scientist with 2-4 years of experience looking to make
business impact at one of the fastest-growing enterprise software companies.

What You'll Do
- Build machine learning models to predict customer churn, expansion potential,
  and product engagement using Python, scikit-learn, and XGBoost.
- Run rigorous A/B tests on product features and customer-facing campaigns;
  analyze results using statistics and hypothesis testing.
- Conduct deep-dive analyses combining clickstream, billing, and CRM data
  using SQL on (yes) Snowflake itself, our primary analytics warehouse.
- Build forecasting models for revenue, usage, and capacity planning.
- Partner with data engineering to productionize models using MLflow and
  Airflow; collaborate on MLOps best practices.
- Communicate findings clearly to executives and cross-functional partners.
- Mentor junior analysts and contribute to the team's experimentation
  playbook.

Basic Qualifications
- 2-4 years of experience in data science or applied machine learning roles.
- Strong proficiency in Python (pandas, scikit-learn) and SQL.
- Solid foundation in machine learning fundamentals: classification,
  regression, feature engineering, hyperparameter tuning.
- Hands-on experience designing and analyzing A/B tests.
- Strong statistics background: hypothesis testing, probability, regression.
- Excellent written and verbal communication.

Preferred Qualifications
- Experience with MLOps tools: MLflow, Airflow, model deployment in production.
- Familiarity with deep learning frameworks (PyTorch or TensorFlow) is a plus.
- Knowledge of Spark or distributed computing.
- Experience working with B2B SaaS metrics (ARR, NDR, LTV, churn).
- Cloud experience: AWS, GCP, or Azure.
- Master's degree in CS, Statistics, Mathematics, Economics, or related field.

Why Snowflake?
- Work with one of the most-loved data platforms in the industry.
- Strong career path; we promote heavily from within.
- Equity, competitive comp, and full remote flexibility.
""",
    },
]


# Helpers para uso desde la app
def get_jobs_by_category(category: str) -> list:
    """Devuelve todos los jobs de una categoría."""
    return [j for j in JOBS if j['category'] == category]


def get_job_by_id(job_id: str) -> dict | None:
    """Busca un job por su ID único."""
    return next((j for j in JOBS if j['id'] == job_id), None)


def get_categories_with_jobs() -> dict:
    """Devuelve dict {categoría: lista de jobs} para la UI."""
    result = {}
    for job in JOBS:
        result.setdefault(job['category'], []).append(job)
    return result