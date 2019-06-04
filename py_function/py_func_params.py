"""
函数的参数
"""
"""
位置参数：传入的值安州位置顺序依次赋给参数
"""

"""
默认参数:
需要注意的问题：
1）必选参数在前，默认参数在后
2）函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
有多个默认参数时，调用的时候，既可以按顺序提供默认参数
也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
"""
def power(x,n=2):
    s = 1;
    while n > 0:
        n = n -1
        s = s * x
    return s

print(power(3))

"""
默认参数的坑！！！
"""
def add_end(L=[]):
    print("---: ",L)
    L.append('END')
    return L

print(add_end([1,2,3]))

print(add_end())#['END']
print(add_end())#['END', 'END']

"""
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
*** 定义默认参数要牢记一点：默认参数必须指向不变对象
"""

"""
可变参数：
可变参数就是传入的参数个数是可变的...允许传入0个或任意个参数
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple
"""
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2))
print(calc(1,2,3,4))

#如果已经有一个list或者tuple，要调用一个可变参数怎么办,可进行如下操作
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))

#上述写法太繁琐，Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*nums))

"""
关键字参数：
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

"""
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)

print(person("haha",30))

print(person('Bob', 35, city='Beijing'))

print(person('Adam', 45, gender='M', job='Engineer'))

"""
关键字参数作用：
扩展函数功能。
和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
"""
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('Jack', 24, **extra))

"""
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
对kw的改动不会影响到函数外的extra.
"""

"""
命名关键字参数:限制关键字参数的名字
例如，只接收city和job作为关键字参数
"""
def person(name, age, *, city, job):
    print(name, age, city, job)

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#命名关键字参数必须传入参数名，由于调用时缺少参数名，Python解释器把这4个参数均视为位置参数
# person('Jack', 24, 'Beijing', 'Engineer')   将报错！！！

"""
参数组合：
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""
