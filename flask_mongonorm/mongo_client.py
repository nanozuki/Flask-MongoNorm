from flask import current_app
from flask import _app_ctx_stack as stack
from mongonorm import MongoClient as OrigMongoClient
from mongonorm.database import DataBase as OrigDataBase

from flask_mongonorm.database import DataBase


class MongoClient(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MONGONORM_URI", "mongodb://localhost:27017/")

    def mongo_client(self):
        return OrigMongoClient(current_app.config['MONGONORM_URI'])

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mongonorm_client'):
                ctx.mongonorm_client = self.mongo_client()
            return ctx.mongonorm_client

    def __getattr__(self, name):
        rtn = getattr(self.client, name)
        if isinstance(rtn, OrigDataBase):
            return DataBase(rtn)
