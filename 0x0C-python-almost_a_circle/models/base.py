#!/usr/bin/python3
"""
Base Class
"""
import json


class Base:

    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """
        Initialize new objects
        Args:
            id : id of  new objects
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """ convert to json string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        ret = []
        for o in list_dictionaries:
            if type(o) == dict:
                ret.append(o)
            elif isinstance(o, Base):
                ret.append(o.to_dictionary())
            else:
                pass
        return json.dumps(ret)

    @classmethod
    def save_to_file(cls, list_objs):

        """ save json str to file """
        filename = cls.__name__+".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):

        """ get objects from json """
        import json
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """ Create new objects """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):

        """ Load from file """
        pass
