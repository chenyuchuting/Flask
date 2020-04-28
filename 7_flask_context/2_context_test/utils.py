from flask import g
# def log_a(username):
#     print('log a %s' % username)
#
# def log_b(username):
#     print('log b %s' % username)
#
# def log_c(username):
#     print('log c %s' % username)
#
def log_a():
    print('log a %s' % g.username)

def log_b():
    print('log b %s' % g.username)

def log_c():
    print('log c %s' % g.username)