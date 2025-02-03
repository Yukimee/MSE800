# Activity:  ==== write a module/ simple code including one class and assign two objects to that class.
# Then, print the initial value of those two objects.

class Student:

    def __init__(self, student_name, student_email):
        self.student_name = student_name    
        self.student_email = student_email 

        pass

    def display_info(self):

        print(f"Student: {self.student_name}, Email:{self.student_email}")



student1 = Student("Lee", "lee@gmail.com")
student1.get_student_info 