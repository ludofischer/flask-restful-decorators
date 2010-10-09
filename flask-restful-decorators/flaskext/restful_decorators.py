from __future__ import absolute_import
import types
import flask

def _route_for_method(self, rule, method, **options):
    def decorator(f):
        self.add_url_rule(rule, None, f, methods=(method,), **options)
        return f
    return decorator

def _get(self, rule, **options):
    return _route_for_method(self, rule, 'GET', **options)


def _post(self, rule, **options):
    return _route_for_method(self, rule, 'POST', **options)

def _put(self, rule, **options):
    return _route_for_method(self, rule, 'PUT', **options)

def _delete(self, rule, **options):
    return _route_for_method(self, rule, 'DELETE', **options)

def add_restful_decorators(app):
    app = app
    app.get = types.MethodType(_get, app, flask.Flask)
    app.post = types.MethodType(_post, app, flask.Flask)
    app.put = types.MethodType(_put, app, flask.Flask)
    app.delete = types.MethodType(_delete, app, flask.Flask)
