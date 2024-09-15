import numpy as np


def syllable_wave_detector(syllable, average_amplitude):
    # 基準となる関数を用意
    def Flat_type_function(x):
        # 平坦型は変化がほとんどない一定の値を持つ
        return np.full_like(x, np.mean(x))

    def Decaying_type_function(x):
        # 減衰型は、指数関数的に減少する形
        return np.exp(-np.linspace(0, 5, len(x))) * np.max(x)

    def Rising_type_function(x):
        # 立ち上がり型は、指数関数的に増加する形
        return np.exp(np.linspace(0, 5, len(x))) / np.exp(5) * np.max(x)

    def Mountain_type_function(x):
        # 山型は、中央でピークを持ち、両側で減衰する形
        return np.exp(-0.5 * (np.linspace(-3, 3, len(x)) ** 2)) * np.max(x)

    # シラブル波形の基準データ
    # x = np.array(syllable)
    x = [sublist[1] for sublist in syllable]

    # 基準関数に基づいた波形の生成
    flat_wave = Flat_type_function(x)
    decaying_wave = Decaying_type_function(x)
    rising_wave = Rising_type_function(x)
    mountain_wave = Mountain_type_function(x)

    # シラブル波形と各基準波形の差を計算
    flat_diff = np.sum(np.abs(x - flat_wave)) * 20
    decaying_diff = np.sum(np.abs(x - decaying_wave))
    rising_diff = np.sum(np.abs(x - rising_wave))
    mountain_diff = np.sum(np.abs(x - mountain_wave)) * 10

    # 最も差が小さいものを選択
    diff_list = {1: flat_diff, 2: decaying_diff, 3: rising_diff, 4: mountain_diff}

    best_match = min(diff_list, key=diff_list.get)

    return best_match
