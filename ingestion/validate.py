
import pyarrow as pa


EXPECTED_COLUMNS = [
    "transaction_id",
    "account_id",
    "customer_id",
    "timestamp",
    "amount_ngn",
    "balance_before_ngn",
    "balance_after_ngn",
    "transaction_type",
    "channel",
    "merchant_category_code",
    "merchant_name",
    "location_lga",
    "location_state",
    "device_id",
    "status",
    "fraud_flag",
]


EXPECTED_TYPES = [
    pa.string(),
    pa.string(),
    pa.string(),
    pa.timestamp("ns"),
    pa.float64(),
    pa.float64(),
    pa.float64(),
    pa.string(),
    pa.string(),
    pa.string(),
    pa.string(),
    pa.string(),
    pa.string(),
    pa.string(),
    pa.string(),
    pa.bool_(),
]


REQUIRED_FIELDS = [
    "transaction_id",
    "account_id",
    "customer_id",
    "timestamp",
]


def validate_batch(batch):
    actual_columns = batch.schema.names
    actual_types = batch.schema.types

    # Check column names
    if actual_columns != EXPECTED_COLUMNS:
        raise ValueError(
            f"Column mismatch. Expected: {EXPECTED_COLUMNS}. "
            f"Received: {actual_columns}"
        )

    # Check data types
    if actual_types != EXPECTED_TYPES:
        raise ValueError(
            f"Data type mismatch. Expected: {EXPECTED_TYPES}. "
            f"Received: {actual_types}"
        )

    # Check for empty batches
    if batch.num_rows == 0:
        raise ValueError("Empty batch received.")

    # Check required fields for NULL values
    for column_name in REQUIRED_FIELDS:
        column_index = batch.schema.get_field_index(column_name)

        null_count = batch.column(column_index).null_count

        if null_count > 0:
            raise ValueError(
                f"Null values found in {column_name}: {null_count}"
            )

    return True
