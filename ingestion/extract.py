
import duckdb

from ingestion.validate import validate_batch


def extract_batches(file_path, batch_size=100_000):
    con = duckdb.connect()

    try:
        query = """
            SELECT *
            FROM read_parquet(?)
        """

        reader = con.execute(
            query, [file_path]
        ).fetch_record_batch(rows_per_batch=batch_size)

        for batch in reader:
            validate_batch(batch)
            yield batch

    finally:
        con.close()
