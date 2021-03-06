SELECT id,
    SUM(CASE month WHEN 'Jan' THEN revenue END) as Jan_Revenue,
    SUM(CASE month WHEN 'Feb' THEN revenue END) as Feb_Revenue,
    SUM(CASE month WHEN 'Mar' THEN revenue END) as Mar_Revenue,
    SUM(CASE month WHEN 'Apr' THEN revenue END) as Apr_Revenue,
    SUM(CASE month WHEN 'May' THEN revenue END) as May_Revenue,
    SUM(CASE month WHEN 'Jun' THEN revenue END) as Jun_Revenue,
    SUM(CASE month WHEN 'Jul' THEN revenue END) as Jul_Revenue,
    SUM(CASE month WHEN 'Aug' THEN revenue END) as Aug_Revenue,
    SUM(CASE month WHEN 'Sep' THEN revenue END) as Sep_Revenue,
    SUM(CASE month WHEN 'Oct' THEN revenue END) as Oct_Revenue,
    SUM(CASE month WHEN 'Nov' THEN revenue END) as Nov_Revenue,
    SUM(CASE month WHEN 'Dec' THEN revenue END) as Dec_Revenue
FROM department
GROUP BY id
;