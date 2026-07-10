from src.wordcount import count_words, top_n


def test_count_words_basic():
    counts = count_words("The cat sat on the mat. THE cat ran.")
    assert counts["the"] == 3
    assert counts["cat"] == 2
    assert counts["mat"] == 1


def test_top_n_orders_by_frequency():
    counts = count_words("a a a b b c")
    assert top_n(counts, 2) == [("a", 3), ("b", 2)]
