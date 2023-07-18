"""Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity."""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict.pop(key)
            self.dict[key] = val
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict.keys():
            if len(self.dict.keys()) == self.capacity:
                del self.dict[next(iter(self.dict))]
        else:
            self.dict.pop(key)
        self.dict[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
