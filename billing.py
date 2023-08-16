# ----------------------------------------------------------------
# Brandi Rosser
# Date:    07/09/2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
from datetime import datetime as dt


def course_cost(hours, in_state):
    # ------------------------------------------------------------
    # This function returns the tuition cost for a course.
    # It takes two parameters:
    # hours, the credit hours for the course;
    # in_state, whether the student should be charged as in-state
    # or out-of-state.
    # The function returns the tuition cost in dollars.
    # ------------------------------------------------------------
    return hours * 225.00 if in_state else hours * 850.00

def course_line(course, hours, cost):
    # ------------------------------------------------------------
    # This function returns a formatted line summarizing a course
    # for the tuition bill.
    # It takes three parameters:
    # course, the name of the course;
    # hours, the credit hours for the course;
    # cost, the tuition cost for this student to take the course.
    # This function returns a formatted string.
    # ------------------------------------------------------------
    return f'{course}       {hours:2d}  ${cost:7.2f}\n'

def display_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill.
    # It takes four parameters:
    # id, the student id;
    # s_in_state, the list of in-state students;
    # c_rosters, the rosters of students in each course;
    # c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------
    print(formatted_bill(id, s_in_state, c_rosters, c_hours, dt.now()))


def formatted_bill(id, s_in_state, c_rosters, c_hours, when):
    # ------------------------------------------------------------
    # This function returns formatted text summarizing the tuition
    # bill.
    # It takes five parameters:
    # id, the student id;
    # s_in_state, the list of in-state students;
    # c_rosters, the rosters of students in each course;
    # c_hours, the number of hours in each course;
    # when, the date and time for when the summary is generated.
    # This function returns a formatted string.
    # ------------------------------------------------------------
    in_state = s_in_state[id]

    result = 'Tuition Summary\n'
    result += student_line(id, in_state)
    result += time_line(when)
    result += 'Course    Hours    Cost\n'
    result += '------    -----  --------\n'

    total_cost = 0
    total_hours = 0
    for course in c_rosters.keys():
        if id in c_rosters[course]:
            hours = c_hours[course]
            cost = course_cost(hours, in_state)
            result += course_line(course, hours, cost)
            total_cost += cost
            total_hours += hours

    result += '        -------  --------\n'
    result += total_line(total_hours, total_cost)
    return result

def student_line(id, in_state):
    # ------------------------------------------------------------
    # This function returns a formatted line summarizing the
    # student for the tuition bill.
    # It takes two parameters:
    # id, the student id;
    # in_state, whether the student should be charged as in-state
    # or out-of-state.
    # This function returns a formatted string.
    # ------------------------------------------------------------
    in_state_term = 'In-State' if in_state else 'Out-of-State'
    return f'Student: {id}, {in_state_term} Student\n'

def time_line(when):
    # ------------------------------------------------------------
    # This function returns a formatted line summarizing when the
    # tuition bill was generated.
    # It takes one parameter:
    # when, the date and time for when the summary is generated.
    # This function returns a formatted string.
    # ------------------------------------------------------------
    when = when.strftime('%Y-%m-%d %H:%M:%S')
    return f'Generated on {when}\n'

def total_line(total_hours, total_cost):
    # ------------------------------------------------------------
    # This function returns a formatted line summarizing the total
    # for the tuition bill.
    # It takes two parameters:
    # total_hours, the total credit hours for this student;
    # total_cost, the total tuition cost for this student.
    # This function returns a formatted string.
    # ------------------------------------------------------------
    return f'Total        {total_hours:2d}  ${total_cost:7.2f}\n'

