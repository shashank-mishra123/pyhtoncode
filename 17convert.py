# convert tuple to list and remove even number
tu = (1,2,3,4,5,6,7,8,9)
l1 =list(tu)
list2 =[]
for i in range(len(l1)):
   if(i%2!=0):
      list2.append(i)
print(list2)