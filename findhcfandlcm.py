#find the lcm and hcf
#hcf
num =16
num1=17
maxi =max(num,num1)

for i in range(2,maxi):
    if num%i==0 and num1%i==0:
        print(i)
    else:
        print("no comman factor")
        break


