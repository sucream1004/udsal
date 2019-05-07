# CHEATSHEET

## docker cp multiple files in unix
for f in data/*txt; do docker cp $f sandbox_web_1:/usr/src/app/data/; done

## postgres
[Tutorial](https://www.saltycrane.com/blog/2019/01/how-run-postgresql-docker-mac-local-development/)

### os command in psql console
\! ls

### RUN
docker run -it --link kpost:postgres --rm postgres sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres' \
docker exec -it kpark_postgres_1 psql -h postgres -U kpark postgres

### Importing CSV into postgre
COPY table_name FROM ‘/path_to_csv_file.csv’ WITH FORMAT csv; <br>
COPY table_name FROM '/path_to_csv_file.csv' DELIMITERS ',' CSV; <br>

### Create Table : should be same as imported csv columns
CREATE TABLE table_name ( \
id BIGSERIAL NOT NULL PRIMARY KEY, \
var1 VARCHAR(50), \
var2 VARCHAR(50), \
var3 VARCHAR(50), \
gender VARCHAR(7) \
);

### ogr command to docker
[ogr example](https://morphocode.com/using-ogr2ogr-convert-data-formats-geojson-postgis-esri-geodatabase-shapefiles/) <br>
ogrinfo PG:"host=* port=5432 user='user' password='password' dbname='dbname'" <br>

ogr2ogr -f "PostgreSQL" PG:"dbname=my_database user=postgres" "source_data.json" <br>

ogr2ogr -f 'PostgreSQL' PG:"host=172.17.0.2 port=5432 user=postgres password=kpass dbname=postgres" 'Downloads/nyct2010.geojson'

### host check
\conninfo <br>

### CONCAT
  ALTER TABLE table_name \
  ADD column_name column_definition; \
  UPDATE [table] \
  SET [column] = CONCAT(state, county, tract)

### create new table by statement
  sql = "SELECT * \
  FROM nyct2010 \
  RIGHT JOIN acs \
  ON nyct2010.cd = acs.cd;"

### Export psql
pg_dump -h 172.17.0.2 -p 5432 -U postgres postgres -N public -T acs > dbexport.pgsql \
\copy (SELECT * FROM persons) to 'C:\tmp\persons_client.csv' with csv

## git
### git pull force
git fetch --all \
git reset --hard origin/master

### Fun!
[Point cloud](https://github.com/heremaps/pptk) # point cloud \
[Transitland animation](https://github.com/transitland/transitland-processing-animation) # transitland animation \
[D3 guide](https://medium.com/@enjalot/the-hitchhikers-guide-to-d3-js-a8552174733a) # d3 \
[Jenks Natural Break](http://qingkaikong.blogspot.com/2018/04/python-jenks-natural-breaks.html) # Jenks Natural Break \
[Street easy analysis](https://observablehq.com/@pstuffa/streeteasy-data-neighborhood-maps) # street easy analysis \
[Postgres, python and JS](https://gis.stackexchange.com/questions/232668/adding-a-postgresql-database-to-a-web-map) # postgres, python and JS (flask or feather) \
[Multi-processing](https://stackoverflow.com/questions/20190668/multiprocessing-a-for-loop) # multi processing python \
[Postgres and JS](https://blog.patricktriest.com/game-of-thrones-map-node-postgres-redis/) # postGIS and nodeJS


### tmp
[ieee short](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8419399) # ieee short \
[ieee long](https://www.researchgate.net/profile/Nhat_Hai_Phan/publication/327106790_Deep_Self-Taught_Learning_for_Detecting_Drug_Abuse_Risk_Behavior_in_Tweets_Invited_to_Computational_Social_Network_2018/links/5b795267a6fdcc5f8b53e849/Deep-Self-Taught-Learning-for-Detecting-Drug-Abuse-Risk-Behavior-in-Tweets-Invited-to-Computational-Social-Network-2018.pdf) # ieee long \
[Crime and DNN](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0176244&type=printable) # crime and dnn

### Reinforcement learning
[Reinforcement Learning with Python](https://towardsdatascience.com/reinforcement-learning-with-python-8ef0242a2fa2)

### POSTGIS, JS and Python (postgres, postgis, javascript, python, flask)
[flask1](http://www.jennifergd.com/post/7/)

### Neural-style theory (computer vision)
[Neural-style](https://towardsdatascience.com/neural-style-transfer-tutorial-part-1-f5cd3315fa7f)
