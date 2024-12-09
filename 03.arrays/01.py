# time complexuty = O(n)
def fib(n):
    fib_array = [1,1]

    if n <= 0:
        return []
    elif n == 1:
        return 1
    else:
        for i in range(2,n):
            fib_array.append(fib_array[i-1] + fib_array[i-2])

        return fib_array



def fib_a(n):

    fib_array = [1,1]

    while len(fib_array) <n+1:
        fib_array.append(fib_array[-1] + fib_array[-2])


    return fib_array


print(fib_a(10))