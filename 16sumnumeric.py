# find sum of numeric value in mixed list
l1 =[1,"a","name",1,3]
sums=0
for i in l1:
    if isinstance(i,(int,float)):
     sums+=i

print(sums)
      

