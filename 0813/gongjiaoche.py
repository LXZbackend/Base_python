#coding=utf-8
import random
# 设置一个公交座位变量seat，用随机数生成
seat = random.randint(0,10)
# 变量balance用于存储公交余额
balance =input("请输入公交卡余额:")
if balance >= 2:
    
    print('滴，老司机卡')
    if seat != 0:
        print ("车上有位子，你可以坐下来休息")
    else:
        print("没位子了，你只能站着了")
else:
    print("穷鬼！请下车")
