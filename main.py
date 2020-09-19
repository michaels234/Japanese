import os
import codecs


def kana_sets():
    hiragana = ['あ', 'い', 'う', 'え', 'お',
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
                'ワ', 'ヲ', 'ン']


def gather_data():
    print("gather")
    kana, kanji, definition = [], [], []

    # which = 0  # both lists
    which = 1  # list 1
    # which = 2  # list 2
    if which in [0, 1]:
        name = "N2 Vocab List From jlptstudy.txt"
        file = codecs.open("{}\\{}".format(os.getcwd(), name), 'r', 'UTF-8')
        text = file.read()
        lines = text.split("\n")
        for line in lines:
            line = line.split("\t")
            kana += [line[1]]
            kanji += [line[2]]
            line[4] = line[4].split("\r")
            definition += [line[4][0]]
    if which in [0, 2]:
        name = "N2 Vocab List From japanesetest4you.txt"
        file = codecs.open("{}/{}".format(os.getcwd(), name), 'r', 'UTF-8')
        text = file.read()
        lines = text.split("\n")
        for line in lines:
            count2 = 0
            marker = 0
            for character in line:
                if character == " " and marker == 0:
                    if line[count2-1] == ":":
                        kanji += [""]
                        kana += [line[:count2-1]]
                        definition += [line[count2:]]
                        break
                    else:
                        kanji += [line[:count2]]
                        count2 += 2
                        marker = count2
                if character == ")":
                    kana += [line[marker:count2]]
                    definition += [line[count2+3:]]
                    break
                count2 += 1
    return kana, kanji, definition


def manipulate_data(kana, kanji, definition):
    print("manipulate")
    count = 0
    for i in range(len(kanji)):
        if "説" in kanji[i]:
            count += 1
    print(count)


def print_cards_txt():
    print("print")


def main():
    # kana_sets()
    kana, kanji, definition = gather_data()
    # print(kana)
    print(kanji)
    # print(definition)
    print(len(kana), len(kanji), len(definition))
    manipulate_data(kana, kanji, definition)
    print_cards_txt()


main()
