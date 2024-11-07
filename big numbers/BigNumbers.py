class BigNumber:
    def __init__(self , num = None):
        self.magnitude = []

        if num== None:                        #create an empty bignumber
            self.sign = True
            self.magnitude.append(0)

        elif type(num)==str:                 #converts a string to a Big Number
            if num[0]=='-':
                self.sign = False
                n = 1
            elif num[0] == '+':
                self.sign = True
                n = 1
            else:
                self.sign = True
                n = 0
            for i in range(n , len(num)):
                    self.magnitude.append(int(num[i]))

        elif type(num)==int:                #converts an integer to a Big Number
            if num < 0:
                self.sign = False
            else:
                self.sign = True
            num = abs(num)
            num_arr = []
            while num != 0:
                num_arr.append(num%10)
                num //= 10                              # for num = 1234, num_arr is [4,3,2,1]
            self.magnitude = num_arr[::-1].copy()

        else:                             #converts a list of digits to a Big Number
            if num[0]<0:
                self.sign = False
            else:
                self.sign = True
            for i in range(len(num)):
                self.magnitude.append(abs(num[i]))


    def add(self, other):

        result = []              #A temporary list to store the results
        carry = 0

        if self.sign == other.sign:                                           ########CASE 1: If two numbers have the same sign ######
            first = self.magnitude[::-1].copy()                               #uses 2 temporary lists for easier calculation
            second = other.magnitude[::-1].copy()

            for i in range(0 , max(len(first) , len(second))):
                if i<len(first) and i<len(second):
                    res = first[i] + second[i] + carry

                elif i >= len(first):
                    res = second[i] + carry

                elif i >= len(second):
                    res = first[i] + carry

                carry = res // 10
                result.append(res % 10)

            if carry != 0:
                result.append(carry)

            self.magnitude =  result[::-1].copy()             #if you want your main Bignumber not to change, ignore this line and return result[::-1] instead
            return self.magnitude

        else:                                                                                  #########CASE2: if their signs are different#######

            first = []
            second = []

            if len(self.magnitude) > len(other.magnitude):                                    #a condition for finding the final sign
                first = self.magnitude[::-1].copy()
                second = other.magnitude[::-1].copy()
            elif len(self.magnitude) == len(other.magnitude):
                flag = False
                for i in range(len(self.magnitude)):
                    if self.magnitude[i] == other.magnitude[i]:
                        continue
                    elif self.magnitude[i] < other.magnitude[i]:
                        first = other.magnitude[::-1].copy()
                        second = self.magnitude[::-1].copy()
                        self.sign = other.sign
                        flag = True
                        break
                    else:
                        break

                if flag == False:
                    first = self.magnitude[::-1].copy()
                    second = other.magnitude[::-1].copy()

            else:                                       #len(self.magnitude) < len(other.magnitude)
                first = other.magnitude[::-1].copy()
                second = self.magnitude[::-1].copy()
                self.sign = other.sign


            for i in range(len(first)):

                if i < len(second):
                    if first[i] < second[i]:
                        first[i+1] -= 1
                        result.append(first[i]+10-second[i])

                    else:
                        result.append(first[i]-second[i])

                else:
                    result.append(first[i])

            while result[-1] == 0:
                result.pop()

            self.magnitude = result[::-1].copy()                        #if you want your main Bignumber not to change, ignore this line and return result[::-1] instead
            return self.magnitude



    def sub(self , other):                                           #subtract method for 2 Big Numbers

        if self.sign != other.sign:                                  #it's exactly like adding 2 Big Numbers with same signs
            bignum = BigNumber(other.magnitude)
            bignum.sign = self.sign

            return self.add(bignum)

        else:                                                        #it's exactly like adding 2 Big Numbers with different signs
            bignum = BigNumber(other.magnitude)
            if other.sign == True:
                bignum.sign = False
            else:
                bignum.sign = True

            return self.add(bignum)


    def rightShift(self , n = 1):                                #right shift works as   self//(10^n)

        while n > 0:
            self.magnitude.pop()
            n -= 1

        return self.magnitude


    def leftShift(self , n = 1):                                #left shift works as   self*(10^n)

        while n > 0:
            self.magnitude.append(0)
            n -= 1

        return self.magnitude













b1 = BigNumber(12740)
b2 = BigNumber('8754')

print(b1.magnitude , b1.sign)
print(b2.magnitude, b2.sign)
print(b1.add(b2) , b1.sign)
print(b2.leftShift(2))
print(b2.rightShift())
