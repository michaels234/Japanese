import os
import codecs
from py_files.convert_to_hiragana import *


def get_joyo(kana):
    """

    gets joyo info from data, including the kanji, the grade of the kanji, the english equivalent, and all the readings
    for the kanji

    Args:
        kana (dict): kana dictionary. has the form kana['hiragana'/'katakana'/'kana'/'romaji'][i] for i kana

    Returns:
        joyo (dict): joyo kanji info dictionary. has the form joyo['kanji'/'grade'/'english'/'readings'][i] for i kanji

    """

    # open file, get the data
    file = codecs.open('{}/{}'.format(os.getcwd(), 'Joyo Kanji.txt'), 'r', 'UTF-8')
    text = file.read()
    file.close()

    # every other new line in the data is a new element of the joyo dictionary we will create
    lines = text.split('\n')

    # every other line in the data will be a joyo kanji, so make joyo['kanji'] an array of an number_of_lines/2 of 0s,
    # to be overwritten soon with kanji
    number_of_lines = len(lines)
    number_of_joyo_kanji = int(number_of_lines / 2)
    joyo = dict()
    joyo['kanji'], joyo['grade'], joyo['english'], joyo['readings'] = [], [], [], []

    for i in range(number_of_joyo_kanji):

        # j will be the element number for each line
        j = i * 2

        # split lines data by tabs separate the data into its respective types
        lines[j] = lines[j].split('\t')

        # theres some kind of hidden return mark which is \xa0 that we want to remove
        joyo['kanji'] += [lines[j][0].split('\xa0')[0]]
        joyo['grade'] += [lines[j][4]]
        joyo['english'] += [lines[j][6]]
        joyo['readings'] += [lines[j][7]]

    # separate readings into an array for each i kanji, remove unwanted characters from the readings, and directly
    # connect the kanji to each reading
    for i in range(number_of_joyo_kanji):

        # separate this kanji's readings text by '、'. now joyo['readings'][i] is an array of readings
        joyo['readings'][i] = joyo['readings'][i].split('、')

        # the joyo readings now has the form joyo['readings'][i][j], each i kanji has j readings
        number_of_readings_for_this_kanji = len(joyo['readings'][i])

        # the last reading for this kanji, reset it to the same thing but without the \r return code that is hiding
        joyo['readings'][i][number_of_readings_for_this_kanji - 1] \
            = joyo['readings'][i][number_of_readings_for_this_kanji - 1].split('\r')[0]

        # now each reading has been separated from each other. but some have some other unwanted characters, lets deal
        # with them. go through all the readings for this i kanji
        for j in range(number_of_readings_for_this_kanji):
            if '[' in joyo['readings'][i][j]:

                # in any reading we only need whats before the [ if there is one, leave out everything from [ onward
                joyo['readings'][i][j] = joyo['readings'][i][j].split('[')[0]

            # get the reading from within the （）, so leave out the first and last characters for this reading
            if '（' in joyo['readings'][i][j]:
                number_of_characters_in_this_reading = len(joyo['readings'][i][j])
                joyo['readings'][i][j] = joyo['readings'][i][j][1:number_of_characters_in_this_reading - 1]

            # at the end, i want each reading to be connected directly with their kanji, so a reading looks like
            # 円エン. it'll make things easier later
            joyo['readings'][i][j] = joyo['kanji'][i] + joyo['readings'][i][j]

    # change all verb readings to have the same form, the base form (remove a removable ru or conjugate any u ending
    # into an i ending). check each i kanji
    for i in range(number_of_joyo_kanji):

        # and each j reading for that kanji
        for j in range(len(joyo['readings'][i])):

            # if theres a '-' that means its a verb reading
            if '-' in joyo['readings'][i][j]:
                hyphen_index = joyo['readings'][i][j].index('-')

                # remove the '-'
                joyo['readings'][i][j] = joyo['readings'][i][j].replace('-', '')

                # get the last character, which is what gets conjugated or maybe already was conjugated
                reading_length = len(joyo['readings'][i][j])
                last_char = joyo['readings'][i][j][reading_length-1]

                # get the index that this hiragana is in the kana dict
                hiragana_index = kana['hiragana'].index(last_char)

                # this determines that the last character ends with an 'u' (this includes ku, ru, etc.), so it has not
                # been conjugated to the base form yet. note we will keep the unconjugated and add the conjugated form
                if hiragana_index % 5 == 2:

                    # so we will conjugate to the base (remove a removable ru, or change the last u to an i, like ku to
                    # ki). readings that have more than 1 hiragana after the hyphen have the ru removed when conjugated,
                    # like ta-beru. remove last character
                    if len(joyo['readings'][i][j][hyphen_index:]) > 1 and last_char == 'る':
                        joyo['readings'][i] += [joyo['readings'][i][j][:reading_length-1]]

                    # otherwise the last character needs to be replaced with the 'i' equivalent of the hiragana
                    else:
                        joyo['readings'][i] += [joyo['readings'][i][j][:reading_length-1]
                                                + kana['hiragana'][hiragana_index - 1]]

                # if the last character didn't end with a 'u', then it was already conjugated to its base
                # TODO: need to check for duplicate readings

    # separate readings into onyomi or kunyomi for each i kanji
    for i in range(number_of_joyo_kanji):

        # replace the current readings array with a dictionary, where onyomi, kunyomi, and all, each have an array
        joyo['readings'][i] = {'onyomi': [], 'kunyomi': [], 'all': joyo['readings'][i]}

        # check if each j reading is onyomi or kunyomi, and add them to the new kunyomi array or onyomi array
        # the form of joyo['readings'] is joyo['readings'][i]['onyomi'/'kunyomi'/'all'][j] for i kanji's j reading
        for j in range(len(joyo['readings'][i]['all'])):
            if joyo['readings'][i]['all'][j][1] in kana['katakana']:
                joyo['readings'][i]['onyomi'] += [
                    f"{joyo['readings'][i]['all'][j][0]}{convert_to_hiragana(joyo['readings'][i]['all'][j][1:], kana)}"]
                joyo['readings'][i]['all'][j] = f"{joyo['readings'][i]['all'][j][0]}" \
                                                f"{convert_to_hiragana(joyo['readings'][i]['all'][j][1:], kana)}"
            elif joyo['readings'][i]['all'][j][1] in kana['hiragana']:
                joyo['readings'][i]['kunyomi'] += [joyo['readings'][i]['all'][j]]

    return joyo


