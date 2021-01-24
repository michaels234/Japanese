import os
import codecs


def get_kyoiku(joyo):
    """

    gets kyoiku kanji from kyoiku kanji list,
    gets english and readings info for each kanji from the joyo kanji dict,
    separates readings into an array for each kanji, removes unwanted characters from the readings, and directly
        connects the kanji to each reading
    changes all verb readings to have the same form, the base form, which removes a removable ru or conjugates any u
        ending into an i ending
    separates readings into onyomi or kunyomi

    Args:
        joyo (dict): joyo kanji info dictionary

    Returns:
        kyoiku(dict): kyoiku kanji info dictionary. has the form kyoiku['kanji'/'english'][i] for i kanji or english,
            or kyoiku['readings'] is kyoiku['readings'][i]['onyomi'/'kunyomi'/'all'][j] for i kanji's j reading

    """

    print('get_kyoiku_kanji')

    # open file, get data
    file = codecs.open('{}/{}'.format(os.getcwd(), 'Kyoiku Kanji.txt'), 'r', 'UTF-8')
    text = file.read()
    file.close()
    kyoiku = dict()

    # start with empty array for kyoiku kanji
    kyoiku['kanji'] = []

    # separate all kyoiku kanji from the text data into separate elements and save to the kyoiku kanji array
    for k in text:
        if k not in kyoiku['kanji']:
            kyoiku['kanji'] += [k]
    number_of_kyoiku_kanji = len(kyoiku['kanji'])
    joyo_item_number = len(joyo['kanji'])

    # just for now to make the english and readings arrays and have the right number of elements, fill them with the
    # kanji, to be replaced soon
    kyoiku['english'], kyoiku['readings'] = kyoiku['kanji'].copy(), kyoiku['kanji'].copy()

    # get english and readings for each i kyoiku kanji
    for i in range(number_of_kyoiku_kanji):

        # find the matching kanji in the joyo dict
        for j in range(joyo_item_number):
            if kyoiku['kanji'][i] == joyo['kanji'][j]:

                # once found, get the english and reading from the joyo and save it to the kyoiku dict too
                kyoiku['english'][i], kyoiku['readings'][i] = joyo['english'][j], joyo['readings'][j]

                # since we found the matching joyo kanji, we don't need to look through joyo anymore. next kyoiku kanji
                break
    return kyoiku
