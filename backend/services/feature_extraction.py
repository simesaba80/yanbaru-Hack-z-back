from dataclasses import dataclass

from fastapi import HTTPException

from backend.services.average_amplitude_calculator import average_amplitude_calculator
from backend.services.cutting_sound import cutting_sound
from backend.services.midi_pitch_calculator import midi_pitch_calculator
from backend.services.modifing_syllable import modifing_syllable
from backend.services.sound_display import sound_display
from backend.services.speech_rating import speech_rating
from backend.services.syllable_max_amplitude import syllable_max_amplitude
from backend.services.syllable_wave_detector import syllable_wave_detector


@dataclass
class Feature:
    speech_rate: int  # 話速
    pitch: int  # 音程
    syllable_1: int  # 第一音節のタイプ
    syllable_2: int  # 第二音節のタイプ
    syllable_3: int  # 第三音節のタイプ
    syllable_4: int  # 第四音節のタイプ


def feature_extraction(sound):
    # 音声の切り抜き
    cutted_sound = cutting_sound(sound)

    # 話速の検出
    speech_rate = speech_rating(cutted_sound)

    # 音程の検出
    pitch = midi_pitch_calculator(cutted_sound)

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
        # 音節の波形検出
        second_number = syllable_wave_detector(
            modified_syllable_list[number], average_amplitude
        )

        syllable_number = first_number * second_number
        syllable_number -= 1

        if (syllable_number is None) or (syllable_number < 0):
            syllable_number = 15

        if number == 0:
            syllable_1 = syllable_number
        elif number == 1:
            syllable_2 = syllable_number
        elif number == 2:
            syllable_3 = syllable_number
        else:
            syllable_4 = syllable_number

    # 音声の情報表示
    sound_display(cutted_sound)

    # 構造体Featureに格納
    feature = Feature(
        speech_rate, pitch, syllable_1, syllable_2, syllable_3, syllable_4
    )

    if None in feature:
        raise HTTPException(status_code=400, detail="Bad Request")

    return feature
