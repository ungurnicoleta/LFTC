from MenuFiniteAutomata import MenuFiniteAutomata
from MenuGrammar import MenuGrammar


def startMenu():
    myMenu = {
        '1': "1. Reads a grammar from file"
    }

    for value in myMenu.values():
        print(value)


if __name__ == '__main__':
    startMenu()
    mg = MenuGrammar("grammar2")
    mg.run()

