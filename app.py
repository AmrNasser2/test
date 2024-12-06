from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('DBproject.html')
@app.route('/Aboutus')
def about():  # put application's code here
    return render_template('Aboutus.html')

if __name__ == '__main__':
    app.run()
