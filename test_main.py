import csv
from main import (
    analyse_logbook,
    unsuccessful_attempts,
    mean_grade, hardest_route,
    furthest_from_average,
    number_of_unique_routes,
    LogbookEntry
    )


TEST_LOGBOOK_ENTRIES = [
    ('Super furry animal', '7a+', 1),
    ("Rescate", "7b+", 3),
    ("Super furry animal", "7a+", 1),
    ("Amigo", "5+", 1)
]

TEST_LOGBOOK_ENTRIES = [LogbookEntry(*entry) for entry in TEST_LOGBOOK_ENTRIES]


def test_number_of_unique_routes():
    expected_output = 3
    assert number_of_unique_routes(TEST_LOGBOOK_ENTRIES) == expected_output


def test_unsuccessful_attempts():
    expected_output = 2
    assert unsuccessful_attempts(TEST_LOGBOOK_ENTRIES) == expected_output


def test_mean_grade():
    expected_output = '7a'
    assert mean_grade(TEST_LOGBOOK_ENTRIES) == expected_output


def test_hardest_route():
    expected_output = '7b+'
    assert hardest_route(TEST_LOGBOOK_ENTRIES) == expected_output


def test_furthest_from_average():
    expected_output = [('Amigo', '5+')]
    assert furthest_from_average(TEST_LOGBOOK_ENTRIES) == expected_output


def test_analyse_logbook():
    expected_output = [
        3,
        2,
        '7a',
        '7b+',
        [('Amigo','5+')],
    ]
    assert analyse_logbook(TEST_LOGBOOK_ENTRIES) == expected_output
