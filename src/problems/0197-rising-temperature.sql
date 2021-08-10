WITH cte AS (
    SELECT
        *,
        LAG(recordDate) OVER(ORDER BY recordDate) prevDate,
        LAG(Temperature) OVER(ORDER BY recordDate) prevTemp
    FROM weather)

SELECT id
FROM cte
WHERE Temperature > prevTemp
--     AND DATEDIFF(recordDate, prevDate) = 1
    AND JULIANDAY(recordDate) - JULIANDAY(prevDate) = 1
;