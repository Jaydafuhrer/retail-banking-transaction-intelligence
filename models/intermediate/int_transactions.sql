
SELECT
    stg.*,

    DATE(stg.timestamp, 'Africa/Lagos') AS transaction_date,

    EXTRACT(
        HOUR FROM DATETIME(stg.timestamp, 'Africa/Lagos')
    ) AS transaction_hour,

    stg.balance_after_ngn - stg.balance_before_ngn
        AS balance_change_ngn

FROM {{ ref('stg_transactions') }} AS stg
