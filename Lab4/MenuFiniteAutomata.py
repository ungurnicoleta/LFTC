from FiniteAutomata import FiniteAutomata


class MenuFiniteAutomata(object):
    def __init__(self, file_name):
        self.__file_name = file_name

    def printMenuFA(self):
        menuGrammar = {
            '1': 'Get the initial state',
            '2': 'Get the set of states',
            '3': 'Get the set of finale states',
            '4': 'Get the alphabet',
            '5': 'Get the transitions',
            '6': 'Constructs the corresponding grammar'
        }
        for key, val in menuGrammar.items():
            print('\t' + key + " " + val)

    def run(self):
        fa = FiniteAutomata(self.__file_name)
        fa.readFAFromFile()
        while True:
            self.printMenuFA()
            cmd = int(input("\tChoose a command: "))
            if cmd == 1:
                print(fa.getInitState())
            if cmd == 2:
                print(fa.getStates())
            if cmd == 3:
                print(fa.getFinalStates())
            if cmd == 4:
                print(fa.getAlphabet())
            if cmd == 5:
                print(fa.getTransitions())
            if cmd == 6:
                print(fa.getGrammar())
            if cmd > 6 or cmd < 0:
                print("Choose a valid command: ")
            if cmd == 0:
                return
