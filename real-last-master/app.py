from flask import Flask, session, render_template, redirect, request, url_for, jsonify, escape
import pymysql, hashlib, ctypes
from time import sleep
app = Flask (__name__)
app.secret_key = 'ABCDEF'
db = pymysql.connect(host="비밀", user="auction", passwd="비밀", db="auction", charset="utf8")
cur = db.cursor()
#템플릿 이동

@app.route('/my_page_html')
def mypage_html():
    if "userId" in session:
        return render_template('/my_page/my_page.html')
    else:
        return jsonify('who are you')

@app.route('/upload_page')
def upload_page_html():
        return render_template('/upload_page/upload_page.html')

@app.route('/modal_html')
def modal_html():
        return render_template('/main/test.html')

@app.route('/user_info_edit_html')
def user_info_edit_html():
    return render_template('/my_page/user_info.html')

@app.route('/edit_html')
def edit_html():
    return render_template('/my_page/edit.html')

# 로그인
@app.route('/', methods=['GET', 'POST'])
def login_proc():
    if request.method == 'POST':
        userId = request.form['idIn']
        userPw = request.form['pwIn']
        if len(userId) == 0 or len(userPw) == 0:
            sleep(0)
            MS_SYSTEMMODAL = 0x00001000
            ctypes.windll.user32.MessageBoxW(0, "아이디 및 패스워드를 입력해주세요.", "알림", MS_SYSTEMMODAL)
            return redirect(url_for('login_proc'))
        else:
            sql = "SELECT * FROM user"
            cur.execute(sql)
            rows = cur.fetchall()
            for i in range(len(rows)):
                if userId == rows[i][1] and hashlib.sha256(userPw.encode()).hexdigest() == rows[i][3]:
                    session['userId'] = userId
                    return redirect(url_for('main'))
            sleep(0)
            MB_SYSTEMMODAL = 0x00001000
            ctypes.windll.user32.MessageBoxW(0, "아이디 및 비밀번호가 틀렸습니다.", "알림", MB_SYSTEMMODAL)
            print(userId)
            return redirect(url_for('login_proc'))
    return render_template('/login_page/login_page.html')

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('userId', None)
    return redirect(url_for('login_proc'))

