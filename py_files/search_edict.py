import os
import codecs


def search_edict():
    inp = input('Search Japanese: ')

    # open file, get the data
    file = codecs.open('{}/{}'.format(os.getcwd(), 'edict.txt'), 'r', 'EUC-JP')
    text = file.read()
    file.close()

    # every other new line in the data is a new element of the joyo dictionary we will create
    outp = []
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = {'japanese': lines[i].split(' /')[0], 'english': lines[i].split(' /')[1:]}
        if inp in lines[i]['japanese']:
            outp += [lines[i]]

    return outp
