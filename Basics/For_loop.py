#Iterating over a list
fruits=['apple','orange','cherry']
for fruit in fruits:
    print(fruit)

#Using range
for i in range(10): # 0-9
    print(i)
print("*****")
for i in range(1,10,2): # 1-9
    print(i)

#Iterating over a Dictionary
my_dict={'name':'Rahul','age':30,'city':'Banglore'}
for key,value in my_dict.items():
    print(key,value)

#zip
names=["Rahul","Vijay"]
scores=[70,90]
for name,score in zip(names,scores):
    print(name,score)

#Iterating over a String
my_string='Python'
for item in my_string:
    print(item)

#Nested Loops
matrix=[[1,2,3],[4,5,6],[7,8,9]] #list of list
fruits=['apple','orange','cherry']


for row in matrix:
    print(row)
    for num in row:
        print(num)

#else
for fruit in fruits:
    print(fruit)
else:
    print("Loop completed")

#enumerate
for item in  enumerate(fruits):
    print(item)
for index,fruit in  enumerate(fruits):
    print(f"Index {index}:{fruit}")
    
