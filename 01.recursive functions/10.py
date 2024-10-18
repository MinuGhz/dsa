def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def fact_sum(n):
    if n==0:
        return 0
    else:
        return 1/fact(n) + fact_sum(n-1)



print(fact_sum(3))