def Truth_table(n , s = ""):
    if n==1:
        print(s + "0")
        print(s + "1")
    else:
        Truth_table(n-1 , s + "0")
        Truth_table(n-1 , s + "1")


Truth_table(3)