from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Abhay! My Flask App is Running."

@app.route('/about')
def about():
    return "This is my first Flask application."

if __name__ == '__main__':
    app.run(debug=True)