student = ('周杰轮',11,['football','music'])
num = student.index(11)
print(num)
name = student[0]
print(name)
del student[2][0]
print(student)
student[2].append('coding')
print(student)