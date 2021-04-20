# MySQL

## Data types
```sql
INT or INTEGER
REAL or FLOAT
DECIMAL(n,d) or NUMERIC(n,d)
CHAR(n) or BIT(b)
VARCHAR(n) or BIT VARYING(n)
-- n and b are length
TIME: 'hh:mm:ss[.ss…]'
Date: ’yyyy-mm-dd’ 
NOT NULL
DEFAULT  
```
## Aggregators
```sql
SUM							-- return sum of all non null values in column
AVG							-- return average value in column
MIN							-- return smallest value in column
MAX							-- return largest value in column
COUNT (includes duplicates)-- return number of values in a column, counts NULL too
COUNT(*) -- Counts the total number of rows (including NULLs) in a column
COUNT (DISTINCT name) (excludes duplicates)
GROUP BY <ASC, DESC>
ORDER BY <ASC, DESC>
HAVING
```