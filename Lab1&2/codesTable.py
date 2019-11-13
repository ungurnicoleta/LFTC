codes = {
    "identifier": 0,
    "constant": 1,
    "int": 2,
    "float": 3,
    "char": 4,
    "string": 5,
    "array": 6,
    "struct": 7,
    "scanf": 8,
    "printf": 9,
    "if": 10,
    "else": 11,
    "while": 12,
    "return": 13,
    ";": 14,
    "=": 15,
    "+": 16,
    "-": 17,
    "==": 18,
    "!=": 19,
    "<": 20,
    ">": 21,
    "<=": 22,
    ">=": 23,
    "/": 24,
    "*": 25,
    "%": 26,
    "]": 27,
    "[": 28,
    "{": 29,
    "}": 30,
    "(": 31,
    ")": 32,
    ".": 33,
    "\"": 34,
    "'": 35,
    ",": 36
}
op = ['+', '-', '*', '/', '%', '=', '++', '--', '<', '<=', '>', '>=']

sep = ['[', ']', '{', '}', ';', ':', ' ', '(', ')', ',', '\'', '.', "'"]

reservedWords = ['if',
                 'else',
                 'while',
                 'printf',
                 'scanf',
                 'return',
                 'then',
                 'write',
                 'char'
                 'bool',
                 'int',
                 'string',
                 'float',
                 'struct',
                 'array']

language = op + sep + reservedWords