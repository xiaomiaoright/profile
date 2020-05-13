from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/index.html')
def my_home_index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')



@app.route('/works.html')
def work():
    return render_template('works.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')



@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/<string: page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/favicon.ico')
# def icon():
#     return 'This is my blogs about dogs!'

# set FLASK_APP=server.py
# set FLASK_ENV=development
# flask run  or # python -m flask run

