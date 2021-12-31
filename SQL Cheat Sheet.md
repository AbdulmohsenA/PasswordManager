# SQL Cheat Sheet

## Create a new Table
`CREATE TABLE` will create a table, `IF NOT EXISTS` will skip the command if the table already exists

### Example

```sql
CREATE TABLE IF NOT EXISTS <TABLENAME> (
  <COLUMN1_NAME> <DATATYPE>,
  <COLUMN2_NAME> <DATATYPE>
)
```

