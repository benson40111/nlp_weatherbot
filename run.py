from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_paginate import Pagination, get_page_parameter

from modules.db.mongo import Course
from modules.webhook.makewebhook import Webhook
from modules.course.course import Search_Course

app = Flask(__name__)

@app.route('/nlp/', methods=['GET'])
def index():
    search = False
    department = request.args.get('department')
    category = request.args.get('category') 
    grade = request.args.get('grade')
    week = request.args.get('week')
    q = request.args.get('q')
    return_all = None
    if (request.args.get('time')):
        time = request.args.get('time').split(',')
    else:
        time = []
    if (q):
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    return_all = Search_Course(department, category, grade, week, time).get_data()[(page-1)*10:page*10]
    pagination = Pagination(page=page, total=return_all.count(), search=search, record_name='course')

    return render_template('table.html', **locals())

@app.route('/nlp/insert', methods=['POST'])
def insert():
    if (request.method == 'POST'):
        num = request.form['num']
        grade = request.form['grade']
        if (num and grade):
            Course.objects(course_id=num).update_one(set__grade=grade)

    return redirect(url_for('index'))


@app.route('/nlp/send', methods=['POST', 'GET'])
def send():
    if (request.method == 'POST'):
        text = ''
        search_str = request.form['search']
        if (search_str):
            text = Webhook().send_message(search_str)
        else:
            text = ''
        return render_template('send_message.html', **locals())
    else:
        return render_template('send_message.html', **locals())

@app.route('/nlp/get', methods=['POST', 'GET'])
def get():
    if (request.method == 'GET'):
        speech = request.args.get('speech')
        print(speech)
        if (speech):
            speech = Webhook().send_message(speech)
            if (speech[0:10] == 'https://va'):
                return_text = { 'text':'您所查詢的課程資料如下：\n', 'url':speech }
            elif (speech[0:5] == 'https'):
                return_text = { 'text':'對不起我聽不懂，我幫您去查詢google的結果如下：\n', 'url':speech }
            else:
                return_text = { 'text':speech, 'url':'' }
        else:
            return_text = { 'text':'', 'url':'' }
        print(return_text)
        return jsonify(return_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

