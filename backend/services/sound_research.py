from dataclasses import dataclass

from pydub import AudioSegment

from backend.services.feature_extraction import feature_extraction


@dataclass
class Feature:
    speech_rate: str  # 話速
    pitch: str  # 音程
    syllable_1: str  # 第一音節のタイプ
    syllable_2: str  # 第二音節のタイプ
    syllable_3: str  # 第三音節のタイプ
    syllable_4: str  # 第四音節のタイプ


def sound_research(audio_file):
    # 音声ファイルの読み込み
    # 音声ファイルaudio_fileはファイル名である。つまりstring型
    sound = AudioSegment.from_file(audio_file, format="ogg")

    # 特徴量抽出
    feature = feature_extraction(sound)

    return feature
