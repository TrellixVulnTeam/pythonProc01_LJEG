"""
字符串与编码
"""

"""
UNICODE:
Unicode把所有语言都统一到一套编码里.
最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）.
如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
UTF-8编码:
可变长编码。
UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
"""

"""
总结“
计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
"""

"""
Python 字符串
最新的Python 3版本中，字符串是以Unicode编码的，其支持多语言。
单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符。
如果知道字符的整数编码，还可以用十六进制写字符串
"""
print(ord('A'))
print(ord('a'))
print(chr(65))
print('\u4e2d\u6587')

"""
Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示
'ABC'与b'ABC':
前者为str，后者为bytes，bytes的每个字符都只占用一个字节。
以Unicode表示的str通过encode()方法可以编码为指定的bytes
要把bytes变为str，就需要用decode()方法
"""
str01 = 'ABC'
bstr01 = str01.encode('ascii')
str02 = "中文"
bstr02 = str02.encode('utf-8')
print(str01,bstr01)
print(str02,bstr02)

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
bstr03 = b'\xe4\xb8\xad\xff'
str03 = bstr03.decode("utf-8",errors='ignore')
print(bstr03,str03)
#要计算str包含多少个字符，可以用len()函数
print(len('acb'))
print(len("你好"))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len("中文".encode('utf-8')))

"""
格式化：用%实现。
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
1）格式化整数和浮点数还可以指定是否补0和整数与小数的位数
2）如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
3）字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
"""
print('%2d -- %02d' % (3,1))
print('%.2f' % 3.1415926)
print("haha is %s and %d" % ('nihao',25))
print("lele %d%%" % 20)

"""
format()方法：
它会用传入的参数依次替换字符串内的占位符{0}、{1}……，与%相比要麻烦一些。
"""
print("Hello,{0} > {1:02}".format('2',1))
print("xiaoshu {0:.2f}".format(3.1415))