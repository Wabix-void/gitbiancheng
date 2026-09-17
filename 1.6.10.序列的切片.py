my_str = "万过薪月，员序程马黑来，nohtyP学"
result0 = my_str[0:3:] #元素从0开始下标
print (result0)
result1 = my_str[5:10:1]
print (result1)
result2 = result1[::-1]
print (result2)
result3 = my_str.split("，")
result6 = result3[1]
result4 = result6.replace("来","")
result5 = result4[::-1]
print(result5)
result10 = my_str.split("，")[1].replace("来","")[::-1]
print(result10)