def multiply(a , b):
    if b==0:
        return 0
    elif b<0:
        return (-1)*multiply(a , -b)
    else:
        return a + multiply(a , b-1)



print(multiply(3,-5))