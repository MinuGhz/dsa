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
        return False
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence[top_op] >= precedence[op]


def calculator(op1, op2, operator):
    match operator:
        case '+':
            return op1 + op2
        case '-':
            return op1 - op2
        case '*':
            return op1 * op2
        case '/':
            return op1 / op2
        case '^':
            return op1 ** op2

########################################################################################################################

def Infix_to_Postfix(exp):
    postfix = ""
    exp_operator = Stack()
    ch = ""
    operators = set(['+', '-', '*', "/", '^', '(', ')'])

    for i in range(len(exp)):
        if exp[i] is not " ":
            ch += exp[i]


        else:
            if ch in operators:

                if ch == "(" or isHigher(ch, exp_operator.top()) or exp_operator.isEmpty():
                    exp_operator.push(ch)

                elif ch == ')':
                    while exp_operator.top() != '(':
                        op = exp_operator.pop()
                        postfix += op
                        postfix += " "

                    exp_operator.pop()


                else:
                    while not isHigher(ch, exp_operator.top()):
                        op = exp_operator.pop()
                        postfix += op
                        postfix += " "


            else:
                postfix += ch
                postfix += " "

            ch = ""

    while not exp_operator.isEmpty():
        op = exp_operator.pop()
        postfix += op
        postfix += " "

    return postfix


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

    pre = []
    ch = ""

    for i in range(len(exp)):
        if exp[i] == " ":
            pre.append(ch)
            pre.append(" ")
            ch = ""

        else:
            ch += exp[i]

    pre.append(exp[-1])


    print(pre)

    pre = pre[::-1]

    exp_pre = ""

    for i in range(len(pre)):

        if pre[i] == "(":
            pre[i] = ')'
        elif pre[i] == ')':
            pre[i] = '('

        exp_pre += pre[i]

    print(exp_pre)


    prefix = Infix_to_Postfix(exp_pre)
    print(prefix)
    prefix = prefix[::-1]

    return prefix





# Test the functions
exp = "-12 * ( 3 - 1 + 5 ^ 2 )"
post = Infix_to_Postfix(exp)
print("Postfix:", post)

res = postfix_calculator(post)
print("Result:", res)

prefix = Infix_to_Prefix(exp)

print("Prefix: " , prefix)

