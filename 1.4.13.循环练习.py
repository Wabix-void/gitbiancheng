import random
money = 10000
for people in range(1,21):
    if money < 1000:
                print("本月工资已发完，下个月再来领取吧")
                break
    jixiao = random.randint(1,10)
    if jixiao >= 5:
        money -= 1000
        print(f"员工{people}发放工资1000元，账户余额还剩{money}元")
    else:
        print(f"员工{people},绩效分{jixiao},低于5，不发工资，下一位")



b=10000
for x in range(1,21):
      jixiao = random.randint(1,10)
      if jixiao < 5:
            print(f"员工{x},绩效分{jixiao},低于5，不发工资，下一位")
            continue
      if b >= 1000:
            b -= 1000
            print(f"员工{x}发放工资1000元，账户余额还剩{b}元")
      """else:
                  print("本月工资已发完，下个月再来领取吧")
                  break
                代码不能及时停止循环，改为第三个if后解决"""
      if b < 1000:
            print("本月工资已发完，下个月再来领取吧")
            break