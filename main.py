
import logging
from pathlib import Path

from ingestion.pipeline import run_pipeline


Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/ingestion.log"),
        logging.StreamHandler()
    ]
)

file_path = "/Users/owner/Downloads/nigerian_retail_transactions_full.parquet"

run_pipeline(file_path)

