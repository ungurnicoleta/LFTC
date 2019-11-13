class Transition(object):
    def __init__(self, first_state, second_state, values):
        self.__first_state = first_state
        self.__second_state = second_state
        self.__values = values

    def getFirstState(self):
        return self.__first_state

    def getSecondState(self):
        return self.__second_state

    def getValues(self):
        return self.__values

    def __str__(self):
        return '({},{})={})'.format(self.__first_state, ''.join([str(s) for s in self.__values]),
                                    self.__second_state)
