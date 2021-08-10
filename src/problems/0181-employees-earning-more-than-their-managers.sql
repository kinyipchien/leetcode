SELECT e1.Name Employee
FROM employee e1, employee e2
WHERE e1.ManagerId IS NOT NULL
    AND e1.ManagerId = e2.Id
    AND e1.Salary > e2.Salary
;