from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from config import Config

app = Flask(__name__)





app.config.from_object(Config)
db = SQLAlchemy(app)
redis_stors = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
app.config.from_object(Config)

CSRFProtect(app)
Session(app)
zhangsan= Manager(app)



@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()