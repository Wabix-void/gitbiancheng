student_year = [21,25,21,23,31,22,20]
print(student_year)
student_year.append(31)
print(student_year)
list1 = [29,33,30]
student_year.extend(list1)
print(student_year)
del student_year[0]
print(student_year)
student_year.pop(-1)
print(student_year)
x = student_year.index(31)
print(x)