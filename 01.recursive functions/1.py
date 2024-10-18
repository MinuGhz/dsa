def func(a,b):
    if a<b:
        return 0
    else:
        return 1+func(a-b , b)



print(func(10,2))
print(func(17,4))