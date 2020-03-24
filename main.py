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
    # note that a set {} is a list of *unique* elements
    return(len({entry.route_name for entry in logbook_entries}))


def unsuccessful_attempts(logbook_entries):
    successful_attempts = len(logbook_entries)
    total_attempts = sum([entry.attempts for entry in logbook_entries])
    unsuccessul_attempts = total_attempts - successful_attempts
    return(unsuccessul_attempts)


def mean_grade(logbook_entries):
    numeric_grades = [GRADE_TO_NUMBER[entry.grade] for entry in logbook_entries]
    # int always rounds down so use int(X+0.5) for nearest integer to X
    mean_numeric_grade = int(sum(numeric_grades) / len(numeric_grades) + 0.5)
    return(NUMBER_TO_GRADE[mean_numeric_grade])


def hardest_route(logbook_entries):
    numeric_grades = [GRADE_TO_NUMBER[entry.grade] for entry in logbook_entries]
    return(NUMBER_TO_GRADE[max(numeric_grades)])


def furthest_from_average(logbook_entries):
    mean_numeric_grade = mean([GRADE_TO_NUMBER[entry.grade] for entry in logbook_entries])
# delta is the difference between the numeric grade and the mean numeric grade
    logbook_entries_with_deltas = [
        (abs(GRADE_TO_NUMBER[entry.grade] - mean_numeric_grade), entry)
        for entry in logbook_entries
    ]
    maxdelta = max(logbook_entries_with_deltas)[0]
# Note that there may be more than one route with grade furthest from the mean.
# Also, if the mean turns out to be an integer (only likely for short logbooks)
# there may be some routes the same distance above the mean as below the mean.
# For example, consider the three entry logbook with grades 6c, 7a, 7b.
# Both the routes with grades 6c and 7b would be furthest from the mean.
# Therefore, we want to return a list of all the routes with grade furthest
# from the mean.
    return([
        (entry[1].route_name, entry[1].grade)
        for entry in logbook_entries_with_deltas if entry[0] == maxdelta
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
    print(furthest_from_average(logbook_entries))

if __name__ == '__main__':
    main()