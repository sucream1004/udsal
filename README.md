# udsal !
- 곧 NYC OPENDATA 사용법 정리해서 올리겠숨다.
- ipython 이라고 인터넷 브라우져(?)에서 python을 동작하고 결과 보여주고 그런게 있더라구요.

# 화이팅~~

# CHEATSHEET

## postgres

### RUN
docker run -it --link kpost:postgres --rm postgres sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

### Importing CSV into postgre
COPY table_name FROM ‘/path_to_csv_file.csv’ WITH FORMAT csv; <br>
COPY table_name FROM '/path_to_csv_file.csv' DELIMITERS ',' CSV; <br>

### Create Table : should be same as imported csv columns
CREATE TABLE table_name ( <br>
id BIGSERIAL NOT NULL PRIMARY KEY, <br>
var1 VARCHAR(50), <br>
var2 VARCHAR(50), <br>
var3 VARCHAR(50), <br>
gender VARCHAR(7) <br>
); <br>

### ogr command to docker
[ogr example](https://morphocode.com/using-ogr2ogr-convert-data-formats-geojson-postgis-esri-geodatabase-shapefiles/) <br>
ogrinfo PG:"host=* port=5432 user='user' password='password' dbname='dbname'" <br>

ogr2ogr -f "PostgreSQL" PG:"dbname=my_database user=postgres" "source_data.json" <br>

ogr2ogr -f 'PostgreSQL' PG:"host=172.17.0.2 port=5432 user=postgres password=kpass dbname=postgres" 'Downloads/nyct2010.geojson'

### host check
\conninfo <br>

### CONCAT
ALTER TABLE table_name <br>
  ADD column_name column_definition; <br>
UPDATE [table]
SET [column] = CONCAT(state, county, tract)

### create new table by statement
CREATE TABLE new_table <br>
  AS (SELECT * FROM old_table);
