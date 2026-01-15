# find string palindrome 
str1 ="naman"
start =0
half = (len(str1)-1)/2
end = len(str1)-1
count =0
while(start<half):
    if(str1[start]==str1[end]):
        count+=1
        start +=1
        end -=1
        
if count==half:
    print("palindrome")
else:
    print("not palinfrome ")
