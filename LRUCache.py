
#146. LRU Cache
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)   # LRU end (dummy)
        self.right = Node(0, 0)  # MRU end (dummy)
        self.left.next = self.right
        self.right.prev = self.left


     def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node


    def get(self, key: int) -> int:

