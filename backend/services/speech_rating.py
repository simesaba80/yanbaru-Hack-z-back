def speech_rating(sound):
    # 音声の長さ（ミリ秒）
    duration_ms = len(sound)

    thresholds = [
        1000,
        1179,
        1357,
        1536,
        1714,
        1893,
        2071,
        2250,
        2429,
        2607,
        2786,
        2964,
        3143,
        3321,
        3500,
    ]

    # もし値がNoneの場合、15を返す
    if duration_ms is None:
        return 15

    # 話速の分類
    for i, threshold in enumerate(thresholds):
        if duration_ms <= threshold:
            return i
