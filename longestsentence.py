# find the longest word in a sentence 
word =" he is a good boy"
long=word.split()
longest=max(long,key=len)
print(longest)