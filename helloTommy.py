from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<strong>Hello Tommy!</strong>"

if __name__ == '__main__':
    app.run()
