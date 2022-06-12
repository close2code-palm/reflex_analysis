"""Compares students who use and who doesnt
As an idea - how often bot users throw"""
from typing import List

import numpy as np
from matplotlib import pyplot as plt

from bot_effectiveness.data_gen import NetologyStudent, course_qa, course_design, student_001, student_000, student_002, \
    Course


def build_module_effectiveness():
    """Deviding courses to parts, after each part
    there is a marker(mark) - so it displays how usefull
    is our bot over time
    achiving own goal relatively to no-bot situation
    """


def build_full_course_effect(bot_used: List[NetologyStudent],
                             bot_unused: List[NetologyStudent]):
    """Visualyze effectivensess of bot usage"""

    # todo build bar chart by course
    # full list of courses
    courses = [course_qa, course_design]
    labels = [crs.naming for crs in courses]

    def get_mark_for_course_student(student: NetologyStudent, course: Course):
        """Getting average academic progress indicator"""
        all_marks = []
        for v in student.marks[course.id]:
            if v:
                all_marks.append(v)
        if not all_marks:
            return
        return sum(all_marks) / len(all_marks)



    def get_crs_mean_for_category(netology_user, crs):
        crs_means = []
        for s in netology_user:
            try:
                user_mean = get_mark_for_course_student(s, crs)
                if user_mean is None:
                    continue
                crs_means.append(user_mean)
            except KeyError:
                continue
        crs_mean = sum(crs_means) / len(crs_means)
        return crs_mean

    netology_bot_user_crs_means = [get_crs_mean_for_category(bot_used, crs)
                                   for crs in courses]
    netology_bot_unused_c_m = [get_crs_mean_for_category(bot_unused, crs) for crs in
                               courses]
    x = np.arange(len(labels))
    width = 0.35  # as 2 groups exists, 3 parts for brightness
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, netology_bot_user_crs_means, width, label='С Ботом')
    rects2 = ax.bar(x + width/2, netology_bot_unused_c_m, width, label='Без Бота')
    ax.set_ylabel('Средние оценки')
    ax.set_title('Оценки по направлениям с Ботом и без')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()
    # return plt
    plt.show()

# this metric should be used to count different courses effect
