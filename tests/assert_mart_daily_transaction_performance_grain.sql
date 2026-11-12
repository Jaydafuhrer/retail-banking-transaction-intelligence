SELECT
    transaction_date,
    channel,
    transaction_type,
    COUNT(*) AS row_count

FROM {{ ref('mart_daily_transaction_performance') }}

GROUP BY
    transaction_date,
    channel,
    transaction_type

HAVING COUNT(*) > 1