my_tuple=(1,2,3,"hello")
print(my_tuple)
#count

my_tuple=(1,2,3,4,1,2,4,1)
print(my_tuple.count(1))
#index
my_tuple=(1,2,3,4,1,2,4,1)
print(my_tuple.index(4))

#len
my_tuple=(1,2,3,4,1,2,4,1)
print(len(my_tuple))
#min
my_tuple=(1,2,3,4,1,2,4,1)
print(min(my_tuple))
#max
my_tuple=(1,2,3,4,1,2,4,1)
print(max(my_tuple))
#sum
my_tuple=(1,2,3,4,1,2,4,1)
print(sum(my_tuple))
#sorted
my_tuple=(1,2,3,4,1,2,4,1)
print(sorted(my_tuple))


# How to modify tuple
my_tuple=(1,2,3,4,1,2,4,1)
temp_list=list(my_tuple)

temp_list.append(10)
print(temp_list)

my_tuple=tuple(temp_list)
print(my_tuple)

#
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)
t4=t1*3
print(t4)