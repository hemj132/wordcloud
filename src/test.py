#coding=utf-8


#在生成器表达式中, in 子句在声明时执行, 而条件子句则是在运行时执行.
array = [1, 8, 15]
#生成器
g = (x for x in array if array.count(x) > 0)
l=[ x for x in array if array.count(x) > 0]
array = [2, 8, 22]
print g
print l
print(list(g))