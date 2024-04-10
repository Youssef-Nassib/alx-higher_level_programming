-- Lists all records of the table second_table having a namse values in my MySQL server.
-- Records are ordered by descending scores.
SELECT `score`, `name`
FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
