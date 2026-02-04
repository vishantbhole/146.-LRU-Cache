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
         if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

     def put(self, key: int, value: int) -> None:
         if key in self.cache:
            self.remove(self.cache[key])
             
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key

def run_ops(ops, args):
    out = []
    obj = None
    for op, a in zip(ops, args):
        if op == "LRUCache":
            obj = LRUCache(a[0])
            out.append(None)
        elif op == "put":
            obj.put(a[0], a[1])
            out.append(None)
        elif op == "get":
            out.append(obj.get(a[0]))
        else:
            raise ValueError(f"Unknown op: {op}")
    return out


if __name__ == "__main__":
    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    print(run_ops(ops, args))
    # Expected: [None, None, None, 1, None, -1, None, -1, 3, 4]

    ops1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args1 = [[2], [1, 1], [5, 5], [5], [6, 6], [6], [4, 4], [5], [1], [4]]
    print(run_ops(ops1, args1))
    # Expected: [None, None, None, 5, None, 6, None, -1, -1, 4]
