total_age = 0
for students in students :
    total_age += (int(student['age']))
    average_age = total_age / len(students)
    print (f"Average students age is{average_age} years")

age = []
for students in students:
    age.apppend(int(students['age']))

print("otrais atrisinājums")
print(age)
print(sum(age) / len(ages))
    