from Converter import Converter
from Transition import Transition


class FAException(Exception):
    def __init__(self, message):
        super(FAException, self).__init__(message)


class UnknownNonTerminal(FAException):
    pass


class UnknownTerminal(FAException):
    pass


class UnknownSymbol(FAException):
    pass


class FiniteAutomata(object):
    def __init__(self, file_name):
        self.__init_state = ""
        self.__states = []
        self.__final_states = []
        self.__alphabet = []
        self.__transitions = []
        self.__file_name = file_name

    def _read_FA(self):
        with open(self.__file_name, 'r') as f:
            # read first line => the initial state
            initial_state = f.readline()
            initial_state = initial_state.strip('\n').split(',')
            self.__init_state = initial_state

            # read second line => the states
            states = f.readline()
            states = states.strip('\n').split(',')
            self.__states.extend(states)

            # read third line => the final states
            final_states = f.readline()
            final_states = final_states.strip('\n').split(',')
            self.__final_states.extend(final_states)

            # read fourth line => the alphabet
            alphabet = f.readline()
            alphabet = alphabet.strip('\n').split(',')
            self.__alphabet.extend(alphabet)

            # read the remaining lines => the transitions
            for line in f:
                transition_line = line.strip('\n').split(',')
                print(transition_line[0]+  " " +  transition_line[1] + " " + transition_line[2:].__str__())
                if transition_line[0] and transition_line[1] not in self.__states:
                    raise UnknownSymbol("Check the transition to be correct!!!")
                self.__transitions.append(Transition(transition_line[0], transition_line[1], transition_line[2:]))

    def readFAFromFile(self):
        self._read_FA()

    def getInitState(self):
        return self.__init_state

    def setInitState(self, value):
        self.__init_state = value

    def getStates(self):
        return self.__states

    def setStates(self, value):
        self.__states = value

    def getFinalStates(self):
        return self.__final_states

    def setFinalStates(self, value):
        self.__final_states = value

    def getAlphabet(self):
        return self.__alphabet

    def setAlphabet(self, value):
        self.__alphabet = value

    def getTransitions(self):
        return self.__transitions

    def setTransitions(self, value):
        self.__transitions = value

    def getFileName(self):
        return self.__file_name

    def setFileName(self, value):
        self.__file_name = value

    def __str__(self):
        return '{}\n{}\n{}\n{}\n{}\n'.format(self.__init_state, self.__states, self.__final_states,
                                         self.__alphabet, self.__transitions)

    def getGrammar(self):
        starting_symbol = self.__init_state
        non_terminals = self.__states
        terminals = self.__alphabet
        rules = {}

        for transition in self.__transitions:
            rules[transition.getFirstState()] = []

        for transition in self.__transitions:
            for symbol in transition.getValues():
                if transition.getSecondState() not in self.__final_states:
                    string = symbol + transition.getSecondState()
                    rules[transition.getFirstState()].append(string)
                else:
                    string = symbol + transition.getSecondState()
                    rules[transition.getFirstState()].append(string)
                    rules[transition.getFirstState()].append(symbol)
        if self.__init_state[0] in self.__final_states:
            rules[self.__init_state[0]].append(' ')

        return Converter(starting_symbol, non_terminals, terminals, rules).__str__()
