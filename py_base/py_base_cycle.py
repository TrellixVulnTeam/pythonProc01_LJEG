"""
循环
"""
#for in
names = ["name01","name02","name03"]
for name in names:
    print(name)

"""
range()函数，生成一个整数序列，在通过list()转换为list。
"""
list01= list(range(5))
print(list01)

sum = 0
for x in range(101):
    sum += x
print(sum)

#while
sum = 0
n = 99
while n > 0:
    sum += n;
    n -= 2;
print(sum)

"""
break:提前退出循环
continue:跳过当前的这次循环，直接开始下一次循环
"""