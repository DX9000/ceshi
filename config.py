import redis

class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'mysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SECRET_KEY = '4asd86s4ad56sa4d56asd456ad4a56das56d4sa8q9efc1q'

    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFEIME = 86400

