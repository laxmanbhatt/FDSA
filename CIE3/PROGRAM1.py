class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear_node is None:
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def front(self):
        if self.front_node is None:
            return None
        return self.front_node.data

    def dequeue(self):
        if self.front_node is None:
            return None
        dequeued_data = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        return dequeued_data

    def is_empty(self):
        return self.front_node is None

if __name__ == "__main__":
    q = Queue()
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("Front of the queue:", q.front())
    print("Dequeue:", q.dequeue())
    print("Front of the queue after dequeue:", q.front())
    print("Is the queue empty?", q.is_empty())
    
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Is the queue empty after all dequeues?", q.is_empty())
    print("Dequeue from empty queue:", q.dequeue())
