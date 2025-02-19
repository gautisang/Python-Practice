#Basic data type
#int
age=30
print(type(age))

#float
amount=12.2
print(type(amount))

#string
name="Jhon"
print(type(name))

#List
fruits=["Apple","Orange"]
print(type(fruits))
print(id(fruits))
print(fruits)
#Mutable
fruits.append("Banana")
print(type(fruits))
print(id(fruits))
print(fruits)

#tuple
fruits=("Apple","Orange")
print(type(fruits))
print(id(fruits))
print(fruits)

#Immutable
fruits+=("Banana",)
print(type(fruits))
print(id(fruits))
print(fruits)


#dict

record={"name":"Jhon","age":30}
print(type(record))
print(id(record))
print(record)
#Mutable
record["address"]="US"
print(type(record))
print(id(record))
print(record)

#set
fruits={"Apple","Orange"}
print(type(fruits))
print(id(fruits))
print(fruits)
#mutable
fruits.add("Banana")
print(type(fruits))
print(id(fruits))
print(fruits)

#Frozenset
fruits=frozenset(["Apple","Orange"])
print(type(fruits))
print(id(fruits))
print(fruits)

#Immutable
fruits=fruits.union(['Banana'])
print(type(fruits))
print(id(fruits))
print(fruits)

#
is_school=True
print(type(is_school))
print(id(is_school))
print(is_school)

name=None
print(type(name))
print(id(name))
print(name)
