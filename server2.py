from flask import Flask, render_template, url_for, request, redirect
import csv
# import requests
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',')
        csv_writer.writerow([email, subject, message])
        # file = database2.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')            
        except: 
            raise         


    else:
        return 'something is wrong'


    # return 'Form submitted1 Horrayyy!'



# @app.route('/favicon.ico')
# def icon():
#     return 'This is my blogs about dogs!'

# set FLASK_APP=server.py
# set FLASK_ENV=development
# flask run  or # python -m flask run

