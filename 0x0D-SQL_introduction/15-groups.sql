-- shows the number of records counting the score and ordering desc
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
