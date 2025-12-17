# Create a function for school admission system. 
# A student can apply for admission by providing their name, age, email, grade
# The function should check if the student is eligible for admission based 
# on grade
# If the student is eligible, 
# the function should return a message saying "Congratulations {name}, 
# you have been admitted to our school"
# If the student is not eligible, the function should return a message saying
#  "Sorry {name}, you are not eligible for admission"
# If the student is eligible, the function should also return the student's 
# profile which includes their name, age, email, and grade.
# If the student is not eligible, the function should not return the profile.
# The function should also store the student's profile in a local storage
# (a dictionary) if they are eligible for admission.


def admission_system(name, age, email, grade):
    eligible_grades = ['A', 'B', 'C']
    student_profile = {
        "name": name,
        "age": age,
        "email": email,
        "grade": grade
    }
    if grade in eligible_grades:
        return f"Congratulations {name}, you have been admitted to our school"
    else:
        return f"Sorry {name}, you are not eligible for admission"

name=input("Enter your full name: ")
age=int(input("Enter your age: "))
email=input("Enter your email: ")
grade=input("Enter your grade (A, B, C, D, E, F): ")
result = admission_system(name, age, email, grade)
print(result)

