class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.dic = dict()
        # initially the linked list only has two elements, head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            n = self.dic[key]
            # Remove the key from linked list and add it to the top of the list
            self.list_remove(n)
            self.list_add(n)
            return n.value
        # if not found
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # If key already in dictionary, just bring it to top of the list.
        if key in self.dic:
            # Remove it from the current position
            n = self.dic[key]
            self.list_remove(n)
        # Create a new node and add it to the top of list
        new_node = Node(key, value)
        # Add this new node to the dictionary or update its value to the new node if the key already exists
        self.dic[key] = new_node
        # Add this new_node to the end of the list
        self.list_add(new_node)
        # if capacity is  reached:
        if len(self.dic) > self.capacity:
            # Remove the LRU, i.e the node at the head
            node_to_remove = self.head.next
            self.list_remove(node_to_remove)
            # Delete this node from the dic
            del self.dic[node_to_remove.key]

    def list_add(self, node):
        # Add a node to the end of  linked list, i.e previous to the tail
        curr_last = self.tail.prev
        self.tail.prev = node
        node.prev = curr_last
        curr_last.next = node
        node.next = self.tail

    def list_remove(self, node):
        # Remove a node from  the list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)