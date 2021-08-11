SELECT
    d.Name Department,
    e1.Name Employee,
    e1.Salary
FROM
    employee e1
JOIN
    (SELECT
        DepartmentId,
        MAX(Salary) max_salary
     FROM employee
     GROUP BY DepartmentID) e2
ON e1.DepartmentId = e2.DepartmentId
JOIN
    department d
ON e1.DepartmentId = d.Id
WHERE e1.Salary = e2.max_salary
;

-- WITH e AS (
--     SELECT
--         Name,
--         Salary,
--         DepartmentId,
--         RANK() OVER(
--             PARTITION BY DepartmentId
--             ORDER BY Salary DESC) salary_rank
--     FROM employee)

-- SELECT
--     d.Name Department,
--     e.Name Employee,
--     e.Salary
-- FROM e
-- JOIN department d
-- ON e.DepartmentId = d.Id
-- WHERE e.salary_rank = 1
-- ;