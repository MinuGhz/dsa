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


procedence = {'(' : 1 , ')' : 1 , '^' : 2 , '*' : 3 , '/' : 3 , '+' : 4 , '-' : 4}



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



def Infix_to_Postfix(exp):

    exp = exp.split(" ")

    operators = {'+' , '-' , '*' , '/' , '^' , '(' , ')'}

    postfix = []
    exp_operators = Stack()


    for element in exp:

        if len(element) > 1:
            postfix.append(element)

        elif len(element) == 1 and element not in operators:
            postfix.append(element)

        elif element in operators:

            if element == ')':
                while exp_operators.top() != '(':
                    postfix.append(exp_operators.pop())

                exp_operators.pop()

            elif element == '(':
                exp_operators.push(element)

            elif exp_operators.isEmpty():
                exp_operators.push(element)

            else:
                while procedence[element] > procedence[exp_operators.top()] and exp_operators != '(':
                    postfix.append(exp_operators.pop())

                exp_operators.push(element)



    while not exp_operators.isEmpty():
        postfix.append(exp_operators.pop())



    return ' '.join(postfix)



exp = "2 * ( 3 - 1 + 5 ^ 2 )"
post = Infix_to_Postfix(exp)
print("Postfix:", post)
