# add(x)
my_set={1,2,3}
print(my_set)
my_set.add(4)
print(my_set)

# update(iterable)

my_set={1,2,3}
print(my_set)
my_set.update([4,5])
print(my_set)
# remove(x)

my_set={1,2,3,4}
print(my_set)
my_set.remove(3)
print(my_set)

# discard(x)
my_set={1,2,3,4}
print(my_set)
my_set.discard(5)
print(my_set)

# pop()
my_set={1,2,3,4,5}
print(my_set)
print(my_set.pop())


# clear()
my_set={1,2,3,4}
print(my_set)
my_set.clear()
print(my_set)
# copy()
my_set={1,2,3,4}
print(my_set)
my_set2=my_set.copy()
print(my_set2)

# Union or |
my_set1={1,2,3,4}
my_set2={6,7}
my_set3=my_set1.union(my_set2)
print(my_set3)
# intersection() or &

my_set1={1,2,3,4}
my_set2={6,7,5,1,2}
my_set3=my_set1.intersection(my_set2)
my_set3=my_set1 & my_set2
print(my_set3)
# Difference or -

my_set1={1,2,3,4}
my_set2={6,7,5,1,2}
my_set3=my_set1.difference(my_set2)
my_set3=my_set1 - my_set2
print(my_set3)

#comparision

# issubset
my_set1={1,2}
my_set2={6,7,5,1,2}
print(my_set1.issubset(my_set2))

# issuperset
my_set1={1,2,3,4}
my_set2={3,4,5}
print(my_set1.issuperset(my_set2))
# isdisjoint

my_set1={1,2,3,4}
my_set2={5}
print(my_set1.isdisjoint(my_set2))

#
my_set1={11,1,2,3,4,10}
print(len(my_set1))
print(max(my_set1))
print(min(my_set1))
print(sum(my_set1))
print(sorted(my_set1))