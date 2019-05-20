#no1
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty(), "Tidka bisa diintip. Stack kosong"
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty(), "Tidka bisa dipop dari Stack kosong"
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

def cetakHexa(d):
    f = Stack()
    if d == 0: f.push(0);
    while d != 0:
        sisa = d%16
        d = d//16
        if sisa == 10:
            sisa = "A"
        elif sisa == 11:
            sisa = "B"
        elif sisa == 12:
            sisa = "C"
        elif sisa == 13:
            sisa = "D"
        elif sisa == 14:
            sisa = "E"
        elif sisa == 15:
            sisa = "F"
        f.push(sisa)
    st = ""
    for i in range (len(f)):
        st = st + str(f.pop())
    return st

#no2
nilai = Stack() #membuat objek baru dari class Stack dengan nama nilai
for i in range (16): # melakukan perulangan dengan range 0 - 16
    if i % 3 == 0: #jika i mod 3 hasilnya 0 maka
        nilai.push(i) # tambahkan nilai i pada object nilai

#no3
nilai = Stack() #membuat objek baru dari class Stack dengan nama nilai
for i in range (16): # melakukan perulangan dengan range 0 - 16
    if i % 3 == 0: #jika i mod 3 hasilnya 0 maka
        nilai.push(i) # tambahkan nilai i pada object nilai
    elif i % 4 == 0: #jika i mod 4 hasilnya 0 maka
        nilai.pop()# keluarkan nilai yang bila di mod 4 sisa nya 0.
