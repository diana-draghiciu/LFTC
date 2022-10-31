# 2. Symbol Table (you need to implement the data structure and required operations) :
# d. hash table
from scanner import Scanner


class ST:
    def __init__(self):
        self.table = {}
        self.hashNr = 7

    def hashFunction(self, symbol):
        """
        Returns the hash for the hashtable for the given symbol
        :param symbol: represents the identifier's symbol
        :return: the hash
        """
        s = 0
        for elem in symbol:
            s += ord(elem)
        return s % self.hashNr

    def checkIfSymbolInST(self, symbol):
        """
        Checks if the given identifier's symbol already exists in the symbol table
        :param symbol: represents the identifier's symbol
        :return: True if the symbol is found, False otherwise
        """
        poz = self.hashFunction(symbol)
        if poz in self.table.keys():
            for elem in self.table[poz]:
                if elem[0] == symbol:
                    return True
        return False

    def addToST(self, symbol, value):
        """
        Adds an identifier to the symbol table if it's symbol isn't already declared
        :param symbol: represents the identifier's symbol
        :param value: represents the identifier's value
        :return: -
        """
        poz = self.hashFunction(symbol)
        if poz not in self.table.keys():
            self.table[poz] = []

        if not self.checkIfSymbolInST(symbol):
            self.table[poz].append((symbol, value))

    def getValue(self, symbol):
        """
        Gets the value of the given identifier's symbol
        :param symbol: represents the identifier's symbol
        :return: the identifier's value
        """
        poz = self.hashFunction(symbol)
        for (x, y) in self.table[poz]:
            if x == symbol:
                return y

    # def setValue(self, symbol, value):
    #     poz = self.hashFunction(symbol)
    #     for (x, y) in self.table[poz]:
    #         if x == symbol:
    #             y=value
    #
    # def getSymbols(self, poz):
    #     result = []
    #     if poz in self.table.keys():
    #         for elem in self.table[poz]:
    #             result.append(elem[0])
    #     return result
