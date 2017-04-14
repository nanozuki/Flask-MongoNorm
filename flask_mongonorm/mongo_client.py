from flask import current_app
from flask import _app_ctx_stack as stack

from mongonorm import MongoClient as OrigMongoClient
from mongonorm.database import Database as OrigDatabase
from flask_mongonorm.database import Database


class MongoClient(object):
    def __init__(self, app=None):
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MONGONORM_URI", "mongodb://localhost:27017/")
        app.teardown_appcontext(self.teardown)

    def mongo_client(self):
        return OrigMongoClient(current_app.config['MONGONORM_URI'])

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'mongonorm_client'):
            ctx.mongonorm_client.close()

    @property
    def client(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'mongonorm_client'):
                ctx.mongonorm_client = self.mongo_client()
            return ctx.mongonorm_client

    def __getattr__(self, name):
        attr = getattr(self.client, name)
        if isinstance(attr, OrigDatabase) is True:
            return Database(self.client, name)
        return attr

    def __getitem__(self, item):
        item_ = getattr(self.client, item)
        if isinstance(item_, OrigDatabase) is True:
            return Database(self.client, item)
        return item_
