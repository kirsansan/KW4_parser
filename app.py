""" my project for learning API and  flask
    this code written by Kirill.S (Mr.K)
"""

import flask
from flask import Flask, render_template, request, url_for, abort, flash
from config.table_of_content import site_menu, l1_menu
from src.model import *
from src.savers import *
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = "lmlmmlmlml666lmlmlm81dvfhg"
# app.config['FLASK_DEBUG'] = 1


@app.route('/')
def index():
    # return '<h1>Hello, %s!</h1>' % "K"
    return render_template('index.html', title="K_Parser", menu=site_menu, submenu=l1_menu)


@app.route('/about', methods=['POST', 'GET'])
def about():
    """in the future may be this page will send e-mail to me"""
    return render_template('about.html', menu=site_menu)


@app.route('/files', methods=['POST', 'GET'])
def request_from_files():
    main_content: list[dict] = []
    if request.method == 'POST':
        keyword = request.form['keyword']
        count = int(request.form['count']) if request.form['count'].isdigit() else 0
        count = MAX_COUNT_VACANCY_FOR_USER_DISPLAY if count > MAX_COUNT_VACANCY_FOR_USER_DISPLAY else count
        if count > 0:
            saver = JSONSaver(FILE_FOR_VACANCY_JSON)
            vvl: list[Vacancy] = saver.read()
            vvl.sort(reverse=True)
            # print("================================================================")
            for i in range(0, count):
                main_content.append(vvl[i].get_json())
            # print(main_content)
    return render_template('request_files.html', menu=site_menu, mytext=[''], content=main_content)


@app.route('/req', methods=['POST', 'GET'])
def request_from_api():
    if request.method == 'POST':
        print('Request')
        print(request.form)
        a = request.form['keyword']
        print("a=", a)
        flash("Request have just already sent - you need wait...", "success")
        # time.sleep(3)
        # flash("All requests has just done")
        # flash("You will redirect for working with local files")
    return render_template('request_api.html', menu=site_menu, mytext=['use code: 1- moscow, 2 - st.peterburg'])


@app.route('/test')
def hello_one_more_time():
    return render_template('hello.html',
                           title="test page",
                           menu=site_menu,
                           hello='Hello World! Do you want to have some test?')
    # return '<h1>Hello World! Do you want to have some test? </h1>'


@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello, %s!</h1>' % name
    return render_template('hello.html', title="WOW", menu=site_menu, hello=f'Hello, {name}!')


@app.route('/testPOS', methods=['POST', 'GET'])
def create_for_post():
    if request.method == 'POST':
        print(request.form)
    return render_template('answer.html', menu=site_menu, mytext=['use code: 1- moscow, 2 - st.peterburg'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', menu=site_menu), 404


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5003)
