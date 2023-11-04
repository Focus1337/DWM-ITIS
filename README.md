### 3 HW - hive

add to `/etc/hosts` (or `C:\Windows\System32\drivers\etc\hosts` for windows)

```
#hadoop
127.0.0.1 namenode
127.0.0.1 datanode
```

Namenode:

```docker cp dataset namenode:\dataset\```

```docker exec -it namenode bash```

```hdfs dfs -put /dataset/dataset.csv /hive/```

Hive:

```docker exec -it hive-server bash```

Main table
```sql
create database if not exists testdb;
use testdb;
CREATE TABLE properties (
    Transaction_unique_identifier STRING,
    price STRING,
    Date_of_Transfer DATE,
    postcode STRING,
    Property_Type STRING,
    Old_New STRING,
    Duration STRING,
    PAON STRING,
    SAON STRING,
    Street STRING,
    Locality STRING,
    Town_City STRING,
    District STRING,
    County STRING,
    PPDCategory_Type STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/hive';
```

Table with removed ""
```sql
CREATE TABLE properties_parsed AS
SELECT
regexp_replace(price, '"', '') AS price,
regexp_replace(postcode, '"', '') AS postcode
FROM properties;
```

Table with casted int
```sql
CREATE TABLE properties_parsed_again AS
SELECT
CAST(price AS INT) AS price_int,
postcode
FROM properties_parsed;
```

Head script
```sql
select * from
(
SELECT *,ROW_NUMBER() over () as rowid FROM properties_parsed_again
)t
where rowid > 0 and rowid <=20;
```

Reducer script
```sql
SELECT postcode, AVG(price_int) AS average_price
FROM properties_parsed_again
GROUP BY postcode;
```
