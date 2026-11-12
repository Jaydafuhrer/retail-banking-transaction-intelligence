
SELECT
    location_state,
    location_lga,

    COUNT(*) AS total_transactions,

    COUNT(DISTINCT customer_id) AS unique_customers,

    COUNTIF(status = 'success') AS successful_transactions,

    COUNTIF(status = 'failed') AS failed_transactions,

    SUM(amount_ngn) AS total_attempted_value_ngn,

    SUM(
        CASE
            WHEN status = 'success' THEN amount_ngn
            ELSE 0
        END
    ) AS successful_transaction_value_ngn,

    COUNTIF(fraud_flag = TRUE) AS fraudulent_transactions,

    SAFE_DIVIDE(
        COUNTIF(fraud_flag = TRUE),
        COUNT(*)
    ) AS fraud_rate,

    COUNT(DISTINCT channel) AS channels_used

FROM {{ ref('int_transactions') }}

GROUP BY
    location_state,
    location_lga
