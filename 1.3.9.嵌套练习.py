import random
num = random.randint(0,10)
print("猜字游戏，一共三次机会，请猜出答案")
num_1 = int(input("请猜测数字"))
if num_1 == num:
    print("恭喜你，一次就猜对了")
else:
    if num_1 > num:
        print("大了")
    else:
        print("小了")
    num_2 = int(input("请第二次猜测数字"))
    if num_2 == num:
        print("恭喜你，两次就猜对了")
    else:
        if num_2 > num:
            print("大了")
        else:
            print("小了")
        num_3 = int(input("请第三次猜测数字"))
    if num_3 == num:
         print("恭喜你，终于猜对了")
    else:
        print("很遗憾，猜错了，答案是：%d"%num)