import numpy as np


def amplitude_peak_detector(sound, average_amplitude, ratio):
    # 音声データの取得
    sound_data = sound.get_array_of_samples()

    # 音声データの振幅リスト
    amplitude_list = np.abs(sound_data)

    # 平均振幅より大きい振幅をピークとする
    amplitude_peak = average_amplitude * ratio

    # 音声データのピーク検出
    amplitude_peak_list = []
    for i in range(len(amplitude_list)):
        if amplitude_list[i] > amplitude_peak:
            amplitude_peak_list.append([i, amplitude_list[i]])

    return amplitude_peak_list
