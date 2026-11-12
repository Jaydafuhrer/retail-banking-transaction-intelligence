
SELECT
    transaction_date,
    channel,
    transaction_type,
    location_state,
    merchant_category_code,

    COUNT(*) AS total_transactions,

    COUNTIF(fraud_flag = TRUE) AS fraudulent_transactions,

    SAFE_DIVIDE(
        COUNTIF(fraud_flag = TRUE),
        COUNT(*)
    ) AS fraud_rate,

    SUM(
        CASE
            WHEN fraud_flag = TRUE THEN amount_ngn
            ELSE 0
        END
    ) AS fraud_flagged_transaction_value_ngn,

    COUNTIF(
        fraud_flag = TRUE
        AND status = 'success'
    ) AS successful_fraudulent_transactions

FROM {{ ref('int_transactions') }}

GROUP BY
    transaction_date,
    channel,
    transaction_type,
    location_state,
    merchant_category_code
