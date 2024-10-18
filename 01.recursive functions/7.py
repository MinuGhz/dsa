def GCD(a,b):
    if a%b==0:
        return b
    else:
        c = a%b
        return GCD(b,c)



print(GCD(15,25))