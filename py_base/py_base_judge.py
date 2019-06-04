"""
条件判断
"""
#if
age = 20
if age >= 18:
    print("age is ",age)

#if-else
if age >= 18:
    print("adult")
else:
    print("teenager")

#if-elif-else
age = 5
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

print("-----------------------------")
birth = input("birth:")
birth = int(birth)
if birth < 2000:
    print("00前")
else:
    print("00后")