def test_get_joyo_kanji():

    print('test_get_joyo_kanji...')

    kana = get_kana()
    joyo = get_joyo(kana)
    num = 163  # line 327: 牙 [5]		牙	4	S	2010	tusk	ガ、（ゲ）、きば
    assert joyo['kanji'][num] == '牙' and joyo['grade'][num] == 'S' and joyo['english'][num] == 'tusk' and \
        joyo['readings'][num] == {'onyomi': ['牙が', '牙げ'], 'kunyomi': ['牙きば'], 'all': ['牙が', '牙げ', '牙きば']}, \
        f"{joyo['kanji'][num]}||{joyo['grade'][num]}||{joyo['english'][num]}||{joyo['readings'][num]} != " \
        f"牙||S||tusk||{{'onyomi': ['牙が', '牙げ'], 'kunyomi': ['牙きば'], 'all': ['牙が', '牙げ', '牙きば']}}"

    num = 172  # line 345: 回		囗	6	2		times	カイ、（エ）、まわ-る、まわ-す
    assert joyo['kanji'][num] == '回' and joyo['grade'][num] == '2' and joyo['english'][num] == 'times' and \
        joyo['readings'][num] == {'onyomi': ['回かい', '回え'], 'kunyomi': ['回まわる', '回まわす', '回まわり', '回まわし'],
                                  'all': ['回かい', '回え', '回まわる', '回まわす', '回まわり', '回まわし']}, \
        f"{joyo['kanji'][num]}||{joyo['grade'][num]}||{joyo['english'][num]}||{joyo['readings'][num]} != " \
        f"回||2||times||{{'onyomi': ['回かい', '回え'], 'kunyomi': ['回まわる', '回まわす', '回まわり', '回まわし'], " \
        f"'all': ['回かい', '回え', '回まわる', '回まわす', '回まわり', '回まわし']}}"

    num = 176  # line 353: 戒		戈	7	S		commandment	カイ、いまし-める
    assert joyo['kanji'][num] == '戒' and joyo['grade'][num] == 'S' and joyo['english'][num] == 'commandment' and \
        joyo['readings'][num] == {'onyomi': ['戒かい'], 'kunyomi': ['戒いましめる', '戒いましめ'],
                                  'all': ['戒かい', '戒いましめる', '戒いましめ']}, \
        f"{joyo['kanji'][num]}||{joyo['grade'][num]}||{joyo['english'][num]}||{joyo['readings'][num]} != " \
        f"戒||S||commandment||{{'onyomi': ['戒かい'], 'kunyomi': ['戒いましめる', '戒いましめ'], " \
        f"'all': ['戒かい', '戒いましめる', '戒いましめ']}}"

    num = 180  # line 361: 悔	悔 [4]	心	9	S		repent	カイ、く-いる、く-やむ、くや-しい
    assert joyo['kanji'][num] == '悔' and joyo['grade'][num] == 'S' and joyo['english'][num] == 'repent' and \
        joyo['readings'][num] == {'onyomi': ['悔かい'], 'kunyomi': ['悔くいる', '悔くやむ', '悔くやしい', '悔くい', '悔くやみ'],
                                  'all': ['悔かい', '悔くいる', '悔くやむ', '悔くやしい', '悔くい', '悔くやみ']}, \
        f"{joyo['kanji'][num]}||{joyo['grade'][num]}||{joyo['english'][num]}||{joyo['readings'][num]} != " \
        f"悔||S||repent||{{'onyomi': ['悔かい'], 'kunyomi': ['悔くいる', '悔くやむ', '悔くやしい', '悔くい', '悔くやみ'], " \
        f"'all': ['悔かい', '悔くいる', '悔くやむ', '悔くやしい', '悔くい', '悔くやみ']}}"

    print('test_get_joyo_kanji - Passed')

    return
