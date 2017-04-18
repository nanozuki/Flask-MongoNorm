Flask-MongoNorm
===============

`English version <README.rst>`_

MongoNorm support for Flask applications.

安装
----

Use pip to install::

    pip install MongoNorm

使用
----

1. 插件的初始化

如同其他flask插件，有两种方式来初始化Flask-MongoNorm。可以直接使用app创建::

    from flask_mongonorm import MongoClient

    client = MongoClient(app)
    db = client.test

也可以通过 `init_app` 来初始化::

    client = MongoClient()
    db = client.test

   client.init_app(app)

**关于lazy load:**

MongoNorm的懒加载特性使得，在使用Model的类方法，或者使用MongoClient或者Database
的方法之前，MongoNorm不会试图链接Mongo Server.

注意到上面那个例子，可以在调用`init_app`之前就通过key来指定db。  
通过这个特性，在app启动之前，可以使用装饰器 `@db.collection("article")` 去修饰
你的Model类，而不会收到 "no application bound" 的错误

2. 一些有用的工具

* 找到一个document或者抛出一个404错误的快捷方式::

    Article.find_one_or_404({'title': 'Flask-MongoNorm'})

* 一个支持ObjectId和datetime的json encoder::

    from flask_mongonorm import BSONEncoder
    app.json_encoder = BSONEncoder

这个encoder会把ObjectId转换成字符串，把datetime转换成unix时间戳(秒)。
