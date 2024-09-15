def feature_to_color(feature):
    color1_data = (
        "#"
        + format(feature.speech_rate * 16, "x")
        + format(feature.pitch * 16, "x")
        + format(feature.syllable_1 * 16, "x")
    )
    color2_data = (
        "#"
        + format(feature.syllable_2 * 16, "x")
        + format(feature.syllable_3 * 16, "x")
        + format(feature.syllable_4 * 16, "x")
    )
    return color1_data, color2_data
