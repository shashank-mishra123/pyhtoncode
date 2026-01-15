# valid password base on condition
condition = ['@','$','%','&']
password = input("enter the password :")
for iteam in range(len(password)):
    if(password[iteam]=='@'):
     print("is valid ") 
     break