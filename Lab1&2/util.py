import json


def get_file_iterator(filename):
    with open(filename) as f:
        lines = [line.strip('\n\t') for line in f.readlines()]
        return get_buffer_iterator(lines)


def get_buffer_iterator(lines):
    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            yield (i, j, character)


def load_json_data(filename):
    with open(filename) as f:
        data = json.load(f)

    return data


def print_tables(pif, identifiers, constants, codes):
    for pif_item in pif:
        code = pif_item.get_code()
        index = pif_item.get_symbol_table_index()
        if code == codes['constant']:
            print('{} - {}'.format(pif_item, constants.get(index)))
        elif code == codes['identifier']:
            print('{} - {}'.format(pif_item, identifiers.get(index)))
        else:
            print('{}'.format(pif_item))


def write_table(table, filename):
    with open(filename, 'w') as f:
        for item in table:
            f.write('{0} - {1}\n'.format(item[0], item[1]))
            f.write('\n')


def write_tokens(tokens, filename):
    with open(filename, 'w') as f:
        for token in tokens:
            f.write('{}: {}'.format(token.get_type(), token.get_normalized()))
