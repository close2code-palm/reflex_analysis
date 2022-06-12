"""Module to mock data"""
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Course:
    id: int
    naming: str
    modules: List[int]

    def __str__(self):
        return self.naming


@dataclass
class NetologyStudent:
    used_bot: bool
    name: str
    netology_id: int
    courses: List[Course]
    marks: Dict[int, List[Optional[int]]]


course_qa = Course(2, 'QA', [1, 2, 3])
course_design = Course(3, 'Design', [1, 2, 3, 4])
student_000 = NetologyStudent(False, 'Venya', 000,
                              [course_qa],
                              {course_qa.id: [4, 3, None]})

student_001 = NetologyStudent(True, 'Zhenya', 1, [course_qa],
                              {course_qa.id: [5, 5, 5]})

student_002 = NetologyStudent(True, 'Sasha', 2, [course_qa],
                              {course_qa.id: [None, None, None]})

student_003 = NetologyStudent(True, 'Sasha', 3, [course_design],
                              {course_design.id: [4, 4, None]})

student_004 = NetologyStudent(False, 'Kolya', 4, [course_design],
                              {course_design.id: [4, 3, 5]})
# class FakeNetologyProvider:
