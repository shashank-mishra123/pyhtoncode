# check whether traingle is valisd or not 
# hint = s1+s2>s3 ,s3+s1>s2 ,s2+s3>s1
s1 = int(input("eneter the number "))
s2 = int(input("eneter the number "))
s3 = int(input("eneter the number "))

if(s1+s2>s3 and s3+s1>s2  and s2+s3>s1):
    print("is valid ")
else:
    print("not valid ")
