-- 01. Querying data

SELECT 
  Name, 
  Milliseconds/60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- 02. Sorting data

-- NULL 정렬 예시

-- 03. Filtering data

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT 
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000;

-- WHERE
--   10000 <= Bytes 
--   AND Bytes <= 500000

SELECT 
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE 
  Country IN ('Canada', 'Germany', 'France');
-- WHERE
--   Country = 'Canada' 
--   OR Country = 'Germany' 
--   OR Country = 'France';

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';

SELECT 
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a'

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;

-- 04. Grouping data

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT 
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

SELECT
  Composer,
  AVG(Milliseconds/60000) AS avgofmilli
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgofmilli < 10;