from flask import Flask, render_template, flash, request
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'scikit4life'

@app.route("/", methods=['GET', 'POST'])
def index():
    data = "Hello World!"
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(host='0.0.0.0') # export FLASK_APP=dashboard.py
