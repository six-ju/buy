from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="localhost", user="root", passwd="", db="auction", charset="utf8")
cur = db.cursor()
@app.route('/')
def home():
    return render_template('upload_page.html')

# db 보내기
@app.route("/upload", methods=["POST"])
def upload():
    date = request.form['date_give']
    title = request.form['title_give']
    category = request.form['category_give']
    start_price = request.form['start_price_give']
    content = request.form['content_give']
    upload_files = request.form['files_give']

    sql = """
            INSERT INTO content VALUES(
            null,   
            '""" + str(date) + """',           
            '""" + str(title) + """',
            '""" + str(category) + """',
            '""" + str(start_price) + """',
            '""" + str(content) + """',
                        1 ,
                '"""+str(upload_files)+"""'
          
       );"""
    cur.execute(sql)
    db.commit()
    return jsonify({'msg': '게시됨!!'})



if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
