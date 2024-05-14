#!/usr/bin/env python3
""" LIFOCache
"""
from base_caching import BaseCaching
from collections import OrderedDict


# class LIFOCache(BaseCaching):
#     """ LIFO caching system
#     """
#     def put(self, key, item):
#         """ assign to cache_data the item value for the key key
#         """
#         if key and item:
#             self.cache_data.pop(key, None)
#             self.cache_data[key] = item
#             if len(self.cache_data) > BaseCaching.MAX_ITEMS:
#                 discarded = list(self.cache_data.keys())[-2]
#                 del self.cache_data[discarded]
#                 print("DISCARD:", discarded)

#     def get(self, key):
#         """ return the value in cache_data linked to key
#         """
#         return self.cache_data.get(key, None)


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
