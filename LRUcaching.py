#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
        
        
    

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.time_keeper = {}
        self.count = 0
        
    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.time_keeper[self.count] = key
                self.count += 1
            else:
                used_list = sorted(self.time_keeper.keys())
                print(f'DISCARD: {self.time_keeper[used_list[0]]}')
                del self.cache_data[self.time_keeper[used_list[0]]]
                del self.time_keeper[used_list[0]]
                self.cache_data[key] = item
                self.count += 1
                self.time_keeper[self.count] = key


    def get(self, key):
        """
        Gets cached data from memory using the given key
        """
        if not key or key not in self.cache_data.keys():
            return None
        self.count += 1
        for k, v in self.time_keeper.items():
            if key == v:
                del self.time_keeper[k]
                break
        self.time_keeper[self.count] = key
        return self.cache_data[key]
        
        
        
        
my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
