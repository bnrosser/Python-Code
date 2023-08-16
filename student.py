# ----------------------------------------------------------------
# Brandi Rosser
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------
from utility import input_string

def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.
    # It has three parameters:
    # id is the ID of the student to be added;
    # c_roster is the list of class rosters;
    # c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to
    # add.  If the course is not offered, display error message
    # and stop.  If student has already registered for this
    # course, display error message and stop.  If the course is
    # full, display error message and stop.  If everything is okay,
    # add student ID to the course’s roster and display a message
    # if there is no problem.
    # This function has no return value.
    # -------------------------------------------------------------
    course = input_string('Enter course you want to add: ')
    try:
        attempt_to_add_course(id, c_roster, c_max_size, course)
        print('Course added')
    except Exception as e:
        # Unpack error message
        (message, *ignored) = e.args
        # Print message, but drop Exception as handled
        print(message)

def attempt_to_add_course(id, c_roster, c_max_size, course):
    # ------------------------------------------------------------
    # This function attempts to add a student to a course.
    # It has four parameters:
    # id is the ID of the student to be added;
    # c_roster is the list of class rosters;
    # c_max_size is the list of maximum class sizes;
    # course is the name of the course to be added.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  If the course is full, display
    # error message and stop.  If everything is okay, add student
    # ID to the course’s roster and display a message if there is
    # no problem.
    # This function has no return value.
    # ------------------------------------------------------------
    if course in c_max_size.keys():
        if course not in c_roster.keys():
            # Course not already in roster, so add empty course
            c_roster[course] = []
        enrolled_students = c_roster[course]
        if id in enrolled_students:
            raise RuntimeError('You are already enrolled in that course.')
        elif len(enrolled_students) == c_max_size[course]:
            raise RuntimeError('Course already full.')
        else:
            enrolled_students.append(id)
    else:
        raise RuntimeError('Course not found')

def attempt_to_drop_course(id, c_roster, course):
    # ------------------------------------------------------------
    # This function drops a student from a course.
    # It has three parameters:
    # id is the ID of the student to be dropped;
    # c_roster is the list of class rosters;
    # course is the name of the course to be dropped.
    # If the course is not offered, display error message and stop.
    # If the student is not enrolled in that course, display error
    # message and stop. Remove student ID from the course’s roster
    # and display a message if there is no problem.
    # This function has no return value.
    # ------------------------------------------------------------
    if course in c_roster.keys():
        enrolled_students = c_roster[course]
        if id in enrolled_students:
            enrolled_students.remove(id)
        else:
            raise RuntimeError('You are not enrolled in that course.')
    else:
        raise RuntimeError('Course not found')

def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.
    # It has two parameters:
    # id is the ID of the student to be dropped;
    # c_roster is the list of class rosters.
    # This function asks the user to enter the course he/she wants
    # to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.
    # This function has no return value.
    # -------------------------------------------------------------
    course = input_string('Enter course you want to drop: ')
    try:
        attempt_to_drop_course(id, c_roster, course)
        print('Course dropped')
    except Exception as e:
        # Unpack error message
        (message, *ignored) = e.args
        # Print message, but drop Exception as handled
        print(message)

def formatted_course_list(id, c_roster):
    # ------------------------------------------------------------
    # This function returns a formatted list of the courses for
    # which a student has registered.  
    # It has two parameters:
    # id is the ID of the student;
    # c_roster is the list of class rosters.
    # This function returns a formatted string.
    # ------------------------------------------------------------
    result = 'Courses registered:\n'
    count = 0
    for course in c_roster:
        if id in c_roster[course]:
            count += 1
            result += f'{course}\n'
    result += f'Total number: {count}\n'
    return result


def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.
    # It has two parameters:
    # id is the ID of the student;
    # c_roster is the list of class rosters.
    # This function has no return value.
    # -------------------------------------------------------------
    print(formatted_course_list(id, c_roster))

