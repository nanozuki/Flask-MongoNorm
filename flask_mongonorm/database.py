from flask import abort
from mongonorm.database import Database as OrigDatabase
from mongonorm import document


def find_one_or_404(cls, filter_=None, *args, **kwargs):
    obj = cls.__collection__.find_one(filter_, *args, **kwargs)
    if obj is None:
        abort(404, "Can't find {0} by {1}".format(cls.__name__, filter_))
    return cls._boxing(obj)


class Database(OrigDatabase):
    def collection(self, name):
        collection = self.get_collection(name)

        def decorator(cls):
            cls.__collection__ = collection
            setattr(cls, 'find_one_or_404', classmethod(find_one_or_404))
            for method in document.property_methods:
                setattr(cls, method, property(getattr(document, method)))
            for method in document.class_methods:
                setattr(cls, method, classmethod(getattr(document, method)))
            for method in document.normal_methods:
                setattr(cls, method, getattr(document, method))
            return cls
        return decorator
