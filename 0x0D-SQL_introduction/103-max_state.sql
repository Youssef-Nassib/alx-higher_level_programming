-- Displays the max temperatures of each states, ordered by a state name.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures` GROUP BY `state` ORDER BY `state`;
