# counter = 0 
# while counter < 5: 
#     print(f"Counter is {counter}")

#valiadate the age by user input

# age=input("Please input age")
# while not age.isdigit():
#     age=print("Invalid age")
#     age=input("Please input age again")

# print(f"Age is {age}")


#Sum user input until 0 entered
total=0
while True:
    number=int(input("Enter a number to add and enter 0 to stop : "))
    if number==0:
        break
    total+=number
print(f"sum is {total}")

 
