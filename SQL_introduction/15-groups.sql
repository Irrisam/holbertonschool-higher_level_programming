-- groups and takes out multiple occurences of values and count them
SELECT score , COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score;