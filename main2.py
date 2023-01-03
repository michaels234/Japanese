import time
import math
from py_files.convert_to_hiragana import convert_to_hiragana, test_convert_to_hiragana
from py_files.get_joyo import get_joyo, test_get_joyo
from py_files.get_kana import get_kana
from py_files.get_kyoiku import get_kyoiku
from py_files.search_edict import search_edict
import os
import codecs


def main():

    # get starting time in order to get total time spent running at the end
    start_time = time.time()

    # set test = 1 if you want to run a test. set to anything else if you want to run the main code
    test = 1

    # test code
    if test == 1:
        print('test...')
        test_convert_to_hiragana()
        #database()
        test_get_joyo()
        outp = search_edict()
        for item in outp:
            print(f"{item['japanese']} : {item['english']}")

    # main code
    else:

        # get the kana dictionary. has the form kana['hiragana'/'katakana'/'kana'/'romaji'][i] for i kana
        kana = get_kana()

        # get the joyo info dictionary. has the form joyo['kanji'/'grade'/'english'/'readings'][i] for i kanji
        joyo = get_joyo(kana)

        # get the kyoiku kyoiku kanji info dictionary. has the form kyoiku['kanji'/'english'][i] for i kanji or english,
        # or kyoiku['readings'] is kyoiku['readings'][i]['onyomi'/'kunyomi'/'all'][j] for i kanji's j reading
        kyoiku = get_kyoiku(joyo)

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

        # count = 0
        # for k in all_kanji:
        #     if k not in kyoiku_kanji:
        #         count += 1
        #         print(count, k)

        # print(all_kanji)
        # print('Total Kanji: {}'.format(len(all_kanji)))

    total_time = time.time() - start_time
    print('Time: {}m　{}s'.format(math.floor(total_time/60), math.floor(total_time-math.floor(total_time/60)*60)))


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
                        if convert_to_hiragana(m[1:], kana) in words['furigana'][i]:
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
                    if convert_to_hiragana(m[1:], katakana, hiragana, to='hiragana') in furigana[i]:
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
