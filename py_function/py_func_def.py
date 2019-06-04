"""
定义函数：
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
"""
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-88))

"""
空函数：
想定义一个什么事也不做的空函数，可以用pass语句
"""
def nop():
    pass

"""
参数检查:
调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
"""

"""
返回多个值:
表项返回多个值，其实返回值是一个tuple
"""
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

t = move(100, 100, 60, math.pi / 6)
print(type(t))