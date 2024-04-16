#!/usr/bin/python3

def lookup(obj):
    """
    Return a list of obj attrributes

    obj: an instant of a class
    """
    return dir(obj)
