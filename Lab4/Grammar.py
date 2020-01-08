from FiniteAutomata import FiniteAutomata
from Transition import Transition


class GrammarException(Exception):
    def __init__(self, message):
        super(GrammarException, self).__init__(message)


class UnknownNonTerminal(GrammarException):
    pass


class UnknownTerminal(GrammarException):
    pass


class UnknownSymbol(GrammarException):
    pass


class Grammar(object):
    def __init__(self, file_name):
        self.__start_symbol = ""
        self.__non_terminals = []
        self.__terminals = []
        self.__rules = {}
        self.__file_name = file_name

    def readGrammarFromFile(self):
        with open(self.__file_name, 'r') as f:
            non_terminals = f.readline()
            non_terminals = non_terminals.strip('\n').split(',')
            self.__non_terminals.extend(non_terminals)

            terminals = f.readline()
            terminals = terminals.strip('\n').split(',')
            self.__terminals = terminals
            for nonTerminal in self.__non_terminals:
                self.__rules[nonTerminal] = []

            self.__start_symbol = f.readline().strip('\n')
            # read the remaining lines => the rules
            count = 1
            for line in f:
                rule_line = "".join(line.split()).strip('\n').split("->")
                non_terminal = rule_line[0]
                rules = rule_line[1].split('|')

                if not self.isNonTerminal(non_terminal):
                    raise UnknownNonTerminal("Unknown non-terminal " + non_terminal)
                self.validateRules(rules)
                rules.append(str(count))
                count += 1
                self.__rules[non_terminal] = self.__rules[non_terminal] + rules

    def getStartSymbol(self):
        return self.__start_symbol

    def setStartSymbol(self, value):
        self.__start_symbol = value

    def getNonTerminals(self):
        return self.__non_terminals

    def setNonTerminals(self, value):
        self.__non_terminals = value

    def getTerminals(self):
        return self.__terminals

    def setTerminals(self, value):
        self.__rules = value

    def getRules(self):
        return self.__rules

    def setRules(self, value):
        self.__rules = value

    def getFileName(self):
        return self.__file_name

    def setFileName(self, value):
        self.__file_name = value

    def isNonTerminal(self, non_terminal):
        if non_terminal not in self.getNonTerminals():
            return False
        return True

    def isTerminal(self, terminal):
        if terminal not in self.getTerminals() and terminal != 'E':
            return False
        return True

    def validateRules(self, rules):
        for rule in rules:
            for symbol in rule:
                is_terminal = self.isTerminal(symbol)
                is_non_terminal = self.isNonTerminal(symbol)

                if not is_terminal and not is_non_terminal:
                    raise UnknownSymbol("Unknown symbol: " + symbol)

    def getProductionsForAGivenNonTerminal(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise UnknownNonTerminal("This is not a non-terminal")
        return self.__rules[nonTerminal]

    def isProductionRegular(self, production):
        if len(production) > 2:
            return False
        if len(production) == 1:
            if not self.isTerminal(production[0]):
                return False
            return True
        else:
            if not self.isTerminal(production[0]):
                return False
            if not self.isNonTerminal(production[1]):
                return False
            return True

    def isS_RHS(self):
        if 'E' in self.__rules[self.__start_symbol]:
            for key, value in self.__rules.items():
                for production in value:
                    if key != self.__start_symbol and self.__start_symbol in production:
                        return False
        return True

    def validate_production(self, productions):
        for production in productions:
            for symbol in production:
                is_terminal = self.isTerminal(symbol)
                is_non_terminal = self.isNonTerminal(symbol)

                if not is_terminal and not is_non_terminal:
                    raise UnknownSymbol("Unknown symbol: " + symbol)

    def isRegular(self):
        for key, value in self.__rules.items():
            for production in value:
                if not self.isProductionRegular(production):
                    return False
                if key != self.__start_symbol and production == 'E':
                    return False
        return self.isS_RHS()

