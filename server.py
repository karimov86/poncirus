from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        save_data_csv(data)
        return 'form submitted'
    return 'something went wrong'

def save_data(data):
    with open("database.txt", "a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"\n{email},{subject},{message}")

def save_data_csv(data):
    with open("database.csv", "a", newline='') as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow((email,subject,message))