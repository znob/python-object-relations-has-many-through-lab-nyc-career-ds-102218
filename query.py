from trip import Trip
from song import Song

class Query:

    @classmethod
    def get_attrs(cls, join_class, instance_obj):
        instance_objs = join_class.all()
        name_of_instance = instance_obj.__class__.__name__.lower()
        return [obj for obj in instance_objs if getattr(obj, name_of_instance) == instance_obj]

    @classmethod
    def get_trips(cls, instance_obj):
        _list = cls.get_attrs(Trip, instance_obj)
        return _list

    @classmethod
    def get_songs(cls, instance_obj):
        _list = cls.get_attrs(Song, instance_obj)
        return _list

    @classmethod
    def get_attributes(cls, list_of_instances, attribute):
        return [getattr(instance, attribute) for instance in list_of_instances]
