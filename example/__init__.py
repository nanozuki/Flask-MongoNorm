#!/usr/bin/env python
from flask import Flask, jsonify
from flask_mongonorm import MongoNorm, BSONEncoder


app = Flask(__name__)
app.config['MONGONORM_URI'] = "mongodb://localhost:27017/"
app.json_encoder = BSONEncoder


mongo = MongoNorm()


@mongo.test.collection('test')
class TheModel(object):
    def __init__(self, n):
        self.insert({'test_id': n})

    def get_id(self):
        return self['test_id']


mongo.init_app(app)


@app.route('/')
def index():
    TheModel.delete_many({})
    TheModel(2)
    tm = TheModel.find_one_or_404({'test_id': 2})
    return jsonify(tm.copy())


if __name__ == '__main__':
    app.run()
