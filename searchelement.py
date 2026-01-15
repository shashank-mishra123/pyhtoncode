# search for a number x in this unique tuple using loop 
# [1,4,9,16,25,36,49,81,100]
a = int(input("enter the number "))
l = (1,4,9,16,25,36,49,81,100)
indx =0
while indx <= len(l):
    if l[indx]==a:
        print("element are found ")
        break
    else:
        print("not found")
indx +=1
