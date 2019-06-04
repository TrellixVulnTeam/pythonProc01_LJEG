"""
list和tuple
"""

"""
list:有序的列表
可随时增删元素
"""
classnames = ['name1','name2','name3']
print(classnames)

#len()获取list元素个数
print(len(classnames))

#索引访问list元素，索引从0开始,若越界，则报错IndexError
print(classnames[0],classnames[2])

# -1：获取最后一个元素，-2获取倒数第二个。。。。
print(classnames[-2],classnames[-3])

#list 是可变的有序表，可以使用append往list的末尾追加元素
classnames.append('name04')
print(classnames)

#也可以在指定的位置插入:insert
classnames.insert(1,"name00")
print(classnames)

#删除末尾的元素：pop
classnames.pop()
print(classnames)

#删除指定位置的元素：pop(i)
classnames.pop(1)
print(classnames)

#替换指定位置元素，直接使用赋值
classnames[1] = 'haha'
print(classnames)

#list里面的元素的数据类型也可以不同
list01 = [1,'a',True,2.14]
print(list01)

#list元素也可以是另一个list
list02 = [1,[2,3],['a','b']]
print(list02)
print("list02->len",len(list02))
print(list02[1][1])
print(list02[2][0])

#如果一个list中一个元素也没有，就是一个空的list，它的长度为0
print("-----------------------------------------------------------------------------------");
"""
tuple:有序、但初始化后不允许被修改！
没有append、insert方法，无法赋值，获取元素方法与list相同。
当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
如果要定义一个空的tuple，可以写成t=()
*定义一个只有1个元素的tuple：若写成t=(1)则表示1这个数，并非tuple。正确的写法是t=(1,).
 因为()可以表示tuple，也可以表示小括号，产生歧义，Python规定该情况下表示小括号
"""
tuple01 = ('tpval01','tpval02','tpval03')

print(tuple01[1])
"""
tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
"""
