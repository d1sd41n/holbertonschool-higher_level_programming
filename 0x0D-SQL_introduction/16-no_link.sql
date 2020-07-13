-- shows all score that is not null and all of this is ordered desc
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
