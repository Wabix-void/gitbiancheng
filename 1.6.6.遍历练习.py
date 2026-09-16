list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for num in list1:
    if num % 2 == 0:
        print(f"列表中的偶数有：{num}")
        list2.append(num)
print(f"列表二的最终值为:{list2}")



list3 = [1,2,3,4,5,6,7,8,9,10]
list4 = []
index = 0
while index < len(list3):
    num = list3[index]
    if num % 2 == 0:
            print(f"列表中的偶数有：{num}")
            list4.append(num)
    index += 1
print(f"列表四的最终值为:{list4}")