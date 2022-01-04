#taking input from user
SID=int(input("SID-"))
Name=input("Name-")
Gender=input("Gender(F,M orU)-")
Course_name=input("Course name-")
Course_name=Course_name.upper()
CGPA=float(input("CGPA-"))

#storing all the collected data into a list
student=[SID,Name,Gender,Course_name,CGPA]

#printing the data to check the program
print(student)