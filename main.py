import os
import codecs
import time
import math


def main():

    # set test = 1 if you want to run a test. set to anything else if you want to run the main code
    test = 1

    # test code
    if test == 1:
        print('TEST')
        test_to_hiragana()
        test_get_joyo_kanji()

    # main code
    else:

        # get starting time in order to get total time spent running at the end
        start_time = time.time()

        # get the kana dictionary. has the form kana['hiragana'/'katakana'/'kana'/'romaji'][i] for i kana
        kana = get_kana()

        # get the joyo info dictionary. has the form joyo['kanji'/'grade'/'english'/'readings'][i] for i kanji
        joyo = get_joyo(kana)

        # get the kyoiku kyoiku kanji info dictionary. has the form kyoiku['kanji'/'english'][i] for i kanji or english,
        # or kyoiku['readings'] is kyoiku['readings'][i]['onyomi'/'kunyomi'/'all'][j] for i kanji's j reading
        kyoiku = get_kyoiku_kanji(joyo)

        # words = get_n2_vocab()
        # words_with_same_furigana, words_with_same_kanji, all_kanji = manipulate_data(kana, kyoiku, words)
        # file = codecs.open('{}/{}'.format(os.getcwd(), 'all_kanji.txt'), 'w', 'UTF-8')
        # for k in all_kanji:
        #     file.write('{}'.format(k))
        # file.close()
        # print_cards_txt(furigana, japanese, english, words_with_same_furigana, words_with_same_kanji)

        # open file, get the data
        file = codecs.open('{}/{}'.format(os.getcwd(), 'edict.txt'), 'r', 'EUC-JP')
        text = file.read()
        file.close()
        # every other new line in the data is a new element of the joyo dictionary we will create
        lines = text.split('\n')
        print(lines[100])

        total_time = time.time() - start_time
        # count = 0
        # for k in all_kanji:
        #     if k not in kyoiku_kanji:
        #         count += 1
        #         print(count, k)

        # print(all_kanji)
        # print('Total Kanji: {}'.format(len(all_kanji)))
        print('Time: {}m　{}s'.format(math.floor(total_time/60), math.floor(total_time-math.floor(total_time/60)*60)))


def get_kana():
    """

    gets hiragana, katakana, kana (which is hiragana and katakana put together), and romaji and puts them into one
    dictionary

    Returns:
        kana (dict[str, list[str]]): kana dictionary. has the form kana['hiragana'/'katakana'/'kana'/'romaji'][i] for i
        kana

    """

    hiragana = ['あ', 'い', 'う', 'え', 'お',
                'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ',
                'か', 'き', 'く', 'け', 'こ',
                'が', 'ぎ', 'ぐ', 'げ', 'ご',
                'さ', 'し', 'す', 'せ', 'そ',
                'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
                'た', 'ち', 'つ', 'て', 'と',
                'だ', 'ぢ', 'づ', 'で', 'ど',
                '＃', '＃', 'っ', '＃', '＃',
                'な', 'に', 'ぬ', 'ね', 'の',
                'は', 'ひ', 'ふ', 'へ', 'ほ',
                'ば', 'び', 'ぶ', 'べ', 'ぼ',
                'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
                'ま', 'み', 'む', 'め', 'も',
                'や', '＃', 'ゆ', '＃', 'よ',
                'ゃ', '＃', 'ゅ', '＃', 'ょ',
                'ら', 'り', 'る', 'れ', 'ろ',
                'わ', '＃', '＃', '＃', 'を',
                'ん', '[dash]']

    katakana = ['ア', 'イ', 'ウ', 'エ', 'オ',
                'ァ', 'ィ', 'ゥ', 'ェ', 'ォ',
                'カ', 'キ', 'ク', 'ケ', 'コ',
                'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
                'サ', 'シ', 'ス', 'セ', 'ソ',
                'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
                'タ', 'チ', 'ツ', 'テ', 'ト',
                'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
                '＃', '＃', 'ッ', '＃', '＃',
                'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
                'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
                'バ', 'ビ', 'ブ', 'ベ', 'ボ',
                'パ', 'ピ', 'プ', 'ペ', 'ポ',
                'マ', 'ミ', 'ム', 'メ', 'モ',
                'ヤ', '＃', 'ユ', '＃', 'ヨ',
                'ャ', '＃', 'ュ', '＃', 'ョ',
                'ラ', 'リ', 'ル', 'レ', 'ロ',
                'ワ', '＃', '＃', '＃', 'ヲ',
                'ン', 'ー',
                ]

    romaji = ['a', 'i', 'u', 'e', 'o',
              'ka', 'ki', 'ku', 'ke', 'ko',
              'ga', 'gi', 'gu', 'ge', 'go',
              'sa', 'shi', 'su', 'se', 'so',
              'za', 'ji', 'zu', 'ze', 'zo',
              'ta', 'chi', 'tsu', 'te', 'to',
              'da', 'dji', 'dzu', 'de', 'do',
              '#', '#', '[double_consonant]', '#', '#',
              'na', 'ni', 'nu', 'ne', 'no',
              'ha', 'hi', 'fu', 'he', 'ho',
              'ba', 'bi', 'bu', 'be', 'bo',
              'pa', 'pi', 'pu', 'pe', 'po',
              'ma', 'mi', 'mu', 'me', 'mo',
              'ya', '#', 'yu', '#', 'yo',
              '[small_ya]', '#', '[small_yu]', '#', '[small_yo]',
              'ra', 'ri', 'ru', 're', 'ro',
              'wa', '#', '#', '#', 'wo',
              'n', '[dash]',
              ]

    kana = {'hiragana': hiragana, 'katakana': katakana, 'kana': hiragana + katakana, 'romaji': romaji}

    return kana


