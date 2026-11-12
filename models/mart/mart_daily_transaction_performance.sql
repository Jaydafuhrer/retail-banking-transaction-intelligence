
SELECT
    transaction_date,
    channel,
    transaction_type,

    COUNT(*) AS total_transactions,

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

    AVG(
        CASE
            WHEN status = 'success' THEN amount_ngn
        END
    ) AS average_successful_transaction_value_ngn,

    COUNTIF(fraud_flag = TRUE) AS fraudulent_transactions

FROM {{ ref('int_transactions') }}

GROUP BY
    transaction_date,
    channel,
    transaction_type
