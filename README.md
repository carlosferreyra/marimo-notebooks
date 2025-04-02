# Data Engineering Interactive Portfolio

Welcome to my interactive data engineering portfolio! This repository showcases real-world data
engineering implementations using [marimo](https://marimo.io) notebooks, demonstrating hands-on
experience with cloud platforms and data processing pipelines.

## 🎯 Portfolio Overview

This portfolio demonstrates practical implementations of data engineering concepts across major
cloud platforms:

### Cloud Platform Implementations

- `notebooks/GCP.py`: Google Cloud Platform implementations showcasing:

  - BigQuery data warehousing
  - Cloud Storage data lakes
  - Dataflow pipelines
  - Cloud Functions for serverless ETL _(GCP Professional Data Engineer Certified)_

- `notebooks/AWS.py`: Amazon Web Services implementations featuring:

  - S3 and Glue ETL workflows
  - Redshift data warehousing
  - Lambda for data processing
  - EMR for big data processing

- `notebooks/Databricks.py`: Enterprise data processing featuring:
  - Delta Lake architecture
  - Spark SQL optimizations
  - Data pipeline orchestration
  - Real-time data processing

### Key Technical Highlights

- **Modern Data Stack**: Python, Polars, dbt, Airflow
- **Data Processing**: ETL/ELT pipelines, batch/streaming processing
- **Backend Integration**: RESTful APIs, microservices architecture
- **Best Practices**: CI/CD, Infrastructure as Code, data testing

## 🚀 Interactive Demonstrations

Each notebook is an interactive demonstration that you can run and modify:

1. Data Pipeline Implementations
2. Real-time Data Processing
3. Data Quality Monitoring
4. Performance Optimization
5. API Integrations

## 💡 Technical Background

- Strong focus on backend development with Python
- Experience in designing scalable data architectures
- Expertise in cloud-native solutions
- Emphasis on code quality and testing

## 🛠️ Getting Started

1. Clone this repository
2. Install dependencies using `uv`:
   ```bash
   uv sync --all-extras
   ```
3. Run marimo:

```bash
# Run as a notebook (development mode)
marimo edit notebooks/GCP.py  # Interactive notebook interface

# Run as an application (production mode)
marimo run notebooks/GCP.py   # Standalone application view
```

Choose the mode that best fits your needs:

- `marimo edit`: Development environment with cell editing
- `marimo run`: Production view for sharing and deployment

## 📚 Project Structure

- `notebooks/`: Interactive implementations of data engineering solutions
- `tests/`: Comprehensive test suite for data pipelines
- `apps/`: Production-ready data applications

## 📊 Sample Data

Sample datasets are included in the `public/` directory for demonstration purposes.

## 🔗 Additional Resources

- [GCP Data Engineering Best Practices](https://cloud.google.com/architecture/data-engineering-best-practices)
- [Modern Data Stack Blog](https://www.datastacktalk.com/)
- [Data Engineering Project Examples](https://github.com/topics/data-engineering)

## 📫 Get in Touch

Feel free to reach out for collaboration or questions about data engineering implementations!
