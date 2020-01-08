from Grammar import Grammar


class MenuGrammar(object):
    def __init__(self, file_name):
        self.__file_name = file_name

    def printMenuGrammar(self):
        menuGrammar = {
            '1': 'Get the set of non-terminals',
            '2': 'Get the set of terminals',
            '3': 'Get the starting symbol',
            '4': 'Get set of productions',
            '5': 'Get the productions of a given non-terminal symbol',
        }
        for key, val in menuGrammar.items():
            print('\t' + key + " " + val)

    def run(self):
        gr = Grammar(self.__file_name)
        gr.readGrammarFromFile()
        while True:
            self.printMenuGrammar()
            cmd = int(input("\tChoose a command: "))
            if cmd == 1:
                print(gr.getNonTerminals())
            if cmd == 2:
                print(gr.getTerminals())
            if cmd == 3:
                print(gr.getStartSymbol())
            if cmd == 4:
                print(gr.getRules())
            if cmd == 5:
                cmd2 = input("Choose non-terminal: ")
                print(gr.getProductionsForAGivenNonTerminal(cmd2))
            if cmd > 5 or cmd < 0:
                print("Choose a valid command: ")
            if cmd == 0:
                return
