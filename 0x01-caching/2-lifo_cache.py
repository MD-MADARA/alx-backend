#!/usr/bin/env python3
""" LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system
    """
    def put(self, key, item):
        """ assign to cache_data the item value for the key key
        """
        if key and item:
            #  If the key already exists, ensure it is deleted before insertion
            #  to guarantee it becomes the most recently inserted key.
            self.cache_data.pop(key, None)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = list(self.cache_data.keys())[-2]
                del self.cache_data[discarded]
                print("DISCARD:", discarded)

    def get(self, key):
        """ return the value in cache_data linked to key
        """
        return self.cache_data.get(key, None)
