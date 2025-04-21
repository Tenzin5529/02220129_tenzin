class Node:
    def __init__(self, data=None):
        self.data = data  # stores the data element
        self.next = None  # references the next node
class LinkedQueue:
    def __init__(self):
        self.front = None  # points to the front of the queue
        self.rear = None   # points to the rear of the queue
        self.size = 0      # tracks the number of elements

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear:  # If the queue is not empty, add to the rear
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:  # If the queue was empty, the new node is the front as well
            self.front = new_node
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue is now empty, set rear to None
            self.rear = None
        self.size -= 1
        print(f"Dequeued element: {dequeued_data}")
        self.display()
        return dequeued_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def size(self):
        return self.size

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display queue: {elements}")
queue = LinkedQueue()
print(f"Created new LinkedQueue")
print(f"Queue is empty: {queue.is_empty()}")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.peek()
queue.dequeue()
print(f"Queue size: {queue.size}")

#Part 1: Queue Implementation using Array
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity  # Default capacity
        self.queue = [None] * capacity  # Underlying array storage
        self.front = -1  # Tracks the front index
        self.rear = -1   # Tracks the rear index

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full!")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        element = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    def size(self):
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - self.front + self.rear + 1

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        if self.rear >= self.front:
            print("Display queue:", self.queue[self.front:self.rear + 1])
        else:
            print("Display queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

# Example usage
queue = ArrayQueue()
print(f"Created new Queue with capacity: {queue.capacity}")
print(f"Queue is empty: {queue.is_empty()}")

queue.enqueue(10)
queue.display()
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
queue.peek().
queue.dequeue()
queue.display()
print(f"Queue size: {queue.size()}")
