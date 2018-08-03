from . import  index_blu
from info import redis_stors

@index_blu.route('/')
def index():
    redis_stors.set('name','itcast')
    return 'index'