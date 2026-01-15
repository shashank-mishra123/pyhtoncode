# find comman element between two list

l1 = [ 1,2, 3,4,6]
l2 = [ 7,8, 3,9,0]
# change into set both 
set1 =set(l1)
set2 =set(l2)

# then intersection 
set3 = list(set1.intersection(set2))
print(set3)