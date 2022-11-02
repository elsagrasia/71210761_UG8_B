from heapq import heappush


class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.d = -1

    def enqueue(self, data):
        if ((self.d + 1) % self.size == self.front):
            print("Antrian penuh")
        elif (self.front == -1):
            self.front = 0
            self.d = 0
            self.queue[self.d] = data
        else:
            self.d = (self.d + 1) % self.size
            self.queue[self.d] = data

    def dequeue(self):   
        if (self.front == self.d):
            hapus = self.queue[self.front]
            self.front = -1
            self.d = -1
            return hapus
        else:
            hapus = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return hapus

    def display(self):
        if  (self.d >= self.front):
            print("Yang ada pada antrian adalah:",
                  end=" ")
            for i in range(self.front, self.d + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            print("Yang ada pada antrian adalah:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.d + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.d + 1) % self.size == self.front):
            print("Antrian penuh")

CircularQueue = CircularQueue(5)
CircularQueue.enqueue(14)
CircularQueue.enqueue(22)
CircularQueue.enqueue(13)
CircularQueue.enqueue(-6)
CircularQueue.display()
print("Data yang dihapus adalah = ", CircularQueue.dequeue())
print("Data yang dihapus adalah = ", CircularQueue.dequeue())
CircularQueue.display()
CircularQueue.enqueue(9)
CircularQueue.enqueue(20)
CircularQueue.enqueue(5)
CircularQueue.display()