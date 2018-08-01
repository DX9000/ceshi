from flask import Flask

app = Flask(__name__)

class Config():
    DEBUG = True


@app.route('/index')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()