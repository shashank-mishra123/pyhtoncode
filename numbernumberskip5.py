# print the number for skipping multiple 5 to 100
number = int(input("enter the numbers"))
indx = 1
while indx < number:
    if indx %5 != 0:
        print(indx)
    indx +=1