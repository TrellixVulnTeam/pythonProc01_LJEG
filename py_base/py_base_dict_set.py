"""
字典：dict
使用键值对存储
一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
dict内部存放的顺序和key放入的顺序是没有关系的.
dict的key必须是不可变对象.
key不存在，dict就会报错,可以通过in判断key是否存在
"""
dict01= {"name01":65,"name02":70,"name03":80}
print(dict01["name02"])

if "name04" in dict01:
    print("Yes")
else:
    print("No")

#dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
val = dict01.get("name05",100)
print(val)

#删除一个key，用pop(key)方法，对应的value也会从dict中删除
dict01.pop("name03")
print(dict01)

"""
与list相比较：
dict：  查找和插入的速度极快，不会随着key的增加而变慢；
        需要占用大量的内存，内存浪费多。
list：  查找和插入的时间随着元素的增加而增加；
        占用空间小，浪费内存很少。
"""

print("------------------------------------------------------")
"""
set:
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
显示的顺序也不表示set是有序的,重复元素在set中自动被过滤
"""
set01 = set([1,1,2,3])
#print(set01)

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
set01.add(6)
set01.add(6)
#print(set01)

#通过remove(key)方法可以删除元素
set01.remove(3)
#print(set01)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

set03 = set([(1,2,3),4,5])
print("set03:  ", set03)

set04 = set([(1,(2,3)),4,5])
print("set04:  ",set04)