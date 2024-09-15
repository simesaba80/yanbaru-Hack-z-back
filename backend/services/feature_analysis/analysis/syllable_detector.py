def syllable_detector(sound, amplitude_peak_list):
    """
    まずリストsyllable_list_tmpを用意する
    ピークの点と次の点の誤差が±1000以内に収まってるとき、カウント変数をインクリメントし、syllable_list_tmpに詰め込む
    もしその次の点が次の点との誤差が大きい場合、カウント変数をリセットする。syllable_list_tmpの中身を捨てる
    もしカウント変数が100以上で、かつ次の点との誤差が大きい場合、syllable_list_tmpの中身をsyllable_listに詰め込む

    syllable_list_tmpの中身をsyllable_listに詰め込む際、syllable_list_tmpというリスト自体を詰め込むので、
    syllable_list内の要素内にはリストのみが詰まっていることになる。これでピークのまとまりが何種類かが分かる
    """

    syllable_list_tmp = []
    syllable_list = []
    count = 0

    for i in range(len(amplitude_peak_list) - 1):
        if (
            count >= 100
            and abs(amplitude_peak_list[i][0] - amplitude_peak_list[i + 1][0]) >= 1000
        ):
            syllable_list.append(syllable_list_tmp)
            count = 0
            syllable_list_tmp = []
            continue

        elif abs(amplitude_peak_list[i][0] - amplitude_peak_list[i + 1][0]) >= 1000:
            count = 0
            syllable_list_tmp = []
            continue

        count += 1
        syllable_list_tmp.append([amplitude_peak_list[i][0], amplitude_peak_list[i][1]])

    # ループ終了後に、残った syllable_list_tmp を syllable_list に追加
    if syllable_list_tmp:
        syllable_list.append(syllable_list_tmp)

    return syllable_list
