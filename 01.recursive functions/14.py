def move(n , s , d , a):
    if n==1:
        print(s + '->' + a)
        print(a + '->' + d)

    else:
        move(n-1 , s , d , a)
        print(s + '->' + a)
        move(n-1 , d , s , a)
        print(a + '->' + d)
        move(n-1 , s , d , a)



move(2 , 'S' , 'D' , 'A')
print('-------------------------------------------------')
move(1 , 'S' , 'D' , 'A')