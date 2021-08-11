WITH cte AS (
    SELECT
        Num,
        LAG(Num) OVER(ORDER BY id) prev_num,
        LEAD(Num) OVER(ORDER BY id) next_num
    FROM logs)

SELECT DISTINCT Num ConsecutiveNums
FROM cte
WHERE prev_num = Num AND Num = next_num
;

-- SELECT DISTINCT Num ConsecutiveNums
-- FROM (
--     SELECT
--         Num,
--         SUM(flag) OVER (ORDER BY id) rolling_count
--     FROM (
--         SELECT
--             *,
--             CASE
--                 WHEN LAG(Num) OVER(ORDER BY id) - Num = 0
--                 THEN 0
--                 ELSE 1
--             END flag
--         FROM logs
--     ) a
-- ) b
-- GROUP BY Num, rolling_count
-- HAVING COUNT(*) >= 3
-- ;