# ----------------------------------------------------------------
# Author:  Group 9
#          Brandi Rosser
#          Jaden Fisher
#          Manar Mohammed
# Date:    07/09/2023
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# costs for their course roster.
# -----------------------------------------------------------------
from utility import input_int
from utility import input_string
import billing
import student

def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to login.
    # It has two parameters:
    # id, the student id;
    # s_list, which is the student list.
    # This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification
    # and return True. Otherwise, display error message and return
    # False.
    # -------------------------------------------------------------
    pin = input_string('Enter PIN: ').strip()
    result = False
    for i,p in s_list:
        if id == i:
            if pin == p:
                result = True
    if result:
        print('ID and PIN verified\n')
    else:
        print('ID or PIN incorrect\n')
    return result

def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.
    # It has no parameters.
    # It creates student list, in_state_list, course list, max
    # class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses.
    # This function has no return value.
    # -------------------------------------------------------------

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'], 'CSC102': ['1001'], 'CSC103': ['1002'], 'CSC104': []}
    student_in_state = {'1001': True, '1002': False, '1003': True, '1004': False}
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]

    while True:
        id = input_string('Enter ID to log in, or 0 to quit: ').strip()
        if id == '0':
            break
        elif login(id, student_list):
            while True:
                prompt = 'Enter '
                prompt += '1 to add course, '
                prompt += '2 to drop course,\n'
                prompt += '3 to list courses, '
                prompt += '4 to show bill, '
                prompt += '0 to exit: '
                choice = input_int(prompt)
                if choice == 0:
                    print('Session ended.\n')
                    break
                elif choice == 1:
                    student.add_course(id, course_roster, course_max_size)
                    print()
                elif choice == 2:
                    student.drop_course(id, course_roster)
                    print()
                elif choice == 3:
                    student.list_courses(id, course_roster)
                elif choice == 4:
                    billing.display_bill(id, student_in_state, course_roster, course_hours)
                else:
                    print('Please enter a valid choice 0-4.')

main()

