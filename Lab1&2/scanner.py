import re

from codesTable import *


def isOperator(char):
    for operator in op:
        if char in operator:
            return True
    return False


def isQuote(line, index):
    return False if index == 0 else line[index - 1] == '\\'


def getStringToken(line, index):
    token = ''
    quote = 0

    while index < len(line) and quote < 2:
        if line[index] == '"' and not isQuote(line, index):
            quote += 1
        token += line[index]
        index += 1

    return token, index


def getOperatorToken(line, index):
    token = ''

    while index < len(line) and isOperator(line[index]):
        token += line[index]
        index += 1

    return token, index


def tokenGenerator(line, separators):
    token = ''
    index = 0

    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = getStringToken(line, index)
            yield token
            token = ''

        elif isOperator(line[index]):
            if token:
                yield token
            token, index = getOperatorToken(line, index)
            yield token
            token = ''

        elif line[index] in separators:
            if token:
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''

        else:
            token += line[index]
            index += 1
    if token:
        yield token


def isId(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,7}$', token) is not None


def isConst(token):
    return re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token) is not None
