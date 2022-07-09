from flask import Flask, render_template, request, redirect

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


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'
