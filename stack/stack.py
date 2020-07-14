from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.items = []
        

#     def __len__(self):
#         return len(self.items)
        

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         if self.items.__len__() == 0:
#             pass
#         else:
#             value = self.items[len(self.items) - 1]
#             self.items.pop()
#             return value




class Stack:
    def __init__(self):
        self.size = 0
        self.items = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.items.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.items.remove_tail()


















