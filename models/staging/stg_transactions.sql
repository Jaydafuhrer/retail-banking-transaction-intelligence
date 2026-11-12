{{ config(
    materialized='table'
) }}
SELECT
    transaction_id,
    account_id,
    customer_id,
    timestamp,
    amount_ngn,
    balance_before_ngn,
    balance_after_ngn,
    LOWER(TRIM(transaction_type)) AS transaction_type,
    LOWER(TRIM(channel)) AS channel,
    merchant_category_code,
    NULLIF(TRIM(merchant_name), '') AS merchant_name,
    TRIM(location_lga) AS location_lga,
    TRIM(location_state) AS location_state,
    device_id,
    LOWER(TRIM(status)) AS status,
    fraud_flag

FROM {{ source('banking_raw', 'transactions_raw') }}
