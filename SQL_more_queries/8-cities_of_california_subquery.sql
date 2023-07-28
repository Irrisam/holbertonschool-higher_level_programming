-- applies subqueries
SELECT id, state FROM cities WHERE cities = (SELECT id, FROM states, WHERE name = 'California')
ORDER BY id;