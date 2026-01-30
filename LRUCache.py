
#146. LRU Cache
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
