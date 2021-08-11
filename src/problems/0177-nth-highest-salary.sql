SELECT DISTINCT Salary `getNthHighestSalary({N})`
FROM (
  SELECT
    Salary,
    DENSE_RANK() OVER(ORDER BY Salary DESC) salary_rank
  FROM employee) e
WHERE salary_rank = {N}
;

-- NOFIX: SQLite does not have a stored function language.
-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--   RETURN (
--       SELECT DISTINCT Salary
--       FROM (
--           SELECT
--             Salary,
--             DENSE_RANK() OVER(ORDER BY Salary DESC) salary_rank
--           FROM employee) e
--       WHERE salary_rank = N

-- --       SELECT DISTINCT Salary
-- --       FROM employee e1
-- --       WHERE N - 1 = (
-- --           SELECT COUNT(DISTINCT Salary)
-- --           FROM employee e2
-- --           WHERE e1.Salary < e2.Salary)
--   );
-- END

-- SELECT getNthHighestSalary(N)
-- FROM employee
-- ;