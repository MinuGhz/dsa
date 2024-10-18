def Ack(m , n):
    if n<0 or m<0:
        return 0
    elif m==0:
        return n+1
    elif n==0:
        return Ack(m-1 , 1)
    else:
        return Ack(m-1 , Ack(m , n-1))



print(Ack(3,2))