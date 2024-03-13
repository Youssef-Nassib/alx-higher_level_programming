-- Lists the number of records with the same score in table second_table in my MySQL server.
-- Records are ordered by descending cont.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
