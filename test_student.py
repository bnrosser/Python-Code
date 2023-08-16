# ----------------------------------------------------------------
# Brandi Rosser
#
# Test the student module.
#
# Run all tests with this command (in a shell at a terminal):
# python3 -m unittest --verbose
#
# Run only these tests with this command (in a shell at a terminal):
# python3 test_student.py
# ----------------------------------------------------------------
from copy import deepcopy
from student import attempt_to_add_course
from student import attempt_to_drop_course
from student import formatted_course_list
from unittest import TestCase

# Copied data from registration module,
# but this could be handled better another way.
course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}

class TestStudent(TestCase):
    def test_attempt_to_add_course_when_course_full(self):
        course, id = 'CSC103', '1001'
        roster = deepcopy(course_roster)
        try:
            attempt_to_add_course(id, roster, course_max_size, course)
            raise AssertionError('Should never reach here!')
        except Exception as e:
            # Unpack error message
            (message, *ignored) = e.args
            self.assertEqual(message, 'Course already full.')

    def test_attempt_to_add_course_when_course_not_offered(self):
        course, id = 'NotaCourse', '1001'
        roster = deepcopy(course_roster)
        try:
            self.assertTrue(course not in course_max_size.keys())
            self.assertTrue(course not in roster.keys())
            attempt_to_add_course(id, roster, course_max_size, course)
            raise AssertionError('Should never reach here!')
        except Exception as e:
            # Unpack error message
            (message, *ignored) = e.args
            self.assertEqual(message, 'Course not found')

    def test_attempt_to_add_course_when_student_already_enrolled(self):
        course, id = 'CSC101', '1003'
        roster = deepcopy(course_roster)
        try:
            attempt_to_add_course(id, roster, course_max_size, course)
            raise AssertionError('Should never reach here!')
        except Exception as e:
            # Unpack error message
            (message, *ignored) = e.args
            self.assertEqual(message, 'You are already enrolled in that course.')

    def test_attempt_to_add_course_when_success(self):
        course, id = 'CSC101', '1001'
        roster = deepcopy(course_roster)
        attempt_to_add_course(id, roster, course_max_size, course)
        self.assertTrue(id in roster[course])

    def test_attempt_to_drop_course_when_course_not_offered(self):
        course, id = 'NotaCourse', '1001'
        roster = deepcopy(course_roster)
        try:
            self.assertTrue(course not in course_max_size.keys())
            self.assertTrue(course not in roster.keys())
            attempt_to_drop_course(id, roster, course)
            raise AssertionError('Should never reach here!')
        except Exception as e:
            # Unpack error message
            (message, *ignored) = e.args
            self.assertEqual(message, 'Course not found')

    def test_attempt_to_drop_course_when_no_students_enrolled(self):
        course, id = 'CSC104', '1001'
        roster = deepcopy(course_roster)
        try:
            attempt_to_drop_course(id, roster, course)
            raise AssertionError('Should never reach here!')
        except Exception as e:
            # Unpack error message
            (message, *ignored) = e.args
            self.assertEqual(message, 'You are not enrolled in that course.')

    def test_attempt_to_drop_course_when_student_not_enrolled(self):
        course, id = 'CSC101', '1001'
        roster = deepcopy(course_roster)
        try:
            attempt_to_drop_course(id, roster, course)
            raise AssertionError('Should never reach here!')
        except Exception as e:
            # Unpack error message
            (message, *ignored) = e.args
            self.assertEqual(message, 'You are not enrolled in that course.')

    def test_attempt_to_drop_course_when_success(self):
        course, id = 'CSC102', '1001'
        roster = deepcopy(course_roster)
        attempt_to_drop_course(id, roster, course)
        self.assertTrue(id not in roster[course])

    def test_formatted_course_list_for_student_1001(self):
        self.assertEqual(
            formatted_course_list('1001', course_roster),
            """Courses registered:\nCSC102\nTotal number: 1\n"""
            )

    def test_formatted_course_list_for_student_1002(self):
        self.assertEqual(
            formatted_course_list('1002', course_roster),
            """Courses registered:\nCSC103\nTotal number: 1\n"""
            )

    def test_formatted_course_list_for_student_1003(self):
        self.assertEqual(
            formatted_course_list('1003', course_roster),
            """Courses registered:\nCSC101\nTotal number: 1\n"""
            )

    def test_formatted_course_list_for_student_1004(self):
        self.assertEqual(
            formatted_course_list('1004', course_roster),
            """Courses registered:\nCSC101\nTotal number: 1\n"""
            )

if __name__ == '__main__':
    unittest.main()

