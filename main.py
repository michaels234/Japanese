import os
import codecs

# def kana_sets():
#     kana = [あいうえお
#             かきくけこ
#             がぎぐげご
#             さしすせそ
#             ざじずぜぞ
#             たちつてと
#             だぢづでど
#             っ
#             なにぬねの
#             はひふへほ
#             ばびぶべぼ
#             ぱぴぷぺぽ
#             まみむめも
#             やゆよ
#             ゃゅょ
#             らりるれろ
#             わをん]


def gather_data():
    print("gather")
    number, kana, kanji, definition = [], [], [], []
    name = "N2 Vocab List From jlptstudy.txt"
    file = codecs.open("{}\\{}".format(os.getcwd(), name), 'r', 'UTF-8')
    text = file.read()
    lines = text.split("\n")
    for line in lines:
        line = line.split("\t")
        number += [int(line[0])+1]
        kana += [line[1]]
        kanji += [line[2]]
        definition += [line[3]]

    # name = "N2 Vocab List From japanesetest4you.txt"
    # file = codecs.open("{}\\{}".format(os.getcwd(), name), 'r', 'UTF-8')
    # text = file.read()
    # lines = text.split("\n")
    # count1 = 1
    # for line in lines:
    #     count2 = 0
    #     marker = 0
    #     for character in line:
    #         if character == " " and marker == 0:
    #             if line[count2-1] == ":":
    #                 kanji += [""]
    #                 kana += [line[:count2-1]]
    #                 definition += [line[count2:]]
    #                 number += [count1]
    #                 break
    #             else:
    #                 kanji += [line[:count2]]
    #                 count2 += 2
    #                 marker = count2
    #         if character == ")":
    #             kana += [line[marker:count2]]
    #             definition += [line[count2+3:]]
    #             number += [count1]
    #             break
    #         count2 += 1
    #     count1 += 1
    return number, kana, kanji, definition


def manipulate_data(number, kana, kanji, definition):
    print("manipulate")
    count = 0
    for i in number:
        if "説" in kanji[i-1]:
            count += 1
    print(count)


def print_cards_txt():
    print("print")


def main():
    # kana_sets()
    number, kana, kanji, definition = gather_data()
    print(kanji)
    manipulate_data(number, kana, kanji, definition)
    print_cards_txt()


main()
