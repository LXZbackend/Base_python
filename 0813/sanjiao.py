#coding=utf-8
#打印三角形第一种方法
'''
i=1
while i<=5:
    print("*"*i)
    i+=1
'''

i = 1
while i<=5:

    j=0
    while j<i:
        print'*',
        j+=1
    print('')
    i+=1
