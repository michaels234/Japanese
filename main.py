import os
import codecs
import time


def get_kana_sets():
    hiragana = ['あ', 'い', 'う', 'え', 'お',
                'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ',
                'か', 'き', 'く', 'け', 'こ',
                'が', 'ぎ', 'ぐ', 'げ', 'ご',
                'さ', 'し', 'す', 'せ', 'そ',
                'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
                'た', 'ち', 'つ', 'て', 'と',
                'だ', 'ぢ', 'づ', 'で', 'ど',
                'っ',
                'な', 'に', 'ぬ', 'ね', 'の',
                'は', 'ひ', 'ふ', 'へ', 'ほ',
                'ば', 'び', 'ぶ', 'べ', 'ぼ',
                'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
                'ま', 'み', 'む', 'め', 'も',
                'や', 'ゆ', 'よ',
                'ゃ', 'ゅ', 'ょ',
                'ら', 'り', 'る', 'れ', 'ろ',
                'わ', 'を', 'ん']
    katakana = ['ア', 'イ', 'ウ', 'エ', 'オ',
                'ァ', 'ィ', 'ゥ', 'ェ', 'ォ',
                'カ', 'キ', 'ク', 'ケ', 'コ',
                'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
                'サ', 'シ', 'ス', 'セ', 'ソ',
                'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
                'タ', 'チ', 'ツ', 'テ', 'ト',
                'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
                'ッ',
                'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
                'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
                'バ', 'ビ', 'ブ', 'ベ', 'ボ',
                'パ', 'ピ', 'プ', 'ペ', 'ポ',
                'マ', 'ミ', 'ム', 'メ', 'モ',
                'ヤ', 'ユ', 'ヨ',
                'ャ', 'ュ', 'ョ',
                'ラ', 'リ', 'ル', 'レ', 'ロ',
                'ワ', 'ヲ', 'ン',
                'ー']
    romaji = ['a', 'i', 'u', 'e', 'o',
              'ka', 'ki', 'ku', 'ke', 'ko',
              'ga', 'gi', 'gu', 'ge', 'go',
              'sa', 'shi', 'su', 'se', 'so',
              'za', 'ji', 'zu', 'ze', 'zo',
              'ta', 'chi', 'tsu', 'te', 'to',
              'da', 'dji', 'dzu', 'de', 'do',
              '[double_consonant]',
              'na', 'ni', 'nu', 'ne', 'no',
              'ha', 'hi', 'fu', 'he', 'ho',
              'ba', 'bi', 'bu', 'be', 'bo',
              'pa', 'pi', 'pu', 'pe', 'po',
              'ma', 'mi', 'mu', 'me', 'mo',
              'ya', 'yu', 'yo',
              '[small_ya]', '[small_yu]', '[small_yo]',
              'ra', 'ri', 'ru', 're', 'ro',
              'wa', 'wo', 'n']
    kana = hiragana + katakana
    return kana, hiragana, katakana, romaji


def gather_data():
    print('gather')
    furigana, kanji, english = [], [], []

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
            furigana += [line[1]]
            if line[2] == '':
                kanji += [line[1]]
            else:
                kanji += [line[2]]
            line[4] = line[4].split('\r')
            if line[4][0] == '':
                no_english += 1
            english += [line[4][0]]
        print('No English: {}'.format(no_english))
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
                        kanji += ['']
                        furigana += [line[:count2-1]]
                        english += [line[count2:]]
                        break
                    else:
                        kanji += [line[:count2]]
                        count2 += 2
                        marker = count2
                if character == ')':
                    furigana += [line[marker:count2]]
                    english += [line[count2+3:]]
                    break
                count2 += 1
    return furigana, kanji, english


def manipulate_data(furigana, kanji, english, words_with_same_furigana, words_with_same_kanji, kana):
    print('manipulate')
    all_kanji = []
    lim = 5
    for i in range(len(kanji)):
        print('\ni', i, end=', ')
        for j in range(i + 1, i + 1 + len(kanji)):
            if j > len(kanji) - 1:
                j -= len(kanji)
            else:
                if furigana[i] == furigana[j]:
                    words_with_same_furigana[i] += '{} '.format(kanji[j])
        kanji_set = ''
        for k in kanji[i]:
            if k not in ['', '~', '(', ')', '/', '='] and k not in kana:
                kanji_set += k
        # this is one of the k's in kanji[i], we want the english for this kanji and all the readings for it
        # do that here, and then in the next step we will search for words for each reading
        # heres the plan, we need to go thru all the kanji[i] first and give them kanji-readings
        # like [覚かく, 係けい], so then we know not just the kanji in each word but the specific reading of it
        # call it like kanjireading
        # then when we search for other words with the kanji we can easily check which reading of it it has
        # we can check if we have gone through all the readings by using things like
        # len(kyoiku_readings[i]) shows to total number of readings for the kanji
        # if kanjireading[i][j][1:] in kyoiku_readings[i]: count one for this kyoiku reading
        # note we have to be careful about hiragana, katakana. need like a quit translator function for that
        for k in kanji_set:
            count_wwsk = 0
            for j in range(i + 1, i + 1 + len(kanji)):
                if j > len(kanji) - 1:
                    j -= len(kanji)
                else:
                    if k in kanji[j] and count_wwsk < lim:  # need to check for kanjireadings, not just kanji
                        1
                        # this is one of the k's in kanji[i], and it was found to be in kanji[j]
                        # this word
            if k not in all_kanji:
                all_kanji += [k]
    return words_with_same_furigana, words_with_same_kanji, all_kanji


