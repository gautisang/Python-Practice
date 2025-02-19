name='Jhon'
print(name)

_age=30
print(_age)

print("Hello ",name)
print("age is ",_age)

x=10
print(id(x))
x=x+1
print(id(x))

my_list=[1,2,3]
print(id(my_list))
my_list.append(4)
print(id(my_list))


a=[1,2,3]
b=a
b.append(4)
print(a)
print(b)
print(id(a))
print(id(b))
