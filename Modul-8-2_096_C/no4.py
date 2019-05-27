class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop()

    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[0]

    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[-1]


q = Queue()
q.enqueue(28)
q.enqueue(19)
q.enqueue(45)


print ("Item paling depan ", q.getFrontMost())
print ("Item paling belakang " , q.getRearMost())
