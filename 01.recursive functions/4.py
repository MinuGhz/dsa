def binary_convertor(number):
    if number==0 :
        return ""

    else:
        return binary_convertor(number//2) + str(number%2)



print(binary_convertor(7))
print(binary_convertor(10))


