def syllable_max_amplitude(syllable, average_amplitude):
    # 音節の最大振幅を取得
    # syllable_max_amplitude = max([item[1] for sublist in syllable for item in sublist])
    syllable_max_amplitude = 0
    for i in range(0, len(syllable)):
        if syllable_max_amplitude < syllable[i][1]:
            syllable_max_amplitude = syllable[i][1]

    # 音節の最大振幅が平均振幅の何倍かを取得
    for i in range(6, 3, -1):
        if syllable_max_amplitude >= i * average_amplitude:
            return i - 2

    return 1
