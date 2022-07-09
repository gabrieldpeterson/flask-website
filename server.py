from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def index(page_name):
    return render_template(page_name)


def write_to_file(ddata):
    with open('database.txt', 'a') as f:
        save_text = f'{ddata["name"]},{ddata["email"]},{ddata["message"]}\n'
        f.write(save_text)


def write_to_csv(ddata):
    with open('database.csv', newline='', mode='a') as f:
        name = ddata["name"]
        email = ddata["email"]
        message = ddata["message"]
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
