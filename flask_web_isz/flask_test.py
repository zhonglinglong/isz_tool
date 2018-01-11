# -*- coding:utf8 -*-

from flask import Flask

app = Flask(__name__)

print app.route('/')
@app.route('/')
def index():
    return '<h1>Hello Wolrd!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s</h1>' % name


if __name__ == "__main__":
    app.run(debug = True)