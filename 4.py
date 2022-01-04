#taking input from user
students=[]
print("Plz give marks as Input\n")
for i in range(0,5):
    element=int(input())
    students.append(element)

#sorting the marks of the students
students.sort()

#seperating input from output
print("*************************")

#printing the sorted result
print(*students,sep="\n")