import numpy as np


def divide_at_min_peak(syllable_list, target_point):
    # 最大振幅が最も小さいピークの点を取得
    min_peak_point = min(syllable_list[target_point], key=lambda x: np.max(x))

    # min_peak_pointを基準にしてsyllable_list[target_point]を2つに分割
    syllable_list.insert(
        target_point + 1,
        syllable_list[target_point][
            syllable_list[target_point].index(min_peak_point) :
        ],
    )

    return syllable_list
