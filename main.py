import os
import codecs
import time
import math


def get_kana_sets():
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
                'ん']
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
                'ン', 'ー']
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
              'n']
    kana = {'hiragana': hiragana, 'katakana': katakana, 'kana': hiragana + katakana, 'romaji': romaji}
    return kana


def get_joyo_kanji():
    file = codecs.open('{}/{}'.format(os.getcwd(), 'Joyo Kanji.txt'), 'r', 'UTF-8')
    text = file.read()
    file.close()
    lines = text.split('\n')
    joyo = dict()
    joyo['kanji'] = [0] * int(len(lines) / 2)
    joyo['grade'], joyo['english'], joyo['readings'] = joyo['kanji'].copy(), joyo['kanji'].copy(), joyo['kanji'].copy()
    for i in range(0, len(lines), 2):
        j = int(i / 2)
        lines[i] = lines[i].split('\t')
        joyo['kanji'][j] = lines[i][0].split('\xa0')[0]
        joyo['grade'][j] = lines[i][4]
        joyo['english'][j] = lines[i][6]
        joyo['readings'][j] = lines[i][7]
    return joyo


def get_kyoiku_kanji(joyo, kana):
    file = codecs.open('{}/{}'.format(os.getcwd(), 'Kyoiku Kanji.txt'), 'r', 'UTF-8')
    text = file.read()
    file.close()
    kyoiku = dict()
    kyoiku['kanji'] = []
    for k in text:
        if k not in kyoiku['kanji']:
            kyoiku['kanji'] += [k]
    kyoiku['english'], kyoiku['readings'] = kyoiku['kanji'].copy(), kyoiku['kanji'].copy()
    for i in range(len(kyoiku['kanji'])):
        for j in range(len(joyo['kanji'])):
            if kyoiku['kanji'][i] == joyo['kanji'][j]:
                kyoiku['english'][i], kyoiku['readings'][i] = joyo['english'][j], joyo['readings'][j]
                break
    for i in range(len(kyoiku['readings'])):
        kyoiku['readings'][i] = kyoiku['readings'][i].split('、')
        kyoiku['readings'][i][len(kyoiku['readings'][i]) - 1] = kyoiku[
            'readings'][i][len(kyoiku['readings'][i]) - 1].split('\r')[0]
        for j in range(len(kyoiku['readings'][i])):
            if '[' in kyoiku['readings'][i][j]:
                kyoiku['readings'][i][j] = kyoiku['readings'][i][j].split('[')[0]
            if '（' in kyoiku['readings'][i][j]:
                kyoiku['readings'][i][j] = kyoiku['readings'][i][j][1:len(kyoiku['readings'][i][j]) - 1]
                kyoiku['readings'][i][j] = kyoiku['kanji'][i] + kyoiku['readings'][i][j]
    for i in range(len(kyoiku['readings'])):
        for j in range(len(kyoiku['readings'][i])):
            if '-' in kyoiku['readings'][i][j]:
                hyphen_index = kyoiku['readings'][i][j].index('-')
                last_char = kyoiku['readings'][i][j][len(kyoiku['readings'][i][j])-1]
                hiragana_index = kana['hiragana'].index(last_char)
                if hiragana_index % 5 == 2:
                    if len(kyoiku['readings'][i][j][hyphen_index+1:]) > 1 and last_char == 'る':
                        to_do = 'remove ru'
                    else:
                        to_do = 'change _u character to _i character'
                    kyoiku['readings'][i][j] = kyoiku['readings'][i][j].replace('-', '')
                    length = len(kyoiku['readings'][i][j])
                    if to_do == 'change _u character to _i character':
                        kyoiku['readings'][i] += [kyoiku['readings'][i][j][:length-1] +
                                                  kana['hiragana'][hiragana_index - 1]]
                    else:
                        kyoiku['readings'][i] += [kyoiku['readings'][i][j][:length-1]]
                else:
                    kyoiku['readings'][i][j] = kyoiku['readings'][i][j].replace('-', '')
    for i in range(len(kyoiku['readings'])):
        kyoiku['readings'][i] = [{'onyomi': [], 'kunyomi': [], 'all': kyoiku['readings'][i]}]
        for j in kyoiku['readings'][i]['all']:
            if kyoiku['readings'][i]['all'][j][1] in kana['katakana']:
                kyoiku['readings'][i]['onyomi'] += [kyoiku['readings'][i]['all'][j]]
            elif kyoiku['readings'][i]['all'][j][1] in kana['hiragana']:
                kyoiku['readings'][i]['kunyomi'] += [kyoiku['readings'][i]['all'][j]]
    return kyoiku


