import csv
from statistics import mean
from collections import namedtuple

# GRADE_TO_NUMBER: dict for converting French grades to numeric grades
GRADE_TO_NUMBER = {}

with open('grade_table.csv') as csvfile:
    grade_reader = csv.reader(csvfile)
    for row in grade_reader:
        GRADE_TO_NUMBER[row[0]] = int(row[1])

# we also want the inverse to convert numeric grades back to French grades:
NUMBER_TO_GRADE = {value: key for key, value in GRADE_TO_NUMBER.items()}

# logbook_entries: list of named tuples of form [(route name, grade, tries)]
LogbookEntry = namedtuple('LogbookEntry', ['route_name', 'grade', 'attempts'])


def number_of_unique_routes(logbook_entries):
    return(len({entry.route_name for entry in logbook_entries}))


def unsuccessful_attempts(logbook_entries):
    successful_attempts = len(logbook_entries)
    total_attempts = sum([entry.attempts for entry in logbook_entries])
    unsuccessul_attempts = total_attempts - successful_attempts
    return(unsuccessul_attempts)


def mean_grade(logbook_entries):
    numeric_grades = [GRADE_TO_NUMBER[entry.grade] for entry in logbook_entries]
    # int always rounds down so use int(X+0.5) for nearest integer to X
    mean_numeric_grade = int(mean(numeric_grades) + 0.5)
    return(NUMBER_TO_GRADE[mean_numeric_grade])


def hardest_route(logbook_entries):
    numeric_grades = [GRADE_TO_NUMBER[entry.grade] for entry in logbook_entries]
    return(NUMBER_TO_GRADE[max(numeric_grades)])


def furthest_from_average(logbook_entries):
    """
    Note that there may be more than one route with grade furthest from the mean.
    Also, if the mean turns out to be an integer (only likely for short logbooks)
    there may be some routes the same distance above the mean as below the mean.
    For example, consider the three entry logbook with grades 6c, 7a, 7b.
    Both the routes with grades 6c and 7b would be furthest from the mean.
    Therefore, we want to return a list of all the routes with grade furthest
    from the mean.

    The routes with grade furthest from the mean will be either all the routes
    with the maximum grade in the logbook, all the routes with the minimum grade
    in the logbook, or all the routes with either the maximum or the minimum
    grade in the logbook, so we distinguish between the three cases:
    """
    numeric_grades = [GRADE_TO_NUMBER[entry.grade] for entry in logbook_entries]
    max_grade = max(numeric_grades)
    min_grade = min(numeric_grades)
    average_grade = mean(numeric_grades)

    delta_plus = max_grade - average_grade
    delta_minus = average_grade - min_grade

    if delta_plus > delta_minus:
        furthest_grade = [max_grade]

    elif delta_plus == delta_minus:
        furthest_grade = [max_grade, min_grade]

    else:
        furthest_grade = [min_grade]

    return([
        (entry.route_name, entry.grade)
        for entry in logbook_entries
        if GRADE_TO_NUMBER[entry.grade] in furthest_grade
        ])


def analyse_logbook(logbook_entries):
    return([number_of_unique_routes(logbook_entries),
           unsuccessful_attempts(logbook_entries),
           mean_grade(logbook_entries),
           hardest_route(logbook_entries),
           furthest_from_average(logbook_entries)])


def main():
    logbook_entries = []

    with open('logbook.csv') as csvfile:
        logbook_reader = csv.reader(csvfile)
        for row in logbook_reader:
            *row, attempts = row
            logbook_entries.append(LogbookEntry(*row, int(attempts)))

    print(number_of_unique_routes(logbook_entries))
    print(unsuccessful_attempts(logbook_entries))
    print(mean_grade(logbook_entries))
    print(hardest_route(logbook_entries))
    print(', '.join(
        ' '.join(route)
        for route in furthest_from_average(logbook_entries)
    ))


if __name__ == '__main__':
    main()
