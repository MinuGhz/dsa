def move(n , s , d , a):
    if n==1:
        print(s + ' -> ' + d)
    else:
        move(n-1, s , a ,d)
        print(s + ' -> ' + d)
        move(n-1, a , d , s)


move(3 , 'S' , 'D' , 'A')