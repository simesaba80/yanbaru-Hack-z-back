import numpy as np


def exclude_weakest_syllable(syllable_list):
    """
    最大振幅が最も小さいピークのかたまりをsyllable_listから除外する
    """
    # 最大振幅が最も小さいピークのかたまりを取得
    weakest_syllable = min(syllable_list, key=lambda x: np.max(x))

    # 最大振幅が最も小さいピークのかたまりをsyllable_listから除外
    syllable_list.remove(weakest_syllable)

    return syllable_list
