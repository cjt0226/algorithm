class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.deque.__len__() < self.size:
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.deque.__len__() < self.size:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.deque.__len__ >= 1:
            self.deque = self.deque[1:self.size]
            return True
        return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deque.__len__() > 0:
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if self.deque.__len__() > 0:
            return self.deque[-1]
        return -1

    def isEmpty(self) -> bool:
        if self.deque.__len__() > 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.deque.__len__() == self.size:
            return True
        else:
            return False


circularDeque = MyCircularDeque(3);
circularDeque.insertLast(1);
circularDeque.insertLast(2);
circularDeque.insertFront(3);
circularDeque.insertFront(4);
circularDeque.getRear();
circularDeque.isFull();
circularDeque.deleteLast();
circularDeque.insertFront(4);
circularDeque.getFront();
