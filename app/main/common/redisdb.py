# coding = utf-8
# @Time    : 2018/1/30 0030 21:23
# @Author  : Carl
# @Site    : 
# @File    : redisdb.py
# @Software: PyCharm

import redis
_redis_cache = redis.Redis(connection_pool=redis.ConnectionPool(host='127.0.0.1', port=6379, password = '', db=1))
_redis_db = redis.StrictRedis(host='127.0.0.1', port=6379, password = '', db=2)


class RedisDB:
    def __init__(self, conn=_redis_db):
        self.conn = conn
    def set(self, key, value, expire=None):
        self.conn.set(key, value, expire)
    def hget(self, name, key):
        ret = self.conn.hget(name, key)
        if ret:
           ret = ret.decode('utf-8')
        return ret
    def hset(self, name, key, value):
        self.conn.hset(name, key, value)

class RedisCache(RedisDB):
    def __init__(self):
        super().__init__(_redis_cache)