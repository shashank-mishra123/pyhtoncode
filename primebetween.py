#find prime number between 1 - 100
"""
 prime =number are divided to 1 and itself

"""
for num in range(2,101):
    for i in range(2,num):
        if num%i==0:
            break
    else:
     print(num)
          
    

    