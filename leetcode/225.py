from queue import Queue

class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue1.put(x)

    def pop(self) -> int:
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        popped_element = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element

    def top(self) -> int:
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        top_element = self.queue1.get()
        self.queue2.put(top_element)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self) -> bool:
        return self.queue1.empty()