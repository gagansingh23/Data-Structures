from singly_linked_list import LinkedList
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
# """
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.queue = []
        
#     def __len__(self):
#         return len(self.queue)

#     def enqueue(self, value):
#         self.queue.append(value)


#     def dequeue(self):
#         if self.queue == []:
#             return None
#         return self.queue.pop(0)
        


# enqueue adds an element to the back of the queue.
# dequeue removes and returns the element at the front of the queue.
# len returns the number of elements in the queue.

class Queue:
    def __init__(self):
        self.size = 0
        self.queue = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.queue.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.queue.remove_head()
