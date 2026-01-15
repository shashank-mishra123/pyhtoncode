# reverse a list without using a reverse function 
l = [1,2,3,4,5,6,7]
count = (len(l)-1)/2
end = len(l)-1
start =0
start1 =0
while(start<=count):
    start1 = l[start]
    l[start] = l[end]
    l[end] = start1

    start +=1
    end -=1
print(l)