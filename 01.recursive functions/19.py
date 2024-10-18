def is_duplicate(str):
    n = len(str)
    if n == 0:
        return True
    elif n%2 == 1:
        return False
    elif str[0:n//2] != str[n//2:]:
        return False
    else:
        return is_duplicate(str[1:n//2])
        



print(is_duplicate("ALLALL"))
print(is_duplicate("ALILIALILI"))


# m = "hell"
# n = m[len(m)//2:]
# print(n)