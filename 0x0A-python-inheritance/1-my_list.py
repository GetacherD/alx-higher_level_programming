#!/usr/bin/python3
"""
class that inherits list
"""


class MyList(list):

    """
    class Representing list subclass
    """
    def print_sorted(self):

        """
        a function that print list sorted
        """
        if any(not isinstance(i, int) for i in self):
            raise TypeError("all elements must be int")
        if not isinstance(self, MyList):
            raise TypeError("obj must be a MyList Type")
        print(sorted(self))
