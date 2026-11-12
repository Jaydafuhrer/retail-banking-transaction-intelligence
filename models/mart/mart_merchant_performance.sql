
SELECT
    merchant_category_code,
    merchant_name,

    COUNT(*) AS total_transactions,

    COUNT(DISTINCT customer_id) AS unique_customers,

    COUNTIF(status = 'success') AS successful_transactions,

    COUNTIF(status = 'failed') AS failed_transactions,

    COUNTIF(status = 'reversed') AS reversed_transactions,

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
    ) AS fraud_rate

FROM {{ ref('int_transactions') }}

GROUP BY
    merchant_category_code,
    merchant_name
