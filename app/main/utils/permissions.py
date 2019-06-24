# coding:utf-8
from flask import g, flash
from functools import wraps
permissions = list()


class Permission(object):

    def __init__(self, module=None, action=None):
        self.module = module
        self.action = action

    def check(self, module, func):
        if not self.current_user:
            return False
        return self.current_user.check('{module}.{action}'.format(
            module=module,
            action=func
        ))

    def deny(self):
        return flash(4003, u'无权访问')

    def __call__(self, func):
        permissions.append({
            'action': '{}.{}'.format(func.__module__, func.__name__),
            'name': func.__doc__
        })

        @wraps(func)
        def decorator(*args, **kwargs):
            if not self.check(func.__module__, func.__name__):
                return self.deny()
            return func(*args, **kwargs)
        return decorator

    def __enter__(self):
        if not self.check(self.module, self.action):
            try:
                self.deny()
            except Exception as e:
                raise e
            else:
                pass

    def __exit(self):
        pass

    @property
    def current_user(self):
        return g.user


permission = Permission()