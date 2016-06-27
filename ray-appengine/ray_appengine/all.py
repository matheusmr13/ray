
from ray.model import Model
from google.appengine.ext.ndb import Model as AppEngineModel


class GAEModel(AppEngineModel, Model):

    @classmethod
    def columns(cls):
        return sorted(cls._properties.keys())

    def put(self):
        super(GAEModel, self).put()
        AppEngineModel.put(self)
        return self

    def remove(self, *args, **kwargs):
        super(AppEngineModel, self).delete()
        return self.key.delete()

    def to_json(self):
        return self.to_dict()

    @classmethod
    def find(cls, *args, **kwargs):
        query = cls.query()

        if not kwargs:
            return query.fetch()

        for field, value in kwargs.items():
            query = query.filter(getattr(cls, field) == value)

        return query.fetch()

    @classmethod
    def get(cls, id=None):
        return cls.get_by_id(id)
