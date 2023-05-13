""" my project for learning API and  flask
    this code written by Kirill.S (Mr.K)
"""

import flask
from flask import Flask, render_template, request, url_for, abort
from config.table_of_content import site_menu, lesson1_menu


app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html', title="K_Parser", menu=site_menu, submenu=lesson1_menu)



@app.route('/about')
def about():
    return render_template('about.html', menu=site_menu)


@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html', menu=site_menu, submenu=lesson1_menu)


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
    print(request.form)
    return render_template('answer.html', menu=site_menu, mytext=['test POS method'])



if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
