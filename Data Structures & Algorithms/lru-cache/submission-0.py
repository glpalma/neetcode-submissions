class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mem = dict() # key -> Node(value)
        # Using dummy head and tail simplifies linked list operations
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node: Node):
        # Add right before tail (most recently used)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        node = self.mem.get(key)
        if not node:
            return -1

        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self._remove(self.mem[key])
        elif len(self.mem) == self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.mem[lru.key]

        new = Node(key, value)
        self._add(new)
        self.mem[key] = new