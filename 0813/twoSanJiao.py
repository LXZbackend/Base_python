#coding=utf-8
#第一种方法 用*这个方法来实现
'''

i = 1
while i<=5:
    print('*'*i)
    i+=1
# 注意 这里面print是查看上面循环后i的值，因为循环后他的值变成6了
#print ('%d'%i) 

#  下面的代码是逐渐减少*的输出 
if i == 6:
    while i>=1:
        print('*'*(i-2))# 这减去2是改变i的初始值

        i-=1



'''

'''
#第二种方法 利用while 的嵌套实现。外面一层循环控制行数，里面的循环控制每行打印的个数 
i = 1
while i<=5:#这个5的意思是 第一次循环有5行  
    j = 0   #这是控制第一行实现的循环变量
    
    while j<i: #这是实现啊每行控制的个数
        print('*'), # 当print() 后面加一个，号 就会取消换行
        j+=1
    print('')#当每行打印后 换行
        
    i+=1

#
j=4   #这是从第六行开始递减的打印星星
while j>=0:
    k=1
    while k<=j:
        print('*'),
        k+=1
        
    print('')

    j-=1

'''



i = 0
while i<5:   
    j=0
    while j<i:
        print('*'),

        j+=1
    print('')


    i+=1













