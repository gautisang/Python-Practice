# append(x)
print("APPEND")
fruits=["APPLE","ORANGE"]
print(fruits)
fruits.append("CHERRY")
print(fruits)

# extend(iterable)
print("EXTEND")
fruits=["APPLE","ORANGE"]
print(fruits)
fruits2=["CHERRY","BANANA"]
fruits.extend(fruits2)
print(fruits)

# insert(i,x)
print("INSERT")
fruits=["APPLE","ORANGE"]
print(fruits)
fruits.insert(2,"BANANA")
print(fruits)

# remove(x)
print("REMOVE")
fruits=["APPLE","ORANGE","BANANA","ORANGE"]
print(fruits)
fruits.remove("ORANGE")
print(fruits)

# pop(i)
print("POP")
fruits=["APPLE","ORANGE"]
print(fruits)
print(fruits.pop(0))

# clear()
print("CLEAR")
fruits=["APPLE","ORANGE"]
print(fruits)
fruits.clear()
print(fruits)

# index(x [, start[, end]])
print("INDEX")
fruits=["APPLE","ORANGE"]
print(fruits)
print(fruits.index("ORANGE"))

# count(x)
print("COUNT")
fruits=["APPLE","ORANGE","ORANGE"]
print(fruits)
print(fruits.count('APPLE'))

# sort(key=None, reverse=False)
print("SORT")
fruits=["APPLE","ORANGE","CHERRY"]
print(fruits)
fruits.sort(reverse=True)
print(fruits)

# reverse()
print("REVERSE")
fruits=["APPLE","ORANGE"]
print(fruits)
fruits.reverse()
print(fruits)

# # copy() #Shallow
print("COPY")
fruits=[["APPLE","BANANA"],["ORANGE"],["CHERRY"]]
fruits2=fruits.copy()
print(fruits)
print(fruits2)
fruits2[0][1]="BANANA_NEW"
print(fruits)
print(fruits2)

# len(list)
print("LEN")
amount=[20,30,10]
print(len(amount))

# min(list)
print("MIN")
amount=[20,30,10]
print(min(amount))

#max(list)
print("MAX")
amount=[20,30,10]
print(max(amount))

#sum(list)
print("SUM")
amount=[20,30,10]
print(sum(amount))