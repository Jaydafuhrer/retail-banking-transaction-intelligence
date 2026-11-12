
import logging

from google.cloud import bigquery

from ingestion.extract import extract_batches
from ingestion.load import load_batch, create_bigquery_client


logger = logging.getLogger(__name__)


def run_pipeline(file_path):

    client = create_bigquery_client()

    batch_count = 0
    total_rows_loaded = 0

    try:
        for batch in extract_batches(file_path):

            if batch_count == 0:
                write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
            else:
                write_disposition = bigquery.WriteDisposition.WRITE_APPEND

            rows_loaded = load_batch(
                batch,
                client,
                write_disposition
            )

            batch_count += 1
            total_rows_loaded += rows_loaded

            logger.info(
                f"Batch {batch_count} loaded successfully: "
                f"{rows_loaded:,} rows"
            )

        logger.info("Ingestion completed.")
        logger.info(f"Total batches: {batch_count}")
        logger.info(f"Total rows loaded: {total_rows_loaded:,}")

    except Exception as error:
        logger.exception(
            f"Ingestion failed while processing batch "
            f"{batch_count + 1}: {error}"
        )
        raise
