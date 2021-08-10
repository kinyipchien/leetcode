SELECT c.Name Customers
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE c.Id = o.CustomerId)
;