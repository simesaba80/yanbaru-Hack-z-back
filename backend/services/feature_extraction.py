from dataclasses import dataclass

from services.cutting_sound import cutting_sound
from services.speech_rating import speech_rating
from services.sound_display import sound_display
from services.average_amplitude_calculator import average_amplitude_calculator

from services.modifing_syllable import modifing_syllable
from services.syllable_max_amplitude import syllable_max_amplitude
from services.syllable_wave_detector import syllable_wave_detector


@dataclass
class Feature:
    speech_rate: str  # 話速
    pitch: str  # 音程
    syllable_1: str  # 第一音節のタイプ
    syllable_2: str  # 第二音節のタイプ
    syllable_3: str  # 第三音節のタイプ
    syllable_4: str  # 第四音節のタイプ


def feature_extraction(sound):
    # 音声の切り抜き
    cutted_sound = cutting_sound(sound)

    # 話速の検出
    speech_rate = speech_rating(cutted_sound)

    # 音程の検出
    pitch = "A"

    # 音声の情報表示
    sound_display(cutted_sound)

    # 平均振幅の計算
    average_amplitude = average_amplitude_calculator(cutted_sound)

    # 適切な音節の決定
    modified_syllable_list = modifing_syllable(cutted_sound, average_amplitude)

    # 音節変数の初期化
    syllable_1 = syllable_2 = syllable_3 = syllable_4 = "N/A"  # デフォルト値を設定

    # 第一音節から第四音節までの最大振幅、波形の検出
    for number in range(4):
        # 音節の最大振幅を取得
        first_number = syllable_max_amplitude(
            modified_syllable_list[number], average_amplitude
        )
        print("first_number : ", first_number)
        # 音節の波形検出
        second_number = syllable_wave_detector(
            modified_syllable_list[number], average_amplitude
        )
        print("second_number : ", second_number)

        syllable_number = first_number * second_number
        print("syllable_number : ", syllable_number)

        syllable_number = hex(syllable_number)[2:].upper()

        if number == 0:
            syllable_1 = syllable_number
        elif number == 1:
            syllable_2 = syllable_number
        elif number == 2:
            syllable_3 = syllable_number
        else:
            syllable_4 = syllable_number

        # 構造体Featureに格納
        feature = Feature(
            speech_rate, pitch, syllable_1, syllable_2, syllable_3, syllable_4
        )

    return feature
