from py_files.get_kana import get_kana


def convert_to_hiragana(text, kana):

    # go through the text  to be switched for each character text[j]
    for k in text:

        # if character is already hiragana, skip do nothing, go to the next character
        if k in kana['katakana']:

            # katakana index and hiragana index line up, so get katakana index of this character, and use it in hiragana
            hiragana_index_of_k = kana['katakana'].index(k)
            text = text.replace(k, kana['hiragana'][hiragana_index_of_k])
    return text


def test_convert_to_hiragana():

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

    assert convert_to_hiragana(hiragana_text1, kana) == hiragana_text1, \
        f"{convert_to_hiragana(hiragana_text1, kana)} != {hiragana_text1}"
    assert convert_to_hiragana(hiragana_text2, kana) == hiragana_text2, \
        f"{convert_to_hiragana(hiragana_text2, kana)} != {hiragana_text2}"
    assert convert_to_hiragana(katakana_text1, kana) == hiragana_text1, \
        f"{convert_to_hiragana(katakana_text1, kana)} != {hiragana_text1}"
    assert convert_to_hiragana(katakana_text2, kana) == hiragana_text2, \
        f"{convert_to_hiragana(katakana_text2, kana)} != {hiragana_text2}"

    print('test_to_hiragana - Passed')

    return
