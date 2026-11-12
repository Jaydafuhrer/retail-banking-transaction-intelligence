# Retail Banking Transaction Intelligence Platform

## Project Overview

An end-to-end data engineering and analytics engineering project built around a synthetic Nigerian retail banking transactions dataset.

The project demonstrates how large-scale transaction data can be extracted, validated, loaded into a cloud data warehouse, transformed into analytical models, and tested for data quality.

The platform uses Python, DuckDB, PyArrow, Google BigQuery and dbt to create structured datasets for investigating transaction performance, customer activity, merchant activity, geographic patterns and potential fraud indicators.

## Architecture

**Data Source → Python Ingestion → BigQuery → dbt Transformations → Analytical Data Marts**

### Technology Stack

| Technology | Purpose |
|---|---|
| Python | Pipeline implementation |
| DuckDB | Batch extraction from Parquet |
| PyArrow | Batch processing and schema validation |
| Google BigQuery | Cloud data warehouse |
| SQL | Data transformation and analysis |
| dbt | Data modelling, testing and documentation |
| pytest | Python validation tests |
| Git & GitHub | Version control |

## Data Source

**Dataset:** [Nigerian Banking Retail Transactions](https://huggingface.co/datasets/electricsheepafrica/nigerian-banking-retail-transactions)

The dataset contains approximately 5 million synthetic banking transactions across 2023 and 2024.

It includes transaction identifiers, customer and account identifiers, timestamps, transaction amounts, balances, transaction types, channels, merchant information, geographic information, transaction statuses and fraud indicators.

**Important:** The dataset is synthetic. Findings describe patterns within the supplied dataset and should not be interpreted as evidence of actual Nigerian banking behaviour or fraud prevalence.

## Data Engineering Implementation

### 1. Python Ingestion Pipeline

Implemented a batch-based ingestion pipeline to process the Parquet dataset and load records into BigQuery.

Key components:

- **Extraction:** DuckDB and PyArrow are used to process the source dataset in batches of 100,000 records.
- **Validation:** PyArrow schema checks verify expected columns, data types, required fields and non-null constraints.
- **Loading:** Validated batches are loaded into BigQuery.
- **Logging:** Pipeline execution, batch progress and errors are recorded in log files.

The ingestion process successfully loaded approximately 5 million records across 50 batches.

### 2. BigQuery Data Warehouse

The raw transaction data is stored in BigQuery and serves as the source for downstream transformations.

### 3. dbt Transformation Layer

The dbt project follows a layered modelling approach.

**Staging**

`stg_transactions`

- Standardises text fields.
- Normalises transaction types, channels and statuses.
- Converts empty merchant names to NULL.
- Selects the required source fields.

**Intermediate**

`int_transactions`

- Derives transaction dates and hours using the Africa/Lagos timezone.
- Calculates transaction balance changes.
- Prepares reusable transaction-level data for downstream models.

**Analytical Data Marts**

| Model | Purpose |
|---|---|
| `mart_daily_transaction_performance` | Daily transaction volumes, values, outcomes and fraud indicators by channel and transaction type |
| `mart_fraud_analysis` | Fraud indicators and rates across transaction dimensions |
| `mart_customer_activity` | Customer transaction activity, engagement and transaction outcomes |
| `mart_geographic_performance` | Transaction performance across states and local government areas |
| `mart_merchant_performance` | Transaction performance across merchant categories and merchant names |

## Data Quality

Data quality checks were implemented at both the Python ingestion and dbt transformation layers.

Python validation includes:

- Expected column validation.
- Data type validation.
- Required-field null checks.
- Batch validation.

dbt tests include:

- Uniqueness checks.
- Not-null checks.
- Model-specific data quality checks.
- A custom grain test for daily transaction performance.

The dbt models and associated tests were successfully executed during development.

## Analytical Areas

The resulting data marts support investigation of:

- Transaction volumes and values across banking channels.
- Successful, failed, pending and reversed transactions.
- Customer transaction activity and behaviour.
- Geographic transaction distribution.
- Merchant and merchant-category performance.
- Fraud-flagged transaction patterns.

## Important Data Limitations

- The dataset is synthetic and does not represent verified real-world banking activity.
- Fraud flags are dataset-provided indicators, not independently confirmed fraud cases.
- Fraud-flagged transaction values should not be interpreted as confirmed financial losses.
- Merchant names are missing for a substantial proportion of transactions, particularly outside merchant-oriented channels.
- Observed patterns should be interpreted within the dataset's generation assumptions.

## Repository Structure

```text
retail-banking-transaction-intelligence/
│
├── ingestion/
│   ├── extract.py
│   ├── load.py
│   ├── pipeline.py
│   ├── validate.py
│   └── init.py
│
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── mart/
│
├── tests/
│   ├── test_validation.py
│   └── assert_mart_daily_transaction_performance_grain.sql
│
├── analyses/
├── macros/
├── seeds/
├── snapshots/
│
├── main.py
├── dbt_project.yml
├── requirements.txt
└── README.md
```

## Running the Python Pipeline

Install the dependencies:

```bash
pip install -r requirements.txt
```

Ensure that the source Parquet file is available at the path configured in `main.py`, and that Google Cloud authentication is configured.

Run:

```bash
python main.py
```

## dbt Execution

The dbt project was developed and executed using dbt Cloud.

The models can be built and tested through the configured dbt environment using:

```bash
dbt build
```

## Project Outcome

The project demonstrates a complete data engineering workflow covering large-scale batch ingestion, schema validation, cloud data warehousing, layered SQL transformations, analytical data modelling and automated data quality testing within dbt.
