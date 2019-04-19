# udsal !
- 곧 NYC OPENDATA 사용법 정리해서 올리겠숨다.
- ipython 이라고 인터넷 브라우져(?)에서 python을 동작하고 결과 보여주고 그런게 있더라구요.

# 화이팅~~

# CHEATSHEET

## postgres
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
ogr2ogr --debug ON -f 'KML' ./areas_desarrollo_indigena_2017_03_07.kml PG:"host=localhost port=5432 dbname=mapserver user=postgres password=" -sql "SELECT * from ( SELECT ST_Intersection(datasrc.geom, polygon) as sharedPolygon, datasrc.* from ST_MakePolygon(ST_GeomFromText('LINESTRING(-69.02160644531251 -20.053351219365318,-69.78515625000001 -20.45789615504684,-69.09851074218751 -20.979392255760608,-69.02160644531251 -20.053351219365318)',4326)) as polygon,datasources.areas_desarrollo_indigena_2017_03_07_15 as datasrc) as sharedPolygon WHERE ST_IsEmpty(sharedPolygon)='false'" <br>

### host check
\conninfo <br>

