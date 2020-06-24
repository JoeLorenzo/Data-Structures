class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def add_to_head(self, value):
        # create a new node
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new node should point to current head
            new_node.next_node = self.head
            # new head equals to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a new node
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to the new node
             self.tail.next_node = new_node
             self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty do nothing
        if not self.head:
            return None
        # if list has only one element set head and tail to None
        if self.head.next_node == None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise if we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    # def remove_tail(self)
    #     # check if list is empty
    #     if not self.head:
    #         return None

    #     # check if list has one element 
    #     if self.head.next_node == None:
    #         head_value = self.head.value
    #         self.head = None:
    #         self.tail = None:
    #         return head_value
    #     # otherwise if we have more than one element 
    #     tail_value = self.tail.value
    #     self.tail = 
        

    def contains(self, value):
        # check if list is empty first, if so return false
        if self.head is None:
            return False
        # loop through each node until we see the value or we could not go further
        current_node = self.head  
        while current_node is not None:
            if current_node.value == value:
                return True
            # otherwise go to the next node
            current_node = current_node.next_node
        return False


# lets intialize the linked list class
linked_list = LinkedList()
# lets add a "B" value to the head
linked_list.add_to_head("B")
# lets add a "Z" value to the tail
linked_list.add_to_tail("Z")
# lets test the contians function
print(f"does the linked list containt M?: {linked_list.contains('M')}")
print(f"does the linked list containt B?: {linked_list.contains('A')}")
# lets check that add_to_head is adding a node to start of the list
linked_list.add_to_head("A")
print(f"the start of the linked list is {linked_list.head.value}")
# lets check that remove_head function is removing the head node to start of the list
linked_list.remove_head()
print(f"the start of the linked list is {linked_list.head.value}")
# linked_list.remove_tail()
# print(f"the end of the linked list is {linked_list.tail.value}")

