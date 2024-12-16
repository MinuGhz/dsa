class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def isEmpty(self):
        return len(self.stack) == 0


def isHigher(op, top_op):
    if top_op is None:
        return True
    precedence = { '(' : 0 , ')' : 0 , '^' : 4 , '*' : 3 , '/' : 3 , '+' : 2 , '-' : 2}
    # print(precedence[top_op] , precedence[op] , top_op , op)
    return precedence[top_op] < precedence[op]


def calculator(op1, op2, operator):
    match operator:
        case '+':
            return op1 + op2
        case '-':
            return op1 - op2
        case '*':
            return op1 * op2
        case '/':
            return op2 / op1
        case '^':
            return op1 ** op2

########################################################################################################################

def Infix_to_Postfix(exp):
    postfix = []
    exp_operator = Stack()
    operators = {'+', '-', '*', "/", '^', '(', ')'}

    exp = exp.split(" ")
    # print(exp, "kiiiii")

    for element in exp:

        if element in operators:

            if element == ")":
                while exp_operator.top() != "(":
                    # print(exp_operator.stack)
                    postfix.append(exp_operator.pop())

                exp_operator.pop()

            elif element == "(":
                exp_operator.push(element)

            elif exp_operator.isEmpty():
                exp_operator.push(element)

            elif isHigher(element , exp_operator.top()):
                # print(exp_operator.stack)
                exp_operator.push(element)


            else:
                while not isHigher(element , exp_operator.top()):
                    # print(exp_operator.stack , element)
                    postfix.append(exp_operator.pop())

                exp_operator.push(element)


        else:
            postfix.append(element)



    while not exp_operator.isEmpty():

        op = exp_operator.pop()
        postfix.append(op)

    return " ".join(postfix)


def postfix_calculator(exp):
    operands = Stack()
    operators = {'+', '-', '*', '/', '^'}

    ch = ""
    for i in range(len(exp)):
        if exp[i] == " ":
            if ch:  # Process the token only if `ch` is not empty
                if ch not in operators:
                    operands.push(float(ch))  # Support float operands
                else:
                    op1 = operands.pop()
                    op2 = operands.pop()
                    res = calculator(op2, op1, ch)  # Correct operand order
                    operands.push(res)
                ch = ""  # Reset `ch` for the next token
        else:
            ch += exp[i]

    # Handle the last token (if any)
    if ch:
        if ch not in operators:
            operands.push(float(ch))
        else:
            op1 = operands.pop()
            op2 = operands.pop()
            res = calculator(op2, op1, ch)
            operands.push(res)

    return operands.pop()  # Final result

########################################################################################################################

def Infix_to_Prefix(exp):

    # exp = exp.split(" ")[::-1]
    #
    # # print(exp)
    #
    # prefix = ""
    #
    # for i in range(len(exp)):
    #     if exp[i] == '(':
    #         exp[i] = ')'
    #
    #     elif exp[i] == ')':
    #         exp[i] = '('
    #
    #     else:
    #         continue


    # print(prefix)

    postfix = Infix_to_Postfix(" ".join(exp))

    prefix = Infix_to_Postfix(exp).split(" ")[::-1]

    return " ".join(prefix)



def prefix_calculator(exp):
    operands = Stack()
    operators = {'+', '-', '*', '/', '^'}

    # Reverse the expression for prefix evaluation
    tokens = exp.split()[::-1]

    for token in tokens:
        if token not in operators:  # If the token is an operand
            operands.push(float(token))
        else:  # The token is an operator
            op1 = operands.pop()
            op2 = operands.pop()
            result = calculator(op2, op1, token)
            operands.push(result)

    return operands.pop()


#######################################################################################################################



# Test the functions
exp = "2 * ( -3 - 1 + 5 ^ 2 )"
post = Infix_to_Postfix(exp)
print("Postfix:", post)

res = postfix_calculator(post)
print("Result:", res)
#
prefix = Infix_to_Prefix(exp)

print("Prefix: " , prefix)
#
res = prefix_calculator(prefix)
print("Result:", res)