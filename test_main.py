from main import analyse_logbook


def test_something():
    logbook_entries = [
        ("Super furry animal", "7a+", 1),
        ("Rescate", "7b+", 3),
        ("Super furry animal", "7a+", 1),
        ("Amigo", "5+", 1)
    ]

    expected_output = [
        3,
        2,
        "7a",
        "7b+",
        "Amigo",
    ]

    assert analyse_logbook(logbook_entries) == expected_output