def print_cards_txt(furigana, kanji, english, words_with_same_furigana, words_with_same_kanji):
    print('print')
    file = codecs.open('{}/{}'.format(os.getcwd(), 'N2_Anki_File.txt'), 'w', 'UTF-8')
    for i in range(len(kanji)):
        file.write('{};{};{};{};{}\n'.format(kanji[i], furigana[i], english[i], words_with_same_furigana[i],
                                             words_with_same_kanji[i]))
    file.close()


def get_kyoiku_kanji(joyo_kanji, joyo_english, joyo_readings):
    file = codecs.open('{}/{}'.format(os.getcwd(), 'Kyoiku Kanji.txt'), 'r', 'UTF-8')
    text = file.read()
    file.close()
    kyoiku_kanji = []
    for k in text:
        if k not in kyoiku_kanji:
            kyoiku_kanji += [k]
    kyoiku_english, kyoiku_readings = kyoiku_kanji.copy(), kyoiku_kanji.copy()
    for i in range(len(kyoiku_kanji)):
        for j in range(len(joyo_kanji)):
            if kyoiku_kanji[i] == joyo_kanji[j]:
                kyoiku_english[i], kyoiku_readings[i] = joyo_english[j], joyo_readings[j]
                break
    for i in range(len(kyoiku_readings)):
        kyoiku_readings[i] = kyoiku_readings[i].split('、')
        kyoiku_readings[i][len(kyoiku_readings[i]) - 1] = kyoiku_readings[i][len(kyoiku_readings[i]) - 1].split(
            '\r')[0]
        for j in range(len(kyoiku_readings[i])):
            if '[' in kyoiku_readings[i][j]:
                kyoiku_readings[i][j] = kyoiku_readings[i][j].split('[')[0]
            if '（' in kyoiku_readings[i][j]:
                kyoiku_readings[i][j] = kyoiku_readings[i][j][1:len(kyoiku_readings[i][j]) - 1]
    return kyoiku_kanji, kyoiku_english, kyoiku_readings


def get_joyo_kanji():
    file = codecs.open('{}/{}'.format(os.getcwd(), 'Joyo Kanji.txt'), 'r', 'UTF-8')
    text = file.read()
    file.close()
    lines = text.split('\n')
    joyo_kanji = [0] * int(len(lines) / 2)
    joyo_grade = [0] * int(len(lines) / 2)
    joyo_english = [0] * int(len(lines) / 2)
    joyo_readings = [0] * int(len(lines) / 2)
    for i in range(0, len(lines), 2):
        j = int(i / 2)
        lines[i] = lines[i].split('\t')
        joyo_kanji[j] = lines[i][0].split('\xa0')[0]
        joyo_grade[j] = lines[i][4]
        joyo_english[j] = lines[i][6]
        joyo_readings[j] = lines[i][7]
    return joyo_kanji, joyo_grade, joyo_english, joyo_readings


def main():
    test = 1
    if test == 1:
        joyo_kanji, joyo_grade, joyo_english, joyo_readings = get_joyo_kanji()
        kyoiku_kanji, kyoiku_english, kyoiku_readings = get_kyoiku_kanji(joyo_kanji, joyo_english, joyo_readings)
        print(kyoiku_english)
    else:
        start_time = time.time()
        kana, hiragana, katakana, romaji = get_kana_sets()
        # kyoiku_kanji = get_kyoiku_kanji()
        furigana, kanji, english = gather_data()
        words_with_same_furigana, words_with_same_kanji = kanji.copy(), kanji.copy()
        words_with_same_furigana, words_with_same_kanji, all_kanji = manipulate_data(furigana, kanji, english,
                                                                                     words_with_same_furigana,
                                                                                     words_with_same_kanji, kana)
        file = codecs.open('{}/{}'.format(os.getcwd(), 'all_kanji.txt'), 'w', 'UTF-8')
        for k in all_kanji:
            file.write('{}'.format(k))
        file.close()
        print_cards_txt(furigana, kanji, english, words_with_same_furigana, words_with_same_kanji)
        total_time = time.time() - start_time
        # count = 0
        # for k in all_kanji:
        #     if k not in kyoiku_kanji:
        #         count += 1
        #         print(count, k)

        print(all_kanji)
        print('Total Kanji: {}'.format(len(all_kanji)))
        print('Time: {}min'.format(total_time/60))


main()
