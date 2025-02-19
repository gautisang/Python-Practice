my_list=[10,20,30,40,50,60,70,80]

#Slice from index 2 to 5,skip 5
print(my_list[2:5]) #5-1
#Start from 3 to the end
print(my_list[3:]) 
#from beginning to index 5
print(my_list[:5]) #5-1
#Using steps
print(my_list[0::3]) 
#reverse list
print(my_list[::-1]) 
#start from 2nd last element till the end
print(my_list[-2:]) 
print(my_list[6:]) 

sales=[15000,18000,21000,24000,20000,22000,23000,25000,27000,29000,30000,32000]

#first quarter sale

print(sales[0:3]) 


#last quarter sale
print(sales[-3:]) 
print(sales[9:]) 
print(sales[::2]) 
print(sales) 
print(sales[::-1]) 

