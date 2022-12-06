from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text
from flask      import Flask, request, jsonify, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text
import pymysql
app = Flask (__name__)
# 2. 접속하기
db = pymysql.connect(host="localhost", user="root", passwd="alex0713", db="auction", charset="utf8")
print(db)
# 3. 커서 가져오기
cur = db.cursor()
# 4. SQL 구문 만들기 (CRUD SQL 구문 등)
# sql = """
#     CREATE TABLE upload (
#         id int NOT NULL,
#         TITLE CHAR(200) NOT NULL,
#         category char(50)NOT NULL,
#         won INT,
#         DATE date NOT NULL,
#         comment VARCHAR(200) NOT NULL,
#         PRIMARY KEY(id , date)
#     );
# """
sql = """
    insert into
     upload( id,title , category, won,date, comment,file)
     value(%s,%s,%s,%s,%s,%s,%s);"""
with db:
    with db.cursor() as cur:
        cur.execute(sql,('10000','코딩','it','50000',221206,'파이썬',''))
        db.commit()


# 5. SQL 구문 실행하기
# cur.execute(sql)

# 6. DB에 Complete 하기
# db.commit()

# 7. DB 연결 닫기
# db.close()

# 8. 데이터 검색(조회)
# sql = "SELECT * FROM upload"
# cur.execute(sql)
#
# result = cur.fetchall()
# for record in result:
#     print(record)