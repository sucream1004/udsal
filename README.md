# udsal !
- 곧 NYC OPENDATA 사용법 정리해서 올리겠숨다.
- ipython 이라고 인터넷 브라우져(?)에서 python을 동작하고 결과 보여주고 그런게 있더라구요.

# 화이팅~~

# CHEATSHEET

## postgres
### Importing CSV into postgre
COPY table_name FROM ‘/path_to_csv_file.csv’ WITH FORMAT csv;
COPY table_name FROM '/path_to_csv_file.csv' DELIMITERS ',' CSV;

### Create Table : should be same as imported csv columns
CREATE TABLE table_name (
id BIGSERIAL NOT NULL PRIMARY KEY,
var1 VARCHAR(50),
var2 VARCHAR(50),
var3 VARCHAR(50),
gender VARCHAR(7)
);
