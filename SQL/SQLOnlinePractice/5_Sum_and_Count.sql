-- Illustration
-- COUNT, SUM, ORDER BY
-- 1. The total population and GDP of Europe.
SELECT SUM(population), SUM(gdp) FROM bbc WHERE region = 'Europe'

-- 2. What are the regions?
SELECT DISTINCT region FROM bbc

-- 3. Show the name and population for each country with a population of more than 100000000.
-- Show countries in descending order of population.
SELECT name, population
  FROM bbc
  WHERE population > 100000000
  ORDER BY population DESC

-- GROUPY BY
-- By including a GROUP BY clause functions such as SUM and COUNT are applied to groups of items sharing values.
-- When you specify GROUP BY continent the result is that you get only one row for each different value of continent.
-- All the other columns must be "aggregated" by one of SUM, COUNT ...
-- If a ORDER BY clause is included we can refer to columns by their position.
-- 1. For each continent show the number of countries:
SELECT continent, COUNT(name)
  FROM world
 GROUP BY continent
-- 2. For each continent show the total population:
SELECT continent, SUM(population)
  FROM world
 GROUP BY continent
-- 3. For each relevant continent show the number of countries that has a population of at least 200000000.
SELECT continent, COUNT(name)
  FROM world
 WHERE population>200000000
 GROUP BY continent

-- HAVING
-- The HAVING clause allows use to filter the groups which are displayed.
-- The WHERE clause filters rows before the aggregation, the HAVING clause filters after the aggregation.
-- 4. Show the total population of those continents with a total population of at least half a billion.
SELECT continent, SUM(population)
  FROM world
 GROUP BY continent
HAVING SUM(population)>500000000

-- Questions
-- 1. Show the total population of the world.
SELECT SUM(population)
FROM world

-- 2. List all the continents - just once each.
SELECT DISTINCT continent from world

-- 3. Give the total GDP of Africa
SELECT SUM(gdp) FROM world WHERE continent = 'Africa'

-- 4. How many countries have an area of at least 1000000
SELECT COUNT(name) FROM world WHERE area >= 1000000

-- 5. What is the total population of ('Estonia', 'Latvia', 'Lithuania')
SELECT SUM(population) FROM world WHERE name IN ('Estonia', 'Latvia', 'Lithuania')

-- 6. For each continent show the continent and number of countries.
SELECT continent, COUNT(name) FROM world GROUP BY continent

-- 7. For each continent show the continent and number of countries with populations of at least 10 million.
SELECT continent, COUNT(name) FROM world WHERE population>=10000000 GROUP BY continent

-- 8. List the continents that have a total population of at least 100 million.
SELECT continent FROM world GROUP BY continent HAVING SUM(population) > 100000000