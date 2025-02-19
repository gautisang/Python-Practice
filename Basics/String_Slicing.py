#First Few characters
text="PYTHON IS FUN"
print(text[0:3])
print(text[3:7])
print(text[3:]) #Till the end
print(text[:4]) #Start from 0


#Negative index
print(text[-1:-5:-1]) #NUF
print(text[-3:]) #NUF
print("***")


#Slicing with steps
print(text[3::2]) #HNI U
print(text[3::3]) #H  N
print(text[-1:-8:-2]) #NFS

#Reverse string
print(text[::-1])

#Extract middle sections of a string
#Extracting substring from date input
my_date="2025-01-11"
print(my_date[0:4])
print(my_date[5:7])
print(my_date[8:])
print(my_date[-2:])
print(my_date[my_date.index("-")+1:7])
print(my_date[my_date.rindex("-")+1:])

#Get file extension from filename
file_name="abc.pdf"
print(file_name[file_name.index(".")+1:])
print(file_name[-3:])

#Get domain name from emailid
emailid="xyz@gmail.com"
print(emailid[emailid.index("@")+1:])
print(emailid[0:emailid.index("@")])
#Get the countrycode from contact
contact="123-456-789"
print(contact[0:3])

#Palindrom checks
text="madam"
print(text==text[::-1])