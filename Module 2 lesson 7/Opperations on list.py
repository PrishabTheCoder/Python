classmates=["aarav","priya","rahul","sneha","dev"]
print("class list:", classmates)

print("total students:", len(classmates))
print("first student:", classmates[0])
print("last student:", classmates[1])
print("first three:", classmates[:3])

classmates.append("meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("dev")
print("after removing dev:", classmates)
classmates.sort()
print ("sorted alphabetically", classmates)
classmates.reverse()
print("reversed:", classmates)

teacher = {"name":"Mr. Kumar", "subject": "Python", "experience":5 }
print("\nteacher profile:", teacher)

print("subject:",teacher["subject"])
print("experience:", teacher.get("experience", "not found"))
teacher["experience"] = 6
teacher["email"] = "prishabshrestha123@gmail.com"
teacher.pop("experience")
print("updated teacher profile", teacher)

roll_numbers = [1,2,3,4,5]
names = ["aarav","priya","rahul","sneha","meera"]
student_directory = dict(zip(roll_numbers, names))
print("\nstudent directory", student_directory)
print("student at roll 3:", student_directory[3])