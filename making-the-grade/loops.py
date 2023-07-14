"""Functions for organizing and calculating student exam scores."""
import math

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    l = []
    for s in student_scores:
        t = round(s)
        l.append(t)

    return l


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    c = 0
    for i in student_scores:
        if ( i <= 40 ):
            c = c + 1
    return c


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    l = []
    for i in student_scores:
        if i >= threshold:
            l.append(i)
    return l


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    # l = []
    # spread = int((highest-40)/4)
    # t1 = 41
    # t2 = t1+spread
    # t3 = t2+spread
    # t4 = t3+spread
    # l.append(t1)
    # l.append(t2)
    # l.append(t3)
    # l.append(t4)
    # return l

    grade = []
    spread = (highest-40)/4
    lower = 41

    for _ in range(4):
        grade.append(int(lower))
        lower += spread

    return grade
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranking = []
    for rank, (score, name) in enumerate(zip(student_scores, student_names)):
        entry = f"{rank + 1}. {name}: {score}"
        ranking.append(entry)
    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for info in student_info:
        name, score = info
        if score == 100:
            return [name, score]
    return []
