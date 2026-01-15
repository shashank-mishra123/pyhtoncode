# remove duplicate element from a list without using set()

l = [1,2,3,2,7,4,3,2,1]
list1 = []
for i in range(len(l)):
    if l.index(l[i])==i:
        list1.append(l[i])
print(list1)
     


