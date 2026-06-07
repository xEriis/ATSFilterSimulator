"""
Catálogo de keywords ponderadas por categoría de puesto.
El "peso" representa la importancia relativa del keyword (1=menor, 5=crítico).

La lógica de la app es:
  1. El JD tiene un pool de keywords candidatas (este catálogo)
  2. Solo las keywords del pool que APAREZCAN en el JD específico se evaluan en el CV
  3. Esto hace que cada JD tenga su propio subset de keywords relevantes
"""

CATEGORY_LABELS = {
    'data-science': 'Data Science / ML',
    'data-engineering': 'Data Engineering',
    'cloud-engineering': 'Cloud Engineering',
    'devops-sre': 'DevOps / SRE',
    'data-analytics': 'Data Analytics',
    'data-governance': 'Data Governance / Leadership',
}


KEYWORD_CATALOG = {

    'data-science': {
        # Lenguajes y librerías
        'Python': 4, 'R': 2, 'SQL': 4, 'Scala': 2,
        'pandas': 3, 'NumPy': 2, 'scikit-learn': 3,
        'TensorFlow': 3, 'PyTorch': 3, 'XGBoost': 2, 'LightGBM': 1,
        'Hugging Face': 2, 'transformers': 2,
        # Conceptos ML
        'machine learning': 5, 'deep learning': 3, 'neural network': 2,
        'classification': 2, 'regression': 2, 'clustering': 2,
        'NLP': 3, 'computer vision': 2, 'time series': 2,
        'feature engineering': 3, 'hyperparameter': 2,
        'model deployment': 3, 'MLOps': 4, 'A/B test': 3, 'experimentation': 2,
        # Estadística
        'statistics': 3, 'hypothesis testing': 2, 'Bayesian': 1, 'probability': 1,
        'causal inference': 2,
        # Big data / infra
        'Spark': 3, 'Databricks': 3, 'Hadoop': 1, 'Kafka': 2,
        'Snowflake': 2, 'BigQuery': 2, 'Redshift': 2,
        # Cloud
        'AWS': 3, 'GCP': 2, 'Azure': 2, 'SageMaker': 2, 'Vertex AI': 2,
        # Tools
        'Jupyter': 1, 'Git': 1, 'Docker': 2, 'Airflow': 2, 'MLflow': 2,
        # Visualización
        'Tableau': 2, 'Power BI': 2, 'matplotlib': 1, 'seaborn': 1,
        # Soft / academic
        'PhD': 1, 'research': 2, 'publication': 1,
    },

    'data-engineering': {
        # Lenguajes
        'Python': 4, 'SQL': 5, 'Scala': 3, 'Java': 2, 'Go': 1,
        # Storage / DBs
        'PostgreSQL': 2, 'MySQL': 1, 'MongoDB': 2, 'Cassandra': 1,
        'Redis': 2, 'Elasticsearch': 2,
        # Data warehousing
        'Snowflake': 4, 'BigQuery': 4, 'Redshift': 4, 'Databricks': 3,
        'data warehouse': 4, 'data lake': 4, 'data lakehouse': 3,
        'dbt': 4, 'Delta Lake': 2, 'Iceberg': 1, 'Parquet': 2,
        # Pipelines
        'ETL': 5, 'ELT': 4, 'pipeline': 4, 'data pipeline': 5,
        'Airflow': 5, 'Prefect': 1, 'Dagster': 1, 'Luigi': 1,
        # Streaming
        'Kafka': 4, 'Kinesis': 2, 'Pub/Sub': 2, 'streaming': 3,
        'Spark': 4, 'Flink': 2, 'Beam': 1,
        # Cloud
        'AWS': 4, 'GCP': 3, 'Azure': 3, 'S3': 3, 'EMR': 2, 'Glue': 2,
        'Lambda': 2, 'Step Functions': 1,
        # Infra
        'Docker': 3, 'Kubernetes': 3, 'Terraform': 3, 'Git': 2,
        # Concepts
        'data modeling': 4, 'data quality': 3, 'schema': 2,
        'CDC': 1, 'orchestration': 3, 'partitioning': 2,
        # Observability
        'Grafana': 1, 'Datadog': 1, 'monitoring': 2,
    },

    'cloud-engineering': {
        # Cloud platforms
        'AWS': 5, 'Azure': 3, 'GCP': 4, 'Google Cloud': 3,
        # AWS services
        'EC2': 3, 'S3': 3, 'Lambda': 3, 'EKS': 3, 'ECS': 2,
        'RDS': 2, 'DynamoDB': 2, 'CloudFront': 1, 'IAM': 3,
        'VPC': 2, 'CloudFormation': 2, 'CloudWatch': 2,
        # GCP services
        'GKE': 2, 'Cloud Run': 2, 'Cloud Functions': 2, 'BigQuery': 2,
        # Azure services
        'AKS': 2, 'Azure DevOps': 1, 'Cosmos DB': 1,
        # IaC
        'Terraform': 5, 'CDK': 2, 'Pulumi': 1, 'Ansible': 2, 'CloudFormation': 2,
        # Containers
        'Docker': 4, 'Kubernetes': 5, 'Helm': 3, 'containerd': 1,
        # Languages
        'Python': 4, 'Go': 3, 'Bash': 3, 'JavaScript': 1, 'TypeScript': 1,
        # CI/CD
        'CI/CD': 4, 'GitHub Actions': 2, 'GitLab CI': 2, 'Jenkins': 2,
        'ArgoCD': 2,
        # Networking
        'VPN': 1, 'DNS': 2, 'load balancer': 2, 'TCP/IP': 1,
        'service mesh': 2, 'Istio': 1, 'Envoy': 1,
        # Security
        'security': 3, 'IAM policies': 2, 'encryption': 2, 'SSO': 1,
        'compliance': 2, 'SOC 2': 1, 'PCI-DSS': 1,
        # Observability
        'Prometheus': 2, 'Grafana': 2, 'Datadog': 2, 'OpenTelemetry': 2,
        # Architecture
        'microservices': 3, 'serverless': 3, 'event-driven': 2,
        'high availability': 3, 'disaster recovery': 2, 'multi-region': 2,
        # Certifications
        'Certified Solutions Architect': 3, 'Certified Cloud Practitioner': 2,
        'CKA': 2, 'CKAD': 1,
    },

    'devops-sre': {
        # Core SRE/DevOps
        'SRE': 4, 'Site Reliability': 4, 'DevOps': 4, 'platform engineering': 2,
        # Containers & orchestration
        'Kubernetes': 5, 'Docker': 4, 'Helm': 3, 'kubectl': 2,
        'ArgoCD': 3, 'GitOps': 3, 'Istio': 1,
        # CI/CD
        'CI/CD': 5, 'Jenkins': 3, 'GitHub Actions': 3, 'GitLab CI': 2,
        'Buildkite': 1, 'CircleCI': 1, 'Tekton': 1, 'pipeline': 2,
        # IaC
        'Terraform': 5, 'Ansible': 3, 'Pulumi': 2, 'Packer': 1, 'Chef': 1,
        # Languages
        'Python': 3, 'Go': 4, 'Bash': 4, 'Rust': 1,
        # Cloud
        'AWS': 4, 'GCP': 2, 'Azure': 2,
        # Observability
        'Prometheus': 4, 'Grafana': 4, 'Datadog': 3, 'New Relic': 1,
        'ELK': 2, 'Loki': 2, 'OpenTelemetry': 3, 'Jaeger': 1,
        'observability': 4, 'monitoring': 3, 'alerting': 2,
        # Reliability concepts
        'SLO': 4, 'SLI': 3, 'SLA': 2, 'error budget': 3, 'incident response': 4,
        'postmortem': 2, 'on-call': 2, 'MTTR': 2, 'chaos engineering': 2,
        # Networking & Linux
        'Linux': 4, 'networking': 2, 'TCP/IP': 1, 'DNS': 2,
        # Security
        'DevSecOps': 2, 'security': 2, 'secrets management': 1, 'Vault': 1,
        # Other
        'Git': 3, 'YAML': 1, 'distributed systems': 3,
        'high availability': 3, 'fault tolerance': 2,
        # Messaging
        'Kafka': 2, 'Redis': 2, 'PostgreSQL': 2,
    },

    'data-analytics': {
        # Querying
        'SQL': 5, 'BigQuery': 3, 'Snowflake': 3, 'Redshift': 2, 'PostgreSQL': 2,
        # BI Tools
        'Tableau': 4, 'Power BI': 4, 'Looker': 4, 'Mode': 2, 'Metabase': 1,
        'dashboards': 3, 'data visualization': 3, 'reporting': 3,
        # Data manipulation
        'Excel': 3, 'pivot tables': 2, 'VBA': 1, 'Google Sheets': 1,
        'pandas': 3, 'Python': 3, 'R': 2,
        # Analytics methods
        'A/B test': 4, 'experimentation': 3, 'statistics': 3,
        'hypothesis testing': 2, 'regression': 2, 'segmentation': 3,
        'cohort analysis': 2, 'funnel analysis': 2, 'attribution': 2,
        'causal inference': 1, 'forecasting': 2,
        # Business
        'KPI': 4, 'metric': 3, 'business intelligence': 4, 'BI': 4,
        'stakeholder': 3, 'storytelling': 2, 'executive': 2,
        'product analytics': 3, 'marketing analytics': 3, 'growth': 2,
        # Data engineering basics
        'dbt': 3, 'Airflow': 2, 'data pipeline': 2, 'ETL': 2,
        # Tools
        'Git': 1, 'Jupyter': 1, 'Hex': 1,
        # Certifications
        'PL-300': 1, 'Google Data Analytics': 2, 'Tableau Certified': 2,
        # Soft
        'communication': 2, 'cross-functional': 2,
    },

    'data-governance': {
        # Governance specific
        'data governance': 5, 'data quality': 5, 'master data management': 4,
        'MDM': 3, 'data stewardship': 4, 'data lineage': 4,
        'metadata': 4, 'data catalog': 4, 'data dictionary': 2,
        'business glossary': 2,
        # Frameworks
        'DAMA': 4, 'DMBOK': 4, 'DCAM': 3, 'CDMP': 3, 'COBIT': 2,
        # Compliance / regulations
        'compliance': 5, 'GDPR': 4, 'CCPA': 3, 'HIPAA': 2,
        'SOX': 2, 'PCI-DSS': 1, 'ISO 27001': 3, 'LFPDPPP': 2,
        'regulatory': 3, 'audit': 3,
        # Privacy & ethics
        'data privacy': 4, 'data ethics': 2, 'responsible AI': 2,
        'PII': 2, 'data classification': 3, 'data protection': 3,
        # Tools
        'Collibra': 4, 'Informatica': 4, 'Alation': 3,
        'Atlan': 2, 'Apache Atlas': 1,
        # Architecture
        'data architecture': 3, 'data strategy': 5, 'data mesh': 2,
        'data fabric': 1, 'lakehouse': 1,
        # Cloud (some)
        'Snowflake': 2, 'Databricks': 2, 'AWS': 2, 'Azure': 2,
        # Tech basics (sometimes needed)
        'SQL': 2, 'Python': 1, 'Power BI': 1, 'Tableau': 1,
        # Leadership
        'strategy': 3, 'leadership': 3, 'C-suite': 2, 'executive': 2,
        'transformation': 3, 'change management': 2, 'roadmap': 2,
        'stakeholder': 3, 'cross-functional': 2, 'budget': 2,
        # Risk
        'risk': 3, 'risk management': 3, 'data risk': 2,
    },
}