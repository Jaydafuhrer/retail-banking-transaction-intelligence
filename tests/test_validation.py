
import pytest
import pyarrow as pa

from ingestion.validate import validate_batch


def test_valid_batch():

    batch = pa.RecordBatch.from_pydict({
        "transaction_id": ["TX001", "TX002"],
        "account_id": ["ACC001", "ACC002"],
        "customer_id": ["CUS001", "CUS002"],
        "timestamp": pa.array(
            ["2026-01-01", "2026-01-02"]
        ).cast(pa.timestamp("ns")),
        "amount_ngn": [5000.0, 3000.0],
        "balance_before_ngn": [10000.0, 8000.0],
        "balance_after_ngn": [5000.0, 5000.0],
        "transaction_type": ["debit", "credit"],
        "channel": ["mobile", "pos"],
        "merchant_category_code": ["5411", "5812"],
        "merchant_name": ["Shop A", "Shop B"],
        "location_lga": ["Ikeja", "Surulere"],
        "location_state": ["Lagos", "Lagos"],
        "device_id": ["DEV001", "DEV002"],
        "status": ["successful", "successful"],
        "fraud_flag": [False, False]
    })

    assert validate_batch(batch) is True


def test_invalid_column_names():

    batch = pa.RecordBatch.from_pydict({
        "wrong_transaction_id": ["TX001", "TX002"],
        "account_id": ["ACC001", "ACC002"],
        "customer_id": ["CUS001", "CUS002"],
        "timestamp": pa.array(
            ["2026-01-01", "2026-01-02"]
        ).cast(pa.timestamp("ns")),
        "amount_ngn": [5000.0, 3000.0],
        "balance_before_ngn": [10000.0, 8000.0],
        "balance_after_ngn": [5000.0, 5000.0],
        "transaction_type": ["debit", "credit"],
        "channel": ["mobile", "pos"],
        "merchant_category_code": ["5411", "5812"],
        "merchant_name": ["Shop A", "Shop B"],
        "location_lga": ["Ikeja", "Surulere"],
        "location_state": ["Lagos", "Lagos"],
        "device_id": ["DEV001", "DEV002"],
        "status": ["successful", "successful"],
        "fraud_flag": [False, False]
    })

    with pytest.raises(ValueError):
        validate_batch(batch)


def test_invalid_data_types():

    batch = pa.RecordBatch.from_pydict({
        "transaction_id": ["TX001", "TX002"],
        "account_id": ["ACC001", "ACC002"],
        "customer_id": ["CUS001", "CUS002"],
        "timestamp": pa.array(
            ["2026-01-01", "2026-01-02"]
        ).cast(pa.timestamp("ns")),
        "amount_ngn": [5000, 3000],
        "balance_before_ngn": [10000.0, 8000.0],
        "balance_after_ngn": [5000.0, 5000.0],
        "transaction_type": ["debit", "credit"],
        "channel": ["mobile", "pos"],
        "merchant_category_code": ["5411", "5812"],
        "merchant_name": ["Shop A", "Shop B"],
        "location_lga": ["Ikeja", "Surulere"],
        "location_state": ["Lagos", "Lagos"],
        "device_id": ["DEV001", "DEV002"],
        "status": ["successful", "successful"],
        "fraud_flag": [False, False]
    })

    with pytest.raises(ValueError):
        validate_batch(batch)


def test_required_fields_reject_nulls():

    batch = pa.RecordBatch.from_pydict({
        "transaction_id": [None, "TX002"],
        "account_id": ["ACC001", "ACC002"],
        "customer_id": ["CUS001", "CUS002"],
        "timestamp": pa.array(
            ["2026-01-01", "2026-01-02"]
        ).cast(pa.timestamp("ns")),
        "amount_ngn": [5000.0, 3000.0],
        "balance_before_ngn": [10000.0, 8000.0],
        "balance_after_ngn": [5000.0, 5000.0],
        "transaction_type": ["debit", "credit"],
        "channel": ["mobile", "pos"],
        "merchant_category_code": ["5411", "5812"],
        "merchant_name": ["Shop A", "Shop B"],
        "location_lga": ["Ikeja", "Surulere"],
        "location_state": ["Lagos", "Lagos"],
        "device_id": ["DEV001", "DEV002"],
        "status": ["successful", "successful"],
        "fraud_flag": [False, False]
    })

    with pytest.raises(ValueError):
        validate_batch(batch)
