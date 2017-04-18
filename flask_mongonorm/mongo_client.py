from flask import current_app
from mongonorm.mongo_client import MongoClient as NormClient,\
    OrigMongoClient, OrigClientFactory

from .database import Database


class MongoClient(NormClient):
    def __init__(self, app=None):
        super().__init__()
        self.app = app
        self._client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MONGONORM_URI", "mongodb://localhost:27017/")
        app.extensions['MongoNorm_client'] = None
        app.teardown_appcontext(self.teardown)

    @property
    def o_client(self):
        if current_app.extensions['MongoNorm_client'] is None:
            current_app.extensions['MongoNorm_client'] = OrigClientFactory(
                current_app.config['MONGONORM_URI']).make()
        return current_app.extensions['MongoNorm_client']

    def teardown(self, exception):
        if current_app.extensions['MongoNorm_client'] is not None:
            current_app.extensions['MongoNorm_client'].close()

    def __getattr__(self, name):
        if name in OrigMongoClient.__dict__:
            return self.o_client.__getattr__(name)
        else:
            return Database(self, name)

    def __getitem__(self, item):
        return Database(self, item)
