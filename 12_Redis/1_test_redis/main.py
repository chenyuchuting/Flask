from redis import Redis


cache = Redis(host='127.0.0.1', port='6379')


# 1. 操作字符串
# cache.set('name', 'link')
# print(cache.get('name'))


# 2. 列表的操作
# cache.lpush('languages', 'python')
# cache.lpush('languages', 'c')
# cache.lpush('languages', 'java')
# print(cache.lrange('languages', 0, -1))

# 3. 集合操作
# cache.sadd('school', 'qinghua')
# cache.sadd('school', 'beida')
# print(cache.smembers('school'))


# 4. 哈希操作
# cache.hset('websites', 'baidu', 'www.baidu.com')
# cache.hset('websites', 'google', 'www.google.com')
# print(cache.hgetall('websites'))


# 5. 事务操作
# pip = cache.pipeline()
# pip.set('name', 'link')
# pip.set('age', 18)
# pip.execute()


# 发布与订阅，异步发送邮件
# 此处push不同，要做个笔记
ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():
        if item['type'] == 'message':
            data = item['data']
            print(data)
