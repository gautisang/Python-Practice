# dict[key]=value
my_dict={"name":"Jhon","age":30}
print(my_dict)
my_dict["age"]=35
print(my_dict)

# update(iterable)
my_dict={"name":"Jhon","age":30}
print(my_dict)
my_dict.update({"city":"New York","age":40})
print(my_dict)

# get(key, default=None)
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.get("name1","Unknown"))

# pop(key, default=None)
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.pop("name1","Unknown"))
print(my_dict)

# popitem()
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.popitem())
print(my_dict)
# del
my_dict={"name":"Jhon","age":30}
print(my_dict)
del my_dict["name"]
print(my_dict)
del my_dict
print(my_dict)

# clear()
my_dict={"name":"Jhon","age":30}
print(my_dict)
my_dict.clear()
print(my_dict)

# in (key in my_dict)
my_dict={"name":"Jhon","age":30}
print(my_dict)
print("name1" in my_dict)

# copy()
print("**copy")
my_dict={"name":"Jhon","age":30}
print(my_dict)
new_dict=my_dict.copy()
print(new_dict)

# setdefault(key, default=None)
print("set default")
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.setdefault("age1",50))
print(my_dict)


# Iterating over a dict
my_dict={"name":"Jhon","age":30}
print(my_dict)

# keys()
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.keys())

# values()
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.values())

# items()
my_dict={"name":"Jhon","age":30}
print(my_dict)
print(my_dict.items())
for key,val in my_dict.items():
    print(key)
    print(val)


# Builtin Functions
# len(dict)
my_dict={"name":"Jhon","age":30}
print(len(my_dict))
# min(dict), max(dict)
my_dict={"name":"Jhon","age":30}
print(min(my_dict))
my_dict={"name":"Jhon","age":30}
print(max(my_dict))
# sorted(dict)
my_dict={"name":"Jhon","age":30}
print(sorted(my_dict))