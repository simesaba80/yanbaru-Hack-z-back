import math


def frequency_to_midi(frequency):
    return 69 + 12 * math.log2(frequency / 440.0)


def get_pitch_class(frequency):
    midi_note = frequency_to_midi(frequency)
    return round(midi_note) % 12


def midi_pitch_calculator(sound):
    # soundの平均周波数を調べる
    frequency = sum(sound) / len(sound)

    pitch_class = get_pitch_class(frequency)

    return hex(pitch_class)[2:].upper()
