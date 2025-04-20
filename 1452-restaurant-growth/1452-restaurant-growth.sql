WITH cte AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
),
cte2 AS (
    SELECT 
        visited_on,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM cte
)
SELECT *
FROM cte2
WHERE DATE_ADD(visited_on, INTERVAL -6 DAY) IN (SELECT visited_on FROM cte);
