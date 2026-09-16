s = (input("请输入数组，逗号隔开："))
nums = [int(i) for i in s.split(",")]
target = int(input("请输入结果："))
for x in nums:
    y = target - x
    if y in nums:
        print([x,y])
        break


#在力扣诞生的第一串史山代码
# for x in nums:
#             p = nums.index(x)
#             del nums[p]
#             y = target - x
#             if y in nums:
#                 q = nums.index(y) + 1
                                   # debug加入：  nums.insert(p,x)
#                 return [p,q]
#             else:
#                 nums.insert(p,x)