# 회원가입
@app.route('/register_page.html/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        result = request.form
        myid = request.form['Id']
        name = request.form['Name']
        pw = request.form['psw']
        pwr = request.form['psw-repeat']
        sql = "SELECT user_id FROM user"
        cur.execute(sql)
        id_data = cur.fetchall()

        for i in range(len(id_data)):
            if myid == id_data[i]:
                sleep(0)
                MS_SYSTEMMODAL = 0x00001000
                ctypes.windll.user32.MessageBoxW(0, "ID 중복 검사를 해주세요.", "알림", MS_SYSTEMMODAL)
                return redirect(url_for('register'))

        if pw != pwr:
            sleep(0)
            MB_SYSTEMMODAL = 0x00001000
            ctypes.windll.user32.MessageBoxW(0, "비밀번호가 일치하지 않습니다.", "알림", MB_SYSTEMMODAL)
            return redirect(url_for('register'))

        else:
            pw_hash = hashlib.sha256(pw.encode()).hexdigest()
            sql = "INSERT INTO user(user_id,name,pw) VALUES(%s,%s,%s)"
            cur.execute(sql,(myid,name,pw_hash))
            db.commit()
            sleep(0)
            MB_SYSTEMMODAL = 0x00001000
            ctypes.windll.user32.MessageBoxW(0, "회원가입 완료", "알림", MB_SYSTEMMODAL)

        return redirect(url_for('login_proc'))

    return render_template('login_page/register_page.html')


# 회원가입 페이지 아이디 중복확인 GET
@app.route('/register_page.html/register/duplicate', methods=['GET'])
def duplicate():
    print("aaaaaaa")
    sql = "SELECT user_id FROM user"
    cur.execute(sql)
    dup = cur.fetchall()
    # for dups in dup:
    #     dupc = dups

    print(dup)

    return jsonify({'dpc': dup})

# 메인페이지
@app.route('/main', methods=['GET', 'POST'])
def main():
    if "userId" in session:
        return render_template('/main/main_page.html')
    else:
        return jsonify("Who are you?")

# 메인페이지 feed
@app.route('/main/feed', methods=['GET'])
def feed_box_get():
    sql = "SELECT title,user_id,date,category,content,start_price FROM feed"
    cur.execute(sql)
    data = cur.fetchall()
    return jsonify({'feeds': data})

@app.route('/main/IT', methods=['GET'])
def feed_box_it_get():
    sql = "SELECT title,user_id,date,category,content,start_price FROM feed WHERE category = 'it'"
    cur.execute(sql)
    data = cur.fetchall()
    return jsonify({'feeds': data})

@app.route('/main/electron', methods=['GET'])
def feed_box_electron_get():
    sql = "SELECT title,user_id,date,category,content,start_price FROM feed WHERE category = 'electron'"
    cur.execute(sql)
    data = cur.fetchall()
    return jsonify({'feeds': data})

@app.route('/main/life', methods=['GET'])
def feed_box_life_get():
    sql = "SELECT title,user_id,date,category,content,start_price FROM feed category = 'life'"
    cur.execute(sql)
    data = cur.fetchall()
    return jsonify({'feeds': data})

#피드 생성
@app.route("/upload", methods=["POST"])
def upload():
    date = request.form['date_give']
    title = request.form['title_give']
    category = request.form['category_give']
    start_price = request.form['start_price_give']
    content = request.form['content_give']
    upload_files = request.form['files_give']
    if upload_files:
        sql = "INSERT INTO feed(title,content,file,date,status,category,start_price,re_price) VALUES(%s,%s,%s,%s,1,%s,%s,%s)"
        cur.execute(sql,(title,content,upload_files,date,category,start_price,start_price))
        db.commit()
    else:
        sql = "INSERT INTO feed(title,content,date,status,category,start_price,re_price) VALUES(%s,%s,%s,1,%s,%s,%s)"
        cur.execute(sql,(title,content,date,category,start_price,start_price))
        db.commit()
    
    return jsonify({'msg': '게시됨!!'})

#마이페이지
@app.route('/image_url', methods=['POST'])
def image_url():
    profil_url = request.form['url_give']
    sql = "UPDATE user SET profile = %s where user_id = %s"
    cur.execute(sql,(profil_url,session['userId']))
    db.commit()
    return jsonify({'msg': '수정 완료!'})

@app.route('/edit_info', methods=['PUT'])
def edit_info():
    user_name = request.form['name_give']
    if user_name:
        sql = "UPDATE user SET name=%s where user_id = %s"
        cur.execute(sql,(user_name,session['userId']))
        db.commit()
    user_id = request.form['id_give']
    if user_id:
        sql = "UPDATE user SET user_id=%s where user_id = %s"
        cur.execute(sql,(user_id,session['userId']))
        session['userId'] = user_id
        db.commit()
    user_pw = request.form['pw_give']
    if user_pw:
        pw_hash = hashlib.sha256(user_pw.encode()).hexdigest()
        sql = "UPDATE user SET pw=%s where user_id = %s"
        cur.execute(sql,(pw_hash,session['userId']))
        db.commit()
    return jsonify({'msg': '수정 완료!'})

@app.route('/user_info',methods=['GET'])
def user_info():
    sql = "SELECT profile,name FROM user where user_id = %s"
    cur.execute(sql,session['userId'])
    result = cur.fetchall()
    return jsonify({'user_info' : result})

# @app.route('/get_modal',methods=['GET'])
# def get_modal():
#     sql = "SELECT title,name,start_price,date,content FROM user where id= %s"
#     cur.execute(sql,session['userId'])
#     result = cur.fetchall()
#     return jsonify({'user_info' : result})

# @app.route('/get_modal_comment',methods=['GET'])
# def get_modal_comment():
#     sql = "SELECT comment_content,comment_id FROM user where user_id = %s"
#     cur.execute(sql,session['userId'])
#     result = cur.fetchall()
#     return jsonify({'user_info' : result})

# @app.route('/image_url', methods=['POST'])
# def image_url():
#     profil_url = request.form['url_give']
#     sql = "UPDATE user SET profile = %s where user_id = %s"
#     cur.execute(sql,(profil_url,session['userId']))
#     db.commit()
#     return jsonify({'msg': '수정 완료!'})

@app.route('/mypost',methods=['GET'])
def mypost():
    sql = "SELECT title,date,category,id FROM feed where user_id = %s"
    cur.execute(sql,session['userId'])
    result = cur.fetchall()
    return jsonify({'mypost' : result})

@app.route('/edit',methods=['GET'])
def edit():
    sql = "SELECT title,category,start_price,content FROM feed where user_id = %s"
    cur.execute(sql,session['userId'])
    result = cur.fetchall()
    print(result)
    return jsonify({'edit' : result})

@app.route('/mypost_delete',methods=['DELETE'])
def mypost_delete():
    comment_id = request.form['comment_id_give']
    sql = "DELETE FROM feed where id = %s"
    cur.execute(sql,(comment_id))
    db.commit()
    return jsonify({'msg': '삭제 완료!'})

# @app.route('/sale', methods=['GET'])
# def sale():
#     sql = "SELECT 어쩌구 FROM 저쩌구 where id = %s"
#     cur.execute(sql,(,session['userId']))
#     result = cur.fetchall()
#     return jsonify({'' : result})

# @app.route('/purchase', methods=['GET'])
# def purchase():
#     sql = "SELECT 어쩌구 FROM 저쩌구 where id = %s"
#     cur.execute(sql(,session['userId']))
#     result = cur.fetchall()
#     return jsonify({'' : result})

# @app.route('/like', methods=['GET'])
# def like():
#     sql = "SELECT 어쩌구 FROM 저쩌구 where id = %s"
#     cur.execute(sql(,session['userId']))
#     result = cur.fetchall()
#     return jsonify({'' : result})

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5000',debug=True)
