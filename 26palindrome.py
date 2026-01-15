# check number is palindrome or not 
number = 121
num = int(str(number)[::-1])
if(num== number ):
    print("palindrome")
else:
    print("number is not palindrome ")