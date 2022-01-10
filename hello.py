# -*- coding: UTF-8 -*-
# if 条件判断
# if (True):
#     total = r'H\n' + \
#     'e' + 'llo';
#     print(total);
# else:
#     print('false');

# 字符串
# str='123456789'
# print(str[0:])
# x="a"
# y="b"

# 不换行输出
# print( x, end=" " )
# print( y, end=" " )

#  定义变量
# a, b, c = 1, 2,"runoob"
# e = f = g = 1
# print(a,b,c);
# print(e,f,g);

# 列表
# list =[1,2,3,4,5,6]
# print(list[1:0])

# 元祖
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
# print(tinytuple*2)
# print(tuple[0])
# print(tuple[0:2])
# print(tuple*2)
# tuple[0]=1;  does not support item assignment


# 集合
# person = {1,2};
# print(person)

# 字典
'''
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict['name'])
print(tinydict.keys())
print(tinydict.values())
'''

# in not in 
'''
a=1;
b=10
list = [1,2,3,4,5];
'''

'''
if(a in list):
    print('a in list');
else:
    print('a not in list');
'''
'''
if(b not in list):
    print('b not in list');
else:
    print('b in list');
'''


# id()

# a=b=1;
# if(id(a)==id(b)):
#     print('a==b');
# else:
#     print('a!=b');    



# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
 
# ### 退出提示
# input("点击 enter 键退出")


# while
# i=0
# while(i<10):
#     print(i);
#     i+=1;
# else:
#     print('while 执行完毕')


# 函数
# def maxNum(a,b):
#     if(a>b):
#         return a;
#     else:
#         return b;  

# result = maxNum(100,2);
# print(result)

# 随机数
# import random
# print(random.randint(7,9))

# 计算每个月天数

# import calendar
# monthRange = calendar.monthrange(2020,12)
# print(monthRange[1])

# str1 = 'hello python';
# print(str1);
# lis = [1,2,3]
# print(lis[0]);
#
# arr = {1,2,3,4,4,5,5}
# print(arr)
#
# obj1={'name':'张三','age':18};
# print(obj1)
#
# tup =('Google',);
# print(tup);

# arr= [44,55,88]
# for item in arr:
#     print(item)

# lis = {'1','2','star'}
# for item in lis:
#     print(item)


# arr =range(1,11);
# for item in arr:
#     print(item)

# sum=0;
# n=0;
# while(n<5):
#     sum=sum+n;
#     n+=1;
#     print('sum:',sum);
#     print('n:',n);

# str1= '11213';
# print(type(str1))
# print(int(str1)+11)

# f = open("H:\python/tmp/foo.txt", "a+")
# f.write( "Python \n")
# # 关闭打开的文件
# f.close()

# from datetime import date
# now = date.today()
# print(now)


# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')
# # 求和
# sum = float(num1) + float(num2)
# print(sum)

# lis = [1,2,3,4,88,88,88]
# print(lis.count(1))
# print(len(lis))
# print(max(lis))
# print(min(lis))
# print(lis.index(88,-1))
