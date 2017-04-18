from flask import abort
from mongonorm import document
from mongonorm.database import Database as NormDatabase, OrigCollectionFactory


def find_one_or_404(cls, filter_=None, *args, **kwargs):
    obj = cls.o_collection().find_one(filter_, *args, **kwargs)
    if obj is None:
        abort(404, "Can't find {0} by {1}".format(cls.__name__, filter_))
    return cls._boxing(obj)


class Database(NormDatabase):
    def __init__(self, client, name, lazy_load=True):
        super().__init__(client, name, lazy_load)

    def collection(self, name):
        collection_factory = OrigCollectionFactory(self, name)

        def decorator(cls):
            cls._o_collection_factory = collection_factory
            cls._o_collection = None
            setattr(cls, 'find_one_or_404', classmethod(find_one_or_404))
            if 'default_values' not in cls.__dict__:
                setattr(cls, 'default_values', {})
            for method in document.property_methods:
                setattr(cls, method, property(getattr(document, method)))
            for method in document.class_methods:
                setattr(cls, method, classmethod(getattr(document, method)))
            for method in document.normal_methods:
                setattr(cls, method, getattr(document, method))
            return cls
        return decorator