def gather_data():
    print('gather')
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


def katakana_hiragana_switcher(text, kana, to=''):
    for j in range(len(text)):
        if text in kana['katakana'] or to == 'hiragana':
            if to == 'hiragana' and text[j] not in kana['katakana']:
                continue
            index_j = kana['katakana'].index(kana[j])
            if text[j] != 'ー':
                text = text[:j] + kana['hiragana'][index_j] + text[j + 1:]
            else:
                index_jm1 = kana['hiragana'].index(text[j - 1])
                text = text[:j] + kana['hiragana'][index_jm1 % 5] + text[j + 1:]
        elif to == 'katakana':
            if to == 'katakana' and text[j] not in kana['hiragana']:
                continue
            index_j = kana['hiragana'].index(text[j])
            if text[j] != 'ー':
                text = text[:j] + kana['katakana'][index_j] + text[j + 1:]
            else:
                index_jm1 = kana['katakana'].index(text[j - 1])
                text = text[:j] + kana['katakana'][index_jm1 % 5] + text[j + 1:]
    return text


def manipulate_data(kana, kyoiku, words):
    print('Manipulate...')

    """ Check for mismatched number of japanese, english, furigana arrays """
    # get elements_j, the number of elements in japanese list
    elements_j = len(words['japanese'])
    # assert that the numbers of elements in furigana and english lists are also  equal to elements_j
    assert elements_j == len(words['furigana']), 'Error in numbers of items in lists'
    assert elements_j == len(words['english']), 'Error in numbers of items in lists'

    for i in range(elements_j):  # get rid of () and ~ in furigana
        if '（' in words['furigana'][i]:
            words['furigana'][i] = ''
        if '~' in words['furigana'][i]:
            words['furigana'][i] = words['furigana'][i].replace('~', '')
    """ get words with same furigana and makes kanji list """
    for i in range(elements_j):  # loop through all the words
        # for j in range(i + 1, i + 1 + number):
        #     if j > number - 1:  # resets j to 0 if it goes past the last word in the list
        #         j -= number
        count = -1
        """ get words with same furigana """
        for j in range(elements_j):  # 2nd loop through all the words
            if i == j:
                continue
            if words['furigana'][i] == words['furigana'][j]:  # checks for words_with_same_furigana
                count += 1
                words[f'same furigana {count} japanese'][i] = words['japanese'][j]
                words[f'same furigana {count} english'][i] = words['english'][j]
        words['kanji'][i] = []
        """ make kanji list """
        for k in words['japanese'][i]:
            if k not in ['', '~', '(', ')', '/', '='] and k not in kana['kana']:  # if character k is a kanji
                words['kanji'][i] += [{'kanji': k}]  # adds k to kanji list
                index_kanji = len(words["kanji"][i]) - 1  # gets index of current kanji in kanji list
                if k in kyoiku['kanji']:  # if kanji k is a kyoiku kanji
                    kyoiku_index = kyoiku['kanji'].index(k)  # gets index of current kanji in kyoiku list
                    words['kanji'][i][index_kanji]['english'] = kyoiku['english'][kyoiku_index]  # inserts english
                    for m in kyoiku['readings'][kyoiku_index]['all']:  # loops through all joyo readings for this kanji
                        if katakana_hiragana_switcher(m[1:], kana, to='hiragana') in words['furigana'][i]:
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
                    if katakana_hiragana_switcher(m[1:], katakana, hiragana, to='hiragana') in furigana[i]:
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


def main():
    test = 0
    if test == 1:
        1
    else:
        start_time = time.time()
        kana = get_kana_sets()
        joyo = get_joyo_kanji()
        kyoiku = get_kyoiku_kanji(joyo)
        words = gather_data()
        words_with_same_furigana, words_with_same_kanji, all_kanji = manipulate_data(kana, kyoiku, words)
        file = codecs.open('{}/{}'.format(os.getcwd(), 'all_kanji.txt'), 'w', 'UTF-8')
        for k in all_kanji:
            file.write('{}'.format(k))
        file.close()
        print_cards_txt(furigana, japanese, english, words_with_same_furigana, words_with_same_kanji)
        total_time = time.time() - start_time
        # count = 0
        # for k in all_kanji:
        #     if k not in kyoiku_kanji:
        #         count += 1
        #         print(count, k)

        # print(all_kanji)
        print('Total Kanji: {}'.format(len(all_kanji)))
        print('Time: {}m　{}s'.format(math.floor(total_time/60), math.floor(total_time-math.floor(total_time/60)*60)))


main()
