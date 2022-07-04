#!/usr/bin/python3
"""
int sub class
"""


class MyInt(int):

    """
    int sub class
    """
    def __eq__(self, Other):

        """
        implement equal method
        """
        return self.real != Other

    def __ne__(self, Other):

        """
        implemet not equal method
        """
        return self.real == Other
