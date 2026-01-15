# find the factorial of number 
# factorial = 1*2*3*4*5
fact = int(input("enter the number "))
fact1=1
while fact>=1:
    fact1 *=fact
    fact -=1

print(f"factorial of {fact} is {fact1}")