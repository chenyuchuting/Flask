import memcache


# 在连接之前，一定要通过cmd窗口进入到memcached文件中启动memcached
# 1. 建立链接
mc = memcache.Client({'127.0.0.1:11211'}, debug=True)
# 分布式的储存
mc = memcache.Client(['127.0.0.1:11211','192.168.0.102:11211'], debug=True)

# 在cmd命令窗口下，使用telnet 127.0.0.1 11211进入
# 2.设置数据
# mc.set('name', 'link', time=60)
mc.set_multi({'title':'python', 'author':'link', 'age': 10}, time=60)

# 3. 获取数据
title = mc.get('title')
print(title)

# 4. 删除数据
mc.delete('title')
title = mc.get('title')
print(title)

# 5. 自增长和自降低
mc.incr('age', delta=10)
mc.decr('age', delta=2)
age = mc.get('age')
print(age)

