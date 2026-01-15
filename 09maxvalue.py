# find the key with the maximum values in a dictionary
d1 = {
    'a':1,
    'b':9,
    'c':5,
    'd':4
}
maxkey = max(d1,key=d1.get)
print(maxkey)