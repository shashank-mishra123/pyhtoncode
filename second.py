# find second largest number 
numbers = [1,0,3,4,4,5,5]

# converst into list
secondlarg =list(set(numbers))

#sort 
secondlarg.sort()
print(secondlarg[-2])

