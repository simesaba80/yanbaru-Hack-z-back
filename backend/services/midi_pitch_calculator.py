import math

import numpy as np


def frequency_to_midi(frequency):
    return 69 + 12 * math.log2(frequency / 440.0)


def get_pitch_class(frequency):
    midi_note = frequency_to_midi(frequency)
    return round(midi_note) % 12


def get_average_frequency(audio_segment):
    # オーディオデータを数値の配列に変換
    samples = np.array(audio_segment.get_array_of_samples())

    # オーディオサンプルのFFT（高速フーリエ変換）
    fft_spectrum = np.fft.fft(samples)
    frequencies = np.fft.fftfreq(len(fft_spectrum), 1.0 / audio_segment.frame_rate)

    # 振幅の絶対値を取得
    amplitude = np.abs(fft_spectrum)

    # 振幅が最大の周波数成分を求める
    peak_freq = frequencies[np.argmax(amplitude)]

    print(type(abs(peak_freq)))

    return abs(peak_freq)  # 周波数を返す


def midi_pitch_calculator(sound):
    # soundの平均周波数を調べる
    frequency = get_average_frequency(sound)

    print(type(frequency))

    pitch_class = get_pitch_class(frequency)

    # return hex(pitch_class)[2:].upper()
    return pitch_class
