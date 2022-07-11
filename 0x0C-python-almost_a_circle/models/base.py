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
        return [json.dumps(d) for d in list_dictionaries]

    @classmethod
    def save_to_file(cls, list_objs):

        """ save json str to file """
        import json
        filename = cls.__name__+".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                js = [o.to_dictionary() for o in list_objs]
                f.write(json.dumps(js))

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
