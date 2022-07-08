#!/usr/bin/python3
"""
Base Class
"""


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
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """ save json str to file """
        import json
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                json.dump("[]", f)
            else:
                json.dump(Base.to_json_string(list_objs), f)
