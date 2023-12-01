from __future__ import annotations

class Course:

    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq_string: str) -> bool:
        if (self.level >= 400 and prereq_string in self.prerequisites):
            return True
        return False

def find_courses(input_list: list[Course], prereq_string: str) -> list[str]:
    new_list: list[str] = []
    for course in input_list:
        if (course.level >= 400 and prereq_string in course.prerequisites):
            new_list.append(course.name)
    return new_list
