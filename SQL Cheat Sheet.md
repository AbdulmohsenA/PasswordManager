# SQL Cheat Sheet

## Create a new Table
`[CREATE TABLE]` will create a table, `[IF NOT EXISTS]` will skip the command if the table already exists

### Example
```sql
CREATE TABLE IF NOT EXISTS <TABLENAME> (
  <COLUMN1_NAME> <DATATYPE>,
  <COLUMN2_NAME> <DATATYPE>
)
```

`ADD` -- Adds a new column to an existing table

`ADD CONSTRAINT` -- Creates a new constraint on an existing table, which is used to specify rules for any data in the table.

`ALTER TABLE` -- Adds, deletes or edits columns in a table. It can also be used to add and delete constraints in a table, as per the above.

`ALTER COLUMN` -- Changes the data type of a table’s column.

`ALL` -- Returns true if all of the subquery values meet the passed condition.

`AND` -- Used to join separate conditions within a WHERE clause.

`ANY` -- Returns true if any of the subquery values meet the given condition.

`AS` -- Renames a table or column with an alias value which only exists for the duration of the query.

ASC -- Used with ORDER BY to return the data in ascending order.

BETWEEN -- Selects values within the given range.

CASE -- Changes query output depending on conditions.

CHECK -- Adds a constraint that limits the value which can be added to a column.

CREATE DATABASE -- Creates a new database.

CREATE TABLE -- Creates a new table. 

DEFAULT -- Sets a default value for a column

DELETE -- Delete data from a table.

DESC -- Used with ORDER BY to return the data in descending order.

DROP COLUMN -- Deletes a column from a table.

DROP DATABASE -- Deletes the entire database.

DROP DEAFULT -- Removes a default value for a column.

DROP TABLE -- Deletes a table from a database.

EXISTS -- Checks for the existence of any record within the subquery, returning true if one or more records are returned.

FROM -- Specifies which table to select or delete data from.

IN --  Used alongside a WHERE clause as a shorthand for multiple OR conditions.

INSERT INTO -- Adds new rows to a table.

IS NULL -- Tests for empty (NULL) values.

IS NOT NULL -- The reverse of NULL. Tests for values that aren’t empty / NULL.

LIKE -- Returns true if the operand value matches a pattern.

NOT -- Returns true if a record DOESN’T meet the condition.
 
OR -- Used alongside WHERE to include data when either condition is true.

ORDER BY -- Used to sort the result data in ascending (default) or descending order through the use of ASC or DESC keywords.

ROWNUM -- Returns results where the row number meets the passed condition.

SELECT -- Used to select data from a database, which is then returned in a results set.

SELECT DISTINCT -- Sames as SELECT, except duplicate values are excluded.

SELECT INTO -- Copies data from one table and inserts it into another.

SELECT TOP -- Allows you to return a set number of records to return from a table.

SET -- Used alongside UPDATE to update existing data in a table.

SOME -- Identical to ANY.

TOP -- Used alongside SELECT to return a set number of records from a table.

TRUNCATE TABLE -- Similar to DROP, but instead of deleting the table and its data, this deletes only the data.

UNION -- Combines the results from 2 or more SELECT statements and returns only distinct values.

UNION ALL -- The same as UNION, but includes duplicate values.

UNIQUE -- This constraint ensures all values in a column are unique.

UPDATE -- Updates existing data in a table.

VALUES -- Used alongside the INSERT INTO keyword to add new values to a table.

WHERE -- Filters results to only include data which meets the given condition.
