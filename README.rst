Flask-MongoNorm
===============

`中文文档 <README_cn.rst>`_

MongoNorm support for Flask applications.

installation
------------

Use pip to install::

    pip install MongoNorm

Use guide
---------

1. Init by Flask app

As Mostly Flask Extension, there are two methods to init Flask-MongoNorm.
You can init by app directly::

    from flask_mongonorm import MongoClient

    client = MongoClient(app)
    db = client.test

Or you can init Flask-MongoNorm by `init_app`::

    client = MongoClient()
    db = client.test

   client.init_app(app)

**Tips about lazy load:**

Until you use your model class or call methods of MongoClient or Database,
it won't try to connect to Mongo Server.

Notice the example below, You can make db before `init_app`. This feature can`
let you use decorator `@db.collection("article")` without exception of
"no application bound"

2. Some useful tools.

* shortcut for find a document or raise 404::

    Article.find_one_or_404({'title': 'Flask-MongoNorm'})

* A json encoder for ObjectId and Datetime::

    from flask_mongonorm import BSONEncoder
    app.json_encoder = BSONEncoder

this encoder will encode ObjectId to str and datetime to unix time(seconds).
