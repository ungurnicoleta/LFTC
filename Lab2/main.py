from MenuFiniteAutomata import MenuFiniteAutomata
from MenuGrammar import MenuGrammar


def startMenu():
    myMenu = {
        '1': "1. Reads a grammar from file",
        '2': "2. Reads a FA from file"
    }

    for value in myMenu.values():
        print(value)


if __name__ == '__main__':
    startMenu()

    cmd = int(input("Choose a command: "))
    if cmd == 1:
        mg = MenuGrammar("grammar.in")
        mg.run()
    if cmd == 2:
        mfa = MenuFiniteAutomata("automaton.in")
        mfa.run()
