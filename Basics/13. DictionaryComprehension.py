squares = {}
for i in range(10):
    squares[i] = i ** 2

print(squares) 


squares={x:x**2 for x in range(10)}
print(squares)

even_squares = {n: n**2 for n in range(10) if n % 2 == 0}
print(even_squares)

#Create a dictionary where each key holds another dictionary with squares of the numbers.

nested_dict={x: {y:y**2 for y in range(3)}  for x in range(3)}
print(nested_dict)

square={x: (x**2 if x % 2 == 0 else 0) for x in range(5) } 
print(square)

import time

start_time = time.time()
squares = {i: i**2 for i in range(100000000)}
end_time = time.time()
print(end_time-start_time)


###############
start_time = time.time()
squares = {}
for i in range(100000000):
    squares[i] = i ** 2
end_time = time.time()
print(end_time-start_time)

even_squares = {}
for i in range(10):
    if i % 2 == 0:
        even_squares[i] = i ** 2

even_squares = {i: i**2 for i in range(10) if i % 2 == 0}













