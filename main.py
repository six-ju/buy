from flask import Flask, render_template, request, jsonify
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="localhost", user="root", passwd="alex0713", db="auction", charset="utf8")
cur = db.cursor()
@app.route('/')
def home():
    return render_template('upload_page.html')


@app.route("/upload", methods=["POST"])
def upload_button():
    date = request.form['date_give']
    upload_id = request.form['upload_id_give']
    title = request.form['title_give']
    category = request.form['category_give']
    start_price = request.form['start_price_give']
    content = request.form['content_give']

    sql = """
            INSERT INTO upload VALUES(
            '""" + str(date) + """',
            '""" + str(upload_id) + """',
            '""" + str(title) + """',
            '""" + str(category) + """',
            '""" + str(start_price) + """',
       '""" + str(content) + """');"""
    cur.execute(sql)
    db.commit()
    return jsonify({'msg': '게시됨!!'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
