# Python-Code
This program creates a class registration system.  Students log into the class registration system and then they can add courses, drop courses, and list the courses for which they have registered.

This program has 6 functions in 3 modules: a student module, a billing module, and a main module.

There are 4 students in this program.  ID and PIN of students are stored as tuples in student_list.  The first element of each tuple is student ID and the second element is the PIN.

Students that are in-state are stored in the student_in_state dictionary. Students 1001 and 1003 are in-state students.

Four courses are offered. Each course has a number of credit hours. The courses and credit hour information are stored in course_hours: 
•	CSC101 has 3 credit hours. 
•	CSC102 has 4 credit hours. 
•	CSC103 has 5 credit hours. 
•	CSC104 has 3 credit hours.

The maximum class size of the courses offered are stored in course_max_size.  The max sizes of CSC101, CSC102, CSC103, and CSC104 are 3, 2, 1, and 3 respectively.

Rosters of the four classes offered are stored as four lists which are values of the course_roster dictionary:  
•	Students 1004 and 1003 are enrolled in CSC101.  
•	Student 1001 is enrolled in CSC102.  
•	Student 1002 is enrolled in CSC103. 
•	No one is enrolled in CSC104.

The data given above must be used in the program as specified above. Any changes to how the data is structured must be proposed as a specification change to the instructor and approved by the instructor.

The program should have a loop to create multiple student sessions.  In each session, ask the user to enter an ID, then call the login function to verify the student’s identity.  If login is successful, use a loop to allow the student to add courses, drop courses, list courses registered, or display a bill.

