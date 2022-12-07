import pymysql

# 2. 접속하기
db = pymysql.connect(host="localhost", user="root", passwd="alex0713", db="auction", charset="utf8")
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
# for index in range(10):
#     id = 905 + index + 1
sql = """
insert into
 upload( id,title , category, won,date, comment,file)
 value('1','안녕못해','2',3,221206,'1','');"""



# 5. SQL 구문 실행하기
cur.execute(sql)

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
# db.close()
#########################################################
# @app.route('/')
# def index():
#     return render_template('upload_page.html')
# if __name__ == '__main__':
#     app.run(host='127.0.0.1',port='5000',debug=True)
