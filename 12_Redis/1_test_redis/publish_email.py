from redis import Redis


cache = Redis(host='127.0.0.1', port=6379)

for i in range(3):
    cache.publish('email', '123@qq.com')