def to_hiragana(text, kana):

    # go through the text  to be switched for each character text[j]
    for k in text:

        # if character is already hiragana, skip do nothing, go to the next character
        if k in kana['katakana']:

            # katakana index and hiragana index line up, so get katakana index of this character, and use it in hiragana
            hiragana_index_of_k = kana['katakana'].index(k)
            text = text.replace(k, kana['hiragana'][hiragana_index_of_k])
    return text


def test_to_hiragana():

    print('test_to_hiragana...')

    hiragana_text1 = 'あいうえおふぁふぃとぅふぇふぉかきくけこがぎぐげごさあしいすうせいそうざじずぜぞたちつてっとおだぢづでどなにぬ' \
                     'ねのはひふへほばびゅぶべぼぱぴゃぷぺぽまみょむめもやゆよらりるれろわをん'
    hiragana_text2 = 'ねのはひふへほばびゅぶべぼぱぴゃぷぺぽまみょむめもやゆよらりるれろわをんじずぜぞたちつてっ' \
                     'あいうえおふぁふぃとぅふぇふぉかきくけこがぎぐげごさあしいすうせえそおざとうだぢづでどなにぬ'
    katakana_text1 = 'アイウエオファフィトゥフェフォカキクケコガギグゲゴサアシイスウセイソウザジズゼゾタチツテットオダヂヅデドナニヌ' \
                     'ネノハヒフヘホバビュブベボパピャプペポマミョムメモヤユヨラリルレロワヲン'
    katakana_text2 = 'ネノハヒフヘホバビュブベボパピャプペポマミョムメモヤユヨラリルレロワヲンジズゼゾタチツテッ' \
                     'アイウエオファフィトゥフェフォカキクケコガギグゲゴサアシイスウセエソオザトウダヂヅデドナニヌ'

    kana = get_kana()

    assert to_hiragana(hiragana_text1, kana) == hiragana_text1, \
        f"{to_hiragana(hiragana_text1, kana)} != {hiragana_text1}"
    assert to_hiragana(hiragana_text2, kana) == hiragana_text2, \
        f"{to_hiragana(hiragana_text2, kana)} != {hiragana_text2}"
    assert to_hiragana(katakana_text1, kana) == hiragana_text1, \
        f"{to_hiragana(katakana_text1, kana)} != {hiragana_text1}"
    assert to_hiragana(katakana_text2, kana) == hiragana_text2, \
        f"{to_hiragana(katakana_text2, kana)} != {hiragana_text2}"

    print('test_to_hiragana - Passed')

    return


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
                # been conjugated to the base form yet
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
                    f"{joyo['readings'][i]['all'][j][0]}{to_hiragana(joyo['readings'][i]['all'][j][1:], kana)}"]
                joyo['readings'][i]['all'][j] = f"{joyo['readings'][i]['all'][j][0]}" \
                                                f"{to_hiragana(joyo['readings'][i]['all'][j][1:], kana)}"
            elif joyo['readings'][i]['all'][j][1] in kana['hiragana']:
                joyo['readings'][i]['kunyomi'] += [joyo['readings'][i]['all'][j]]

    return joyo


def test_get_joyo_kanji():

    print('test_get_joyo_kanji...')

    kana = get_kana()
    joyo = get_joyo(kana)
    num = 163  # line 327: 牙 [5]		牙	4	S	2010	tusk	ガ、（ゲ）、きば
    print(joyo['readings'][num])
    assert joyo['kanji'][num] == '牙' and joyo['grade'][num] == 'S' and joyo['english'][num] == 'tusk' and \
        joyo['readings'][num] == {'onyomi': ['牙が', '牙げ'], 'kunyomi': ['牙きば'], 'all': ['牙が', '牙げ', '牙きば']}, \
        f"{joyo['kanji'][num]}||{joyo['grade'][num]}||{joyo['english'][num]}||{joyo['readings'][num]} != " \
        f"牙||S||tusk||{{'onyomi': ['牙が', '牙げ'], 'kunyomi': ['牙きば'], 'all': ['牙が', '牙げ', '牙きば']}}"

    return


def get_kyoiku_kanji(joyo):
    """

    gets kyoiku kanji from kyoiku kanji list,
    gets english and readings info for each kanji from the joyo kanji dict,
    separates readings into an array for each kanji, removes unwanted characters from the readings, and directly connects the kanji to each reading
    changes all verb readings to have the same form, the base form, which removes a removable ru or conjugates any u ending into an i ending
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

    # just for now to make the english and readings arrays and have the right number of elements, fill them with the kanji, to be replaced soon
    kyoiku['english'], kyoiku['readings'] = kyoiku['kanji'].copy(), kyoiku['kanji'].copy()

    # get english and readings for each i kyoiku kanji
    for i in range(number_of_kyoiku_kanji):

        # find the matching kanji in the joyo dict
        for j in range(joyo_item_number):
            if kyoiku['kanji'][i] == joyo['kanji'][j]:

                # once found, get the english and reading from the joyo and save it to the kyoiku dict too
                kyoiku['english'][i], kyoiku['readings'][i] = joyo['english'][j], joyo['readings'][j]

                # since you found the matching joyo kanji, you don't need to look through joyo anymore. next kyoiku kanji
                break
    return kyoiku


def get_n2_vocab():

    print('get_n2_vocab')

    words = {'japanese': [], 'furigana': [], 'english': []}
    # which = 0  # both lists
    which = 1  # list 1
    # which = 2  # list 2
    if which in [0, 1]:
        name = 'N2 Vocab List From jlptstudy.txt'
        file = codecs.open('{}/{}'.format(os.getcwd(), name), 'r', 'UTF-8')
        text = file.read()
        file.close()
        lines = text.split('\n')
        no_english = 0
        for line in lines:
            line = line.split('\t')
            words['furigana'] += [line[1]]
            if line[2] == '':
                words['japanese'] += [line[1]]
            else:
                words['japanese'] += [line[2]]
            line[4] = line[4].split('\r')
            if line[4][0] == '':
                print('No English: ', line[2], len(words['japanese']))
                no_english += 1
            words['english'] += [line[4][0]]
    if which in [0, 2]:
        name = 'N2 Vocab List From japanesetest4you.txt'
        file = codecs.open('{}/{}'.format(os.getcwd(), name), 'r', 'UTF-8')
        text = file.read()
        file.close()
        lines = text.split('\n')
        for line in lines:
            count2 = 0
            marker = 0
            for character in line:
                if character == ' ' and marker == 0:
                    if line[count2-1] == ':':
                        words['japanese'] += ['']
                        words['furigana'] += [line[:count2-1]]
                        words['english'] += [line[count2:]]
                        break
                    else:
                        words['japanese'] += [line[:count2]]
                        count2 += 2
                        marker = count2
                if character == ')':
                    words['furigana'] += [line[marker:count2]]
                    words['english'] += [line[count2+3:]]
                    break
                count2 += 1
    return words


def manipulate_data(kana, kyoiku, words):
    print('Manipulate...')

    """ Check for mismatched number of japanese, english, furigana arrays """
    # get elements_j, the number of elements in japanese list
    elements_j = len(words['japanese'])
    # assert that the numbers of elements in furigana and english lists are also equal to elements_j
    assert elements_j == len(words['furigana']), 'Error in numbers of items in lists'
    assert elements_j == len(words['english']), 'Error in numbers of items in lists'

    """ get words with same furigana and makes kanji list """
    # get rid of () and ~ in furigana
    for i in range(elements_j):
        if '（' in words['furigana'][i]:
            words['furigana'][i] = ''
        if '~' in words['furigana'][i]:
            words['furigana'][i] = words['furigana'][i].replace('~', '')
    # loop through all the words
    for i in range(elements_j):
        # # loop that resets j to 0 if it goes past the last word in the list
        # for j in range(i + 1, i + 1 + number):
        #     if j > number - 1:
        #         j -= number
        """ get words with same furigana """
        # initiate words['same furigana'][i] dictionary with empty lists
        words['same furigana'][i] = {'japanese': [], 'english': []}
        # 2nd loop through all the words
        for j in range(elements_j):
            # skip when j and i are the same
            if i == j:
                continue
            # get words with same furigana, get their japanese and english
            if words['furigana'][i] == words['furigana'][j]:
                words['same furigana'][i]['japanese'] += [words['japanese'][j]]
                words['same furigana'][i]['english'] += [words['english'][j]]
        """ make kanji list """
        # initiate words['kanji'][i] with an empty list
        words['kanji'][i] = []
        # loop through all the characters in words['japanese'][i]
        for k in words['japanese'][i]:
            # if character k is a kanji
            if k not in ['', '~', '(', ')', '/', '='] and k not in kana['kana']:
                # initialize dictionary for kanji list, and add kanji k to dictionary
                words['kanji'][i] += [{'kanji': k}]
                # get index of current kanji in kanji list
                index_kanji = len(words["kanji"][i]) - 1
                # if kanji k is a kyoiku kanji
                if k in kyoiku['kanji']:
                    # get index of kanji k in kyoiku list
                    kyoiku_index = kyoiku['kanji'].index(k)
                    # add the kanji's english to the kanji list dictionary
                    words['kanji'][i][index_kanji]['english'] = kyoiku['english'][kyoiku_index]
                    # loop through all the joyo readings for this kanji
                    for m in kyoiku['readings'][kyoiku_index]['all']:
                        # if joyo reading m is in the furigana for this i'th word, thats the reading for kanji k here
                        if to_hiragana(m[1:], kana) in words['furigana'][i]:
                            # finds the reading that this kanji has in this word
                            if m in kyoiku['readings'][kyoiku_index]['onyomi']:
                                which = 'onyomi'
                            elif m in kyoiku['readings'][kyoiku_index]['kunyomi']:
                                which = 'kunyomi'
                            else:
                                which = 'none'
                            words['kanji'][i][index_kanji]['reading'] = {'this reading': m, 'onyomi or kunyomi': which,
                                                                   'other readings': kyoiku['readings'][kyoiku_index]}

    kanji_reading = words['japanese'].copy()  # this loop gets the kanji_reading for each kanji in each word
    for i in range(elements_j):
        kanji_reading[i] = []
        for k in kanji[i]:
            if k in kyoiku_kanji:
                index_kanji = kyoiku_kanji.index(k)
                got_it = 0
                for m in kyoiku_readings[index_kanji]:
                    if to_hiragana(m[1:], katakana, hiragana, to='hiragana') in furigana[i]:
                        kanji_reading[i] += [m]
                        got_it = 1
                        break
                if got_it == 0:
                    kanji_reading[i] += ['S+']
            else:
                kanji_reading[i] += ['S+']

    # we have to go thru things like a-u and get rid of the hyphen in the reading, and also make another reading of ai
    words_with_same_kanji = japanese.copy()
    count = [{}] * elements_j
    for i in range(elements_j):  # this loop gets all the words_with_same_kanji
        words_with_same_kanji[i] = []
        for j in range(i + 1, i + 1 + elements_j - 1):  # this loops from the current i+1, back to 0 after number, until i-1
            if j > elements_j - 1:  # resets j to 0 if it goes past the last word in the list
                j -= elements_j
            for k in range(len(kanji[i])):
                count[i]['kanji_{}_onyomi'.format(k)] = 0
                count[i]['kanji_{}_kunyomi'.format(k)] = 0
                if kanji[i][k] in kanji[j]:
                    skip = 0
                    index = kanji[j].index(kanji[i][k])
                    for m in words_with_same_kanji[i]:
                        if kanji_reading[j][index] in m:
                            skip = 1
                    if skip == 0:
                        if kanji_reading[j][index] != 'S+':
                            words_with_same_kanji[i] += [[japanese[j], furigana[j], english[j],
                                                          kanji_reading[j][index]]]
                            if kanji_reading[j][index][1] in katakana:
                                count[i]['kanji_{}_onyomi'.format(k)] += 1
                            else:
                                count[i]['kanji_{}_kunyomi'.format(k)] += 1

    all_kanji = []
    for i in range(elements_j):  # this loop makes all_kanji list
        for k in kanji[i]:
            if k not in all_kanji:  # puts any kanji not already in all_kanji into the list
                all_kanji += [k]

    count = 0
    for k in kyoiku_kanji:  # this look finds the kyoiku kanji that aren't yet in our list, so we need words for them
        if k not in all_kanji:
            count += 1
            print(count, 'This kyoiku kanji is not in any word in the N2 list', k)

    # this is one of the k's in japanese[i], we want the english for this kanji and all the readings for it
    # do that here, and then in the next step we will search for words for each reading
    # heres the plan, we need to go thru all the japanese[i] first and give them kanji-readings
    # like [覚かく, 係けい], so then we know not just the kanji in each word but the specific reading of it
    # call it like kanjireading
    # then when we search for other words with the kanji we can easily check which reading of it it has
    # we can check if we have gone through all the readings by using things like
    # len(kyoiku_readings[i]) shows to total number of readings for the kanji
    # if kanjireading[i][j][1:] in kyoiku_readings[i]: count one for this kyoiku reading
    # note we have to be careful about hiragana, katakana. need like a quit translator function for that

    return words_with_same_furigana, words_with_same_kanji, all_kanji


def print_cards_txt(furigana, japanese, english, kanji, kanji_english, count, words_with_same_furigana, words_with_same_kanji):
    print('print')
    file = codecs.open('{}/{}'.format(os.getcwd(), 'N2_Anki_File.txt'), 'w', 'UTF-8')
    for i in range(len(japanese)):
        # <style>body{font-size:30px}table{font-size:20px}</style><center><body>furigana<br>english<br></body><table border = "1"><tr><td colspan = "2">kanji 1</td><td colspan = "2">kanji 2</td></tr><tr><td colspan = "2">kanji 1 english</td><td colspan = "2">kanji 2 english</td></tr><tr><td>onyomi 1</td><td>kunyomi 1</td><td>onyomi 2</td><td>kunyomi 2</td></tr><tr><td>word</td><td>word</td><td>word</td><td>word</td></tr><tr><td>reading</td><td>reading</td><td>reading</td><td>reading</td></tr><tr><td>english</td><td>english</td><td>english</td><td>english</td></tr></table></center>
        # <style>body{font-size:30px}table{font-size:20px}</style><center><body>furigana<br>english<br></body>
        # <table border = "1"><tr><td colspan = "2">kanji 1</td><td colspan = "2">kanji 2</td></tr><tr><td colspan = "2">kanji 1 english</td><td colspan = "2">kanji 2 english</td></tr><tr><td>onyomi 1</td><td>kunyomi 1</td><td>onyomi 2</td><td>kunyomi 2</td></tr><tr><td>word</td><td>word</td><td>word</td><td>word</td></tr><tr><td>reading</td><td>reading</td><td>reading</td><td>reading</td></tr><tr><td>english</td><td>english</td><td>english</td><td>english</td></tr></table></center>
        file.write('<style>body{{font-size:30px}}</style><center><body>{}</body>;'.format(japanese[i]))
        file.write('<style>body{{font-size:30px}}table{{font-size:20px}}</style><center><body>{}<br>{}<br></body>'.
                   format(furigana[i], english[i]))
        file.write('<table border = "1">')
        for j in range(6):
            file.write('<tr>')
            if j == 0:
                for k in range(len(kanji[i])):
                    file.write('<td colspan = "{}">{}</td>'.
                               format(count[i]['kanji_{}_onyomi'.format(k)] + count[i]['kanji_{}_kunyomi'.format(k)],
                                      kanji[i][k]))
            elif j == 1:
                for k in range(len(kanji[i])):
                    file.write('<td colspan = "{}">{}</td>'.
                               format(count[i]['kanji_{}_onyomi'.format(k)] + count[i]['kanji_{}_kunyomi'.format(k)],
                                      kanji_english[i][k]))
            elif j == 2:
                for k in range(len(kanji[i])):
                    for m in range(count[i]['kanji_{}_kunyomi'.format(k)]):
                        file.write('<td colspan = "{}">訓<br>{}</td>'.
                                   format(count[i]['kanji_{}_kunyomi'.format(k)], kanji[i][k]))
            file.write('</tr>')
        file.write('<table border = "1">')
    file.close()


main()
