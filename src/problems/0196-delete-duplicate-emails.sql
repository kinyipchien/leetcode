DELETE FROM person
WHERE Id NOT IN (
    SELECT Id
    FROM (
        SELECT MIN(Id) Id
        FROM person
        GROUP BY Email
    ) temp
)
;