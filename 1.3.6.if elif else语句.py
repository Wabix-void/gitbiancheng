import random
num_1 = random.randint(0,10)
if int(input("请猜一猜数字")) == num_1:
    print("恭喜你猜对了")
elif int(input("猜错了，请再猜一次")) == num_1:
    print("恭喜你猜对了")
elif int(input("猜错了，请再猜一次")) == num_1:
    print("恭喜你猜对了")
else:
    print("对不起，完全失败了，答案是%d"%num_1)