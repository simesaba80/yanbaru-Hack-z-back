import numpy as np


def average_amplitude_calculator(sound):
    # 音声データの取得
    sound_data = sound.get_array_of_samples()

    # 平均振幅の計算
    average_amplitude = np.mean(np.abs(sound_data))

    return average_amplitude
