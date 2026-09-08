name = "大学"
year = 1352
student_num = 1.376
message  = "这所%s成立于%d年，现在有%f万学生"%(name,year,student_num)
print(message)
message  = "这所%s成立于%d年，现在有%.2f万学生"%(name,year,student_num)
print(message)
num = 11.366
print("宽度8，小数精度2，结果是：%8.2f"%num)
print("宽度1，小数精度2，结果是：%1.2f"%num)