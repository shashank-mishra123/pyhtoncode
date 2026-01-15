# merge two dictionary
dict1 = {
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
dict2 ={
    'e':5,
    'd':6
}
merge = dict1 | dict2
print(merge)
dict1.update(dict2)
print(dict1)