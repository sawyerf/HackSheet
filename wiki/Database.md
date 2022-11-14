# 🗄️ Database

---
- [Dynamodb](#dynamodb)
- [Influx DB](#influx-db)
- [Mysql](#mysql)
- [SQLite](#sqlite)


# MySql
### Connect to mysql
```bash
mysql -h localhost -u myname -p
```

### Show Info
```
SHOW DATABASES;
use db_name
SHOW TABLES;
```

### Select
```sql
SELECT * FROM table_name
```

# SQLite
### Open
```bash
sqlite3 database.sqlite3
```
or open in vs code

### Show info
```
.databases
.tables
```

### Select
```
SELECT * FROM table_name;
```

# Influx DB

[CVE-2019-20933 Influxdb](https://github.com/LorenzoTullini/InfluxDB-Exploit-CVE-2019-20933)

```
> show databases # to display databases
> show field keys # field keys (like columns in sql)
> show measurements # to display measurements (like tables in sql)
{
  ...
  "results": [
    "values": [
        [
            <strong>"foo"</strong>
        ]
    ]
  ...
}
> select * from "foo" # display all content of measurments (table) 'foo' (keep the doubles quotes)
```

# Dynamodb

See [this page](../wiki/Cloud.md)