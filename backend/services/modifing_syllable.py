from fastapi import HTTPException

from backend.services.amplitude_peak_detector import amplitude_peak_detector
from backend.services.divide_at_min_peak import divide_at_min_peak
from backend.services.exclude_weakest_syllable import exclude_weakest_syllable
from backend.services.syllable_detector import syllable_detector

"""
syllable_list内のリストが4つになるように調整する
まず倍率ratioを0.2ずつ調整してamplitude_peakを再調整し、ピークの点をamplitude_peak_listに再度詰め込む
"""


def modifing_syllable(sound, average_amplitude):
    # 倍率の初期化
    ratio = 10.0

    # 音声のピーク検出
    # amplitude_peak_list内にはピークの点とその振幅が詰まっている
    amplitude_peak_list = amplitude_peak_detector(sound, average_amplitude, ratio)

    # 音節の検出
    syllable_list = syllable_detector(sound, amplitude_peak_list)

    # リストの長さが4になるまで繰り返す
    while len(syllable_list) != 4:
        # リストの初期化
        syllable_list = []

        # 次の倍率を計算
        ratio -= 0.2

        # 音声のピーク検出
        amplitude_peak_list = amplitude_peak_detector(sound, average_amplitude, ratio)

        # 音節の検出
        syllable_list = syllable_detector(sound, amplitude_peak_list)

        if ratio == 0:
            raise HTTPException(status_code=400, detail="Bad Request")

    # syllable_list内のピークのまとまりが4つある内、ピークのまとまりの要素数が3000以上のとき、
    for i in range(len(syllable_list)):
        if len(syllable_list[i]) >= 3000:
            # ピークの点の中で最も振幅が小さいピークの点を基準にリストを分割する
            syllable_list = divide_at_min_peak(syllable_list, i)
            # 最大振幅が最も小さいピークのかたまりをsyllable_listから除外する
            syllable_list = exclude_weakest_syllable(syllable_list)

    # 倍率を表示
    print("倍率 : ", ratio)

    return syllable_list
