#break

for i in range(5): #0 to 4
    if i==3:
        break
    print(i)

#continue
print("continue")
for i in range(5): #0 to 4
    if i==3:
        continue
    print(i)

#pass

print("pass")
for i in range(5): #0 to 4
    if i==3:
        pass
    print(i)


#
# correct_pass="123"
# for i in range(3):
#     password=input("Enter the pass")
#     if password==correct_pass:
#         print("Access granted")
#         break
#     else:
#         print("try again")
# else:
#     print('Too many failed attempts')

users=[
    {"name":"A","status":"active"}, #0
    {"name":"B","status":"inactive"}, #1
    {"name":"C","status":"active"} #2
]

for user in users:
    if user["status"]=="inactive":
        continue
    print(f"Generatig report for {user['name']}")

#pass

def process_payment():
    pass

def send_email():
    print("sent email")