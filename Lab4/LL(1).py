from Grammar import Grammar


class LL1:
    def __init__(self):
        self.__grammar = Grammar("grammar2")
        self.__LL1Table = {}
        self.__first = {}
        self.__FIRST = {}
        self.__follow = {}
        self.__FOLLOW = {}

    def getRules(self):
        return self.__grammar.getRules()

    def firstFunction(self):
        nonTerminals = self.__grammar.getNonTerminals()
        rules = self.__grammar.getRules()
        i = 0
        for nt in nonTerminals:
            self.__first[nt] = [[]] * 10
        for nt in nonTerminals:
            for j in range(0, len(rules[nt]), 2):
                myRules = []
                if self.__grammar.isTerminal(rules[nt][j][0]):
                    myRules.append(rules[nt][j][0])
                    self.__first[nt][i] = self.__first[nt][i] + myRules
        i += 1
        while i < 10:
            for nt in nonTerminals:
                for j in range(0, len(rules[nt]), 2):
                    myRules = []
                    if self.__grammar.isTerminal(rules[nt][j][0]):
                        myRules.append(rules[nt][j][0])
                        self.__first[nt][i] = self.__first[nt][i] + myRules
                    else:
                        self.__first[nt][i] = self.__first[nt][i] + self.__first[rules[nt][j][0]][i - 1]
            i += 1
        for nt in nonTerminals:
            self.__FIRST[nt] = self.__first[nt][i - 1]
        return self.__FIRST

    def followFunction(self, ):
        nonTerminals = self.__grammar.getNonTerminals()
        i = 0
        for nt in nonTerminals:
            self.__follow[nt] = [[]]
            if nt == self.__grammar.getStartSymbol():
                self.__follow[self.__grammar.getStartSymbol()][0].append('E')
            self.__follow[nt].append([])

        i += 1
        while i < 10:
            for nt in nonTerminals:
                for key, val in self.__grammar.getRules().items():
                    myRules = self.__follow[nt][i - 1]
                    for elem in val:
                        index = elem.find(nt)

                        if index == len(elem) - 1:
                            for elemIJ in self.__follow[key][i - 1]:
                                if elemIJ not in myRules:
                                    myRules.append(elemIJ)

                        if index + 1 != len(elem) and index >= 0 and \
                                elem[index + 1] not in myRules:

                            if self.__grammar.isTerminal(elem[index + 1]):
                                myRules.append(elem[index + 1])

                            elif self.__grammar.isNonTerminal(elem[index + 1]):
                                first = self.__FIRST[elem[index + 1]]

                                for firstFromNT in first:
                                    if firstFromNT != 'E' and firstFromNT not in myRules:
                                        myRules.append(firstFromNT)

                                    if firstFromNT == 'E' and firstFromNT not in myRules:
                                        for elemI in self.__follow[key][i - 1]:
                                            myRules.append(elemI)
                self.__follow[nt][i] = self.__follow[nt][i] + myRules
                self.__follow[nt].append([])
            i += 1
        for key, val in self.__follow.items():
            self.__FOLLOW[key] = self.__follow[key][0]
        return self.__FOLLOW

    def getTable(self):
        self.__grammar.readGrammarFromFile()
        FIRST = self.firstFunction()
        FOLLOW = self.followFunction()
        RULES = self.__grammar.getRules()
        for term in self.__grammar.getTerminals():
            for nonTerm in self.__grammar.getNonTerminals():
                self.__LL1Table[(nonTerm, term)] = ["err", '-2']
            for term2 in self.__grammar.getTerminals():
                self.__LL1Table[(term2, term)] = ["err", '-2']
                if term == term2 and term != '$':
                    self.__LL1Table[(term2, term)] = ["POP", '-1']
                if term == term2 and term == '$':
                    self.__LL1Table[(term2, term)] = ["ACC", '-1']
        for NT, listOfFirst in FIRST.items():
            for elem in listOfFirst:
                if elem != 'E':
                    if len(RULES[NT]) == 2:
                        self.__LL1Table[(NT, elem)] = RULES[NT]
                    else:
                        for elemRULE in range(len(RULES[NT])):
                            if RULES[NT][elemRULE].find(elem) >= 0:
                                self.__LL1Table[(NT, elem)] = RULES[NT][elemRULE: elemRULE + 2]
                else:
                    follow = FOLLOW[NT]
                    for elemF in follow:
                        if elemF == 'E':
                            self.__LL1Table[(NT, '$')] = RULES[NT][-2:]
                        else:
                            self.__LL1Table[(NT, elemF)] = RULES[NT][-2:]
        return self.__LL1Table

    def LL1Algorithm(self, wordList):
        inputStack = ['$'] + wordList
        outputStack = ['$'] + [self.__grammar.getStartSymbol()]
        TABLE = self.getTable()
        pi = ""
        message = ""
        indexI = len(inputStack) - 1
        indexO = len(outputStack) - 1
        go = True

        while go:
            indexI = len(inputStack) - 1
            indexO = len(outputStack) - 1
            headAlpha = inputStack[indexI]
            headBeta = outputStack[indexO]
            if TABLE[(headBeta, headAlpha)][0] != 'POP' and TABLE[(headBeta, headAlpha)][0] != 'err' and \
                    TABLE[(headBeta, headAlpha)][0] != 'ACC' and TABLE[(headBeta, headAlpha)][0] != 'E':
                new = TABLE[(headBeta, headAlpha)][0]
                del outputStack[indexO]
                if len(new) > 1:
                    i = len(new) - 1
                    while i >= 0:
                        outputStack.append(new[i])
                        i -= 1
                else:
                    outputStack.append(new)
                pi = pi + TABLE[(headBeta, headAlpha)][1]
            elif TABLE[(headBeta, headAlpha)][0] == 'ACC':
                go = False
                message = "ACC"
            elif TABLE[(headBeta, headAlpha)][0] == 'E':
                del outputStack[indexO]
                pi = pi + TABLE[(headBeta, headAlpha)][1]
            else:
                if TABLE[(headBeta, headAlpha)][0] == 'POP':
                    del inputStack[indexI]
                    del outputStack[indexO]

        if message == "ACC":
            return pi
        else:
            return "ERROR"


if __name__ == '__main__':
    ll1 = LL1()
    ll1.getTable()
    print("\n\t***********FIRST*************\n")
    for key, val in ll1.firstFunction().items():
        print("\t" + str(key) + "  :  " + str(val) + '\n')

    print("\n\t***********FOLLOW*************\n")
    for key, val in ll1.followFunction().items():
        print("\t" + str(key) + "  :  " + str(val) + '\n')

    print("\n\t***********TABLE*************\n")
    for key, val in ll1.getTable().items():
        print("\t" + str(key) + " => " + str(val))

    print("\n\t***********RULES*************\n\n")
    for key, val in ll1.getRules().items():
        print("\t" + str(key) + " -> " + str(val))

    print("\n")
    word = "a * ( a + a )"
    wordList = word.split(" ")

    print("\t***********PI*************\n")
    print("\tPi is = " + ll1.LL1Algorithm(wordList[::-1]))
