
SELECT
    customer_id,

    COUNT(*) AS total_transactions,

    COUNT(DISTINCT transaction_date) AS active_days,

    MIN(transaction_date) AS first_transaction_date,

    MAX(transaction_date) AS last_transaction_date,

    COUNTIF(status = 'success') AS successful_transactions,

    COUNTIF(status = 'failed') AS failed_transactions,

    COUNTIF(status = 'reversed') AS reversed_transactions,

    COUNTIF(status = 'pending') AS pending_transactions,

    SUM(amount_ngn) AS total_attempted_value_ngn,

    SUM(
        CASE
            WHEN status = 'success' THEN amount_ngn
            ELSE 0
        END
    ) AS successful_transaction_value_ngn,

    COUNTIF(transaction_type = 'debit') AS debit_transactions,

    COUNTIF(transaction_type = 'credit') AS credit_transactions,

    SUM(
        CASE
            WHEN transaction_type = 'debit'
                AND status = 'success'
            THEN amount_ngn
            ELSE 0
        END
    ) AS successful_debit_value_ngn,

    SUM(
        CASE
            WHEN transaction_type = 'credit'
                AND status = 'success'
            THEN amount_ngn
            ELSE 0
        END
    ) AS successful_credit_value_ngn,

    COUNT(DISTINCT channel) AS channels_used,

    COUNTIF(fraud_flag = TRUE) AS fraudulent_transactions,

    SAFE_DIVIDE(
        COUNTIF(fraud_flag = TRUE),
        COUNT(*)
    ) AS fraud_rate

FROM {{ ref('int_transactions') }}

GROUP BY customer_id
