class Converter(object):
    def __init__(self, starting_symbol, non_terminals, terminals, productions):
        self.__starting_symbol = starting_symbol
        self.__non_terminals = non_terminals
        self.__terminals = terminals
        self.__productions = productions

    def getStartSymbol(self):
        return self.__starting_symbol

    def geNonTerminals(self):
        return self.__non_terminals

    def getTerminals(self):
        return self.__terminals

    def getProductions(self):
        return self.__productions

    def __str__(self):
        return '{}\n{}\n{}\n{}\n'.format(self.__starting_symbol, self.__non_terminals, self.__terminals, self.__productions)
