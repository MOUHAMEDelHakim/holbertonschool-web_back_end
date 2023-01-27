#!/usr/bin/env python3
"""
 Basic dictionary
"""
BaseCaching = __import__('BaseCaching').baseCaching
class BasicCache (BaseCaching):

    """
   basicCache
    """


    def put(self, key, item):

     if(key, item is None ):
        self.cache_data[key] = item

    def get(self, key):
     if key is None or key not in self.cache_data.keys():
        return None
     else:
        return self.cache_data[key]
