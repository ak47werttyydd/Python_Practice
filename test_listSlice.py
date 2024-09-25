# pattern = [1,2,3]
# print(pattern[3:]) #[]
#
# lst1=['hello','world',123,98,6,"world",125,"world"]
# # print(lst1.index("world"),)
# print(lst1.index("world",6,7))

# lst=[10,20,30,40,50,60,70,80]
# # print(lst[9])
# print(lst[:3:-4])
#
# lst=[1,2,3]
# def fun(lst_in):
# 	lst_in[0]=2
# fun(lst)
# print(lst)

# lst=[1,2,3,4,5]
# lst2=lst[2:]  #切片作为右值的时候，原列表不会改变
# print('lst=',lst)
# print('lst2=',lst2)
#
# lst3=[100,200,300]
# lst[2:]=lst3  #切片作为左值的时候，原列表被改变
# #lst[2:2]=100  出错，因为切片作为左值只能由迭代体赋值
# print('lst=',lst)
# print(3 not in lst)
#
# lst=[10,20,30]
# lst.append(100)  #尾部追加元素   ,id不变，还是同一个列表
# print(lst)
# lst2=['hello','world']
# lst.append(lst2)  #把整个lst2放到lst[4]中
# print(lst)

# lst=[10,20,30]
# lst2=['hello','world']
# lst.extend(lst2)
# print(lst)
# #or
# lst=[10,20,30]
# lst3=lst+lst2
# print(lst3)

# lst=[10,20,30]
# lst4=lst*2
# print(lst4)

# list = [[i+j for i in range(2)] for j in range(4)]
# print(list)

# lst=[10,20,30,40,50,60,30]
# del lst[0]
# print(lst) #删除第一个元素

# #删除某个键值对和清空字典
# scores=dict(张三=99,a=110,age=330)
# del scores['张三']  #删除'张三'和对应的值
# print(scores)
#
# del scores  #删除字典
# print(scores)
#
# scores=dict(张三=100,李四=98,王五=45)
# for i in scores: #i is key
#   print(i,scores[i],scores.get(i))   #左边为键，中间为值，右边为值

# def fun():
#   n2.append(1)
#   return
#
#
# n2 = [22, 33, 44]
# print('n2原始值=', n2)
# fun()  #
# print('新的n2=', n2)

# x=1
# y=1
# if x==y:
#   z=x
# p=z
# print(p)
#
# s4='hello world python'
# lst4=s4.rsplit() #default delimeter is space
# print(lst4)
#
# lst5=s4.rsplit(maxsplit=1) #default delimeter is space
# print(lst5)

# #转成大写
# s='WasadaaaAAA'
# print('s.upper() is: ',s.upper())
# print('s is: ',s)
#
# #转成小写
# s='WasadaaaAAA'
# print('s.lower() is: ',s.lower())
# print('s is: ',s)

# str = "this is string example....wow!!! this is really string"
# print(str.replace("is", "was"))  #左参数是原字符串，右参数是新字符串
# print(str.replace("is", "was", 3)) #左参数是原字符串，右参数是新字符串，3表示最多替换3个
# print(str.replace("is", "wassss", 2)) #左参数是原字符串，右参数是新字符串，3表示最多替换3个
# print(str)    #str本身没有改变，说明需要创建一个str1=str.replace()

# def fun1(l1, l2):
#   l1.append(1)
#   l2 = [1, 2, 3]  # Creates a new local list variable, doesn't modify the original list2

# def fun2(l1, l2):
#   l2[::1] = [1, 2, 3]  #change list2
#
#
# list1 = [9, 8, 7]
# list2 = [9, 8, 7]
#
# print("Before fun1, list1 is:", list1, " list2 is: ",list2)
# fun1(list1, list2)
# print("After fun1, list1 is:", list1, " list2 is: ",list2)
#
# print("Before fun2, list1 is:", list1, " list2 is: ",list2)
# fun2(list1, list2)
# print("After fun2, list1 is:", list1, " list2 is: ",list2)

# def fun(*arg):  # *arg是个数可变的位置参数，arg是元组
#   for idx,item in enumerate(arg):
#     print(f'arg[{idx}]=', item, end='\040')
#   print()
#
#
# tuple1 = ('Python', 'is', 1, 2, 3)  # tuple1是元组
# fun(*tuple1)  # *tuple1是位置参数

#funA 作为装饰器函数
# def funA(fn):
#     print("C语言中文网")
#     fn() # 执行传入的fn参数
#     print("http://c.biancheng.net")
#     return "装饰器函数的返回值"
# @funA
# def funB():
#     print("学习 Python")
#
# a=funB
# print('a is ',a)

#先建立两个列表
# items=['Fruits','Books','Others']   #存keys的列表
# prices=[96,78,85]     #存values的列表
# items_prices=list(zip(items,prices))
# print("is ",items_prices[1][0]," price is ",items_prices[1][1],"?")

# print(type(format(255, 'b'))) # base 10 to base 2
# print(format(010,'d'))

# lst=[1,2,3]
# def fun():
# 	lst[0]=2
# fun()
# print(lst)#[2,2,3]