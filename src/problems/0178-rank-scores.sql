SELECT
    score,
    DENSE_RANK() OVER(ORDER BY Score DESC) `Rank`
FROM scores
;