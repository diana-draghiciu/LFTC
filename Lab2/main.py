# 2. Symbol Table (you need to implement the data structure and required operations) :
# d. hash table

class ST:
    def __init__(self):
        self.table = {}
        self.hashNr = 7

    def hashFunction(self, symbol):
        s = 0
        for elem in symbol:
            s += ord(elem)
        return s % self.hashNr

    def checkIfSymbolInST(self, symbol):
        poz = self.hashFunction(symbol)
        for elem in self.table[poz]:
            if elem[0] == symbol:
                return True
        return False

    def addToST(self, symbol, value):
        poz = self.hashFunction(symbol)
        if poz not in self.table.keys():
            self.table[poz] = []

        if not self.checkIfSymbolInST(symbol):
            self.table[poz].append((symbol, value))

    def getValue(self, symbol):
        poz = self.hashFunction(symbol)
        for (x, y) in self.table[poz]:
            if x == symbol:
                return y


if __name__ == '__main__':
    st = ST()
    st.addToST('abc', 4)
    st.addToST('p', 5)
    st.addToST('efg', 5)
    st.addToST('abc', 3)
    print(st.table)  # {0: [('abc', 4), ('p', 5)], 5: [('efg', 5)]}
    print(st.getValue('abc'))  # 4
