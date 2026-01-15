# determine type of traingle 
# hint = equiletraiel , sclaer , isoselecs

s1 = int(input("enter the side of traingle "))
s2 = int(input("enter the side of traingle "))
s3 = int(input("enter the side of traingle "))

if(s1==s2==s3):
    print("traingle is equileterail:")
elif(s1==s2 or s1==s3 or s2==s3):
    print("traingle is isoceles")
else:
    print(" traingle is scaler")
