from PIF_Item import PIF
from SymbolTable import ST
from scanner import tokenGenerator, isConst, isId
from codesTable import *

if __name__ == "__main__":
    fileName = input("Insert file name: ")

    file = open(fileName, 'r')
    for line in file:
        print(line)

    with open(fileName, 'r') as file:
        for line in file:
            print([token for token in tokenGenerator(line, sep)])

    symbolTable = ST()
    pif = PIF()

    with open(fileName, 'r') as file:
        lineNo = 0
        for line in file:
            lineNo += 1
            for token in tokenGenerator(line[0:-1], sep):
                if token == " ":
                    continue
                elif token in sep + reservedWords + op:
                    pif.add(codes[token], -1)
                elif isId(token):
                    id = symbolTable.add(token)
                    pif.add(codes['identifier'], id)
                elif isConst(token):
                    id = symbolTable.add(token)
                    pif.add(codes['constant'], id)
                else:
                    raise Exception('Unknown token ' + token + ' at line ' + str(lineNo))

    print('Program Internal Form: \n', pif)
    print('Symbol Table: \n')
    symbolTable.print()

    # print('\n\nCodification table: ')
    # for e in codes:
    #     print(e, " -> ", codes[e])



