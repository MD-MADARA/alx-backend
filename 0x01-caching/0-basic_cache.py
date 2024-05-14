#!/usr/bin/env python3
""" BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ a caching system
    """
    def put(self, key, item):
        """ assign to cache_data the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in cache_data linked to key
        """
        return self.cache_data.get(key, None)
