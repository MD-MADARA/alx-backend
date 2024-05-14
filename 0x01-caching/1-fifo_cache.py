#!/usr/bin/env python3
""" BasicCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system
    """
    def put(self, key, item):
        """ assign to cache_data the item value for the key key
        """
        self.cache_data[key] = item
        if key and item:
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = list(self.cache_data.keys())[0]
                del self.cache_data[discarded]
                print("DISCARD:", discarded)

    def get(self, key):
        """ return the value in cache_data linked to key
        """
        return self.cache_data.get(key, None)
