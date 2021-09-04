from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if value is None:
            return -1
        else:
            self.cache.move_to_end(key, last=True)
            return value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) is None:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value