# ----------------------------------------------------------------
# Author:  Group 9
#          Brandi Rosser
#          Jaden Fisher
#          Manar Mohammed
# Date:    07/09/2023
#
# Test the billing module.
#
# Run all tests with this command (in a shell at a terminal):
# python3 -m unittest --verbose
#
# Run only these tests with this command (in a shell at a terminal):
# python3 test_billing.py
# ----------------------------------------------------------------
from billing import course_cost
from billing import course_line
from billing import student_line
from billing import time_line
from billing import total_line
from datetime import datetime as dt
from unittest import TestCase


class TestBilling(TestCase):
    def test_course_cost_0(self):
        self.assertEqual(course_cost(3, True), 675)

    def test_course_cost_1(self):
        self.assertEqual(course_cost(3, False), 2550)

    def test_course_cost_2(self):
        self.assertEqual(course_cost(4, True), 900)

    def test_course_cost_3(self):
        self.assertEqual(course_cost(4, False), 3400)

    def test_course_cost_4(self):
        self.assertEqual(course_cost(5, True), 1125)

    def test_course_cost_5(self):
        self.assertEqual(course_cost(5, False), 4250)

    def test_course_line_0(self):
        self.assertEqual(
            course_line('CSC101', 3, 675.00),
            'CSC101        3  $ 675.00\n'
            )

    def test_course_line_1(self):
        self.assertEqual(
            course_line('CSC102', 4, 900.00),
            'CSC102        4  $ 900.00\n'
            )

    def test_course_line_2(self):
        self.assertEqual(
            course_line('CSC104', 3, 675.00),
            'CSC104        3  $ 675.00\n'
            )

    def test_student_line_1001(self):
        self.assertEqual(
            student_line('1001', True),
            'Student: 1001, In-State Student\n'
            )

    def test_student_line_1002(self):
        self.assertEqual(
            student_line('1002', False),
            'Student: 1002, Out-of-State Student\n'
            )

    def test_student_line_1003(self):
        self.assertEqual(
            student_line('1003', True),
            'Student: 1003, In-State Student\n'
            )

    def test_student_line_1004(self):
        self.assertEqual(
            student_line('1004', False),
            'Student: 1004, Out-of-State Student\n'
            )

    def test_time_line_0(self):
        when = dt(2022, 10, 13, 9, 15, 38)
        self.assertEqual(
            time_line(when),
            'Generated on 2022-10-13 09:15:38\n'
            )

    def test_time_line_1(self):
        when = dt(2023, 7, 9, 21, 10, 4)
        self.assertEqual(
            time_line(when),
            'Generated on 2023-07-09 21:10:04\n'
            )

    def test_total_line_0(self):
        self.assertEqual(
            total_line(10, 2250.00),
            'Total        10  $2250.00\n'
            )

    def test_total_line_1(self):
        self.assertEqual(
            total_line(4, 900.00),
            'Total         4  $ 900.00\n'
            )

if __name__ == '__main__':
    unittest.main()

