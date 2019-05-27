class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry (data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s=0
        for i in range(1, len(self.qlist)):
           if A[i].priority < A[s].priority:
               s = i
        hasil = self.qlist.pop(s)
        return hasil.item

class _PriorityQEntry():
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

p = PriorityQueue()
p.enqueue("Angieta", 1)
p.enqueue("Putri", 3)
p.enqueue("Wahendra", 4)
p.enqueue("Keyla",2)

print(p.dequeue())
print(p.dequeue())
print(p.dequeue())
print(p.dequeue())
