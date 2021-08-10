WITH cte AS (
    SELECT
        *,
        DENSE_RANK() OVER(ORDER BY Salary DESC) rank_desc
    FROM employee)

SELECT MAX(salary) SecondHighestSalary
FROM cte
WHERE rank_desc = 2
;