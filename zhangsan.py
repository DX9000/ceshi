from flask import Flask,session
from flask.ext.sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from config import Config
from info import creat_app, db




app = creat_app('1')

zhangsan= Manager(app)
Migrate(app, db)
zhangsan.add_command('db', MigrateCommand)





if __name__ == '__main__':
    app.run()