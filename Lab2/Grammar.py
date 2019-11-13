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

            self.__start_symbol = f.readline().strip('\n')

            # read the remaining lines => the rules
            for line in f:
                rule_line = "".join(line.split()).strip('\n').split("->")
                non_terminal = rule_line[0]
                rules = rule_line[1].split('|')

                if not self.isNonTerminal(non_terminal):
                    raise UnknownNonTerminal("Unknown non-terminal " + non_terminal)
                self.validateRules(rules)

                self.__rules[non_terminal] = rules

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

    def isNonTerminal(self, non_terminal):
        if non_terminal not in self.getNonTerminals():
            return False
        return True

    def isTerminal(self, terminal):
        if terminal not in self.getTerminals():
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

    def getFA(self):
        initial_state = self.__start_symbol
        alphabet = self.__terminals
        states = []
        final_states = []
        transitions = []

        for non_terminal, production in self.__rules.items():
            states.append(non_terminal)
            for prod in production:
                if len(prod) == 2:
                    transitions.append(Transition(non_terminal, prod[1], [prod[0]]).__str__())
                else:
                    if prod[0] == ' ' and self.__start_symbol not in final_states:
                        final_states.append(self.__start_symbol)
                        continue
                    if 'K' not in states:
                        states.append('K')
                    if 'K' not in final_states:
                        final_states.append('K')
                    transitions.append(Transition(non_terminal, 'K', [prod[0]]).__str__())

        fa = FiniteAutomata("")
        fa.setAlphabet(alphabet)
        fa.getFinalStates()
        fa.setStates(states)
        fa.setTransitions(transitions)
        fa.setInitState(initial_state)

        return fa.__str__()

