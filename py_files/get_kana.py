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
