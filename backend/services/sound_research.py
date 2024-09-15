from pydub import AudioSegment
from dataclasses import dataclass

from services.feature_extraction import feature_extraction


@dataclass
class Feature:
    speech_rate: int  # 話速
    pitch: int  # 音程
    syllable_1: int  # 第一音節のタイプ
    syllable_2: int  # 第二音節のタイプ
    syllable_3: int  # 第三音節のタイプ
    syllable_4: int  # 第四音節のタイプ


# 音声ファイルの読み込み
sound = AudioSegment.from_file("sample.ogg", format="ogg")

# 特徴量抽出
feature = feature_extraction(sound)

# 特徴量を〇〇〇に渡す
# export(feature)

print(feature)
