# The purpose  of this console application is to use file-based storage system
# We will create "student.json" file to store the information of the students.
# We will CRUD(Create, Retrieve, Update, Delete) in students.json file.


from create import create_student
from read import  read_student
from update import update_student
from delete import delete_student

def inquiry():
    selection = input("Select your choice c/r/u/d/e ")
    selection = selection.lower()


    def exit_message():
        print("Thank you. See you again")
    if selection == "c":
        repeat = create_student()
        inquiry() if repeat else exit_message()
    elif selection == "r":
        student_id = input("Enter the student id")
        inquiry() if repeat else exit_message()
        read_student()
    elif selection == "u":
        update_student()
    elif selection == "d":
        delete_student()
    else:
        exit_message()

if __name__ == "__main__":
    inquiry()
