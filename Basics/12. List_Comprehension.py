squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in range(1,6)]
print(squares)

# Filtering Even Numbers:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)



multiples=[]
for i in range(1,6):
    intermidiate_list=[]
    for j in range(1,6):
        intermidiate_list.append(i*j)
    multiples.append(intermidiate_list)

print(multiples)  


multiples = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(multiples)


words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)