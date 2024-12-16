# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, data):
#         self.stack.append(data)
#
#     def pop(self):
#         if not self.isEmpty():
#             return self.stack.pop()
#
#     def top(self):
#         if not self.isEmpty():
#             return self.stack[-1]
#         return None
#
#     def isEmpty(self):
#         return len(self.stack) == 0
#
#
# # procedence = {'(' : 1 , ')' : 1 , '^' : 2 , '*' : 3 , '/' : 3 , '+' : 4 , '-' : 4}
#
# def isHigher(op, top_op):
#     if top_op is None:
#         return False
#     precedence = {'(' : 1 , ')' : 1 , '^' : 2 , '*' : 3 , '/' : 3 , '+' : 4 , '-' : 4}
#     right_associative = {'^'}
#
#     if precedence[op] < precedence[top_op]:
#         return True
#     elif precedence[op] == precedence[top_op]:
#         # Handle associativity: Right-associative operators should NOT trigger a pop
#         return op not in right_associative
#     return False
#
#
# def Infix_to_Postfix(exp):
#     postfix = []
#     exp_operator = Stack()
#     operators = {'+', '-', '*', '/', '^', '(', ')'}
#
#     exp = exp.split(" ")
#
#     for element in exp:
#         if element in operators:
#             if element == ")":
#                 while exp_operator.top() != "(":
#                     postfix.append(exp_operator.pop())
#                 exp_operator.pop()  # Remove the '(' from the stack
#
#             elif element == "(":
#                 exp_operator.push(element)
#
#             else:  # Regular operators
#                 while (not exp_operator.isEmpty() and
#                        isHigher(element, exp_operator.top())):
#                     postfix.append(exp_operator.pop())
#                 exp_operator.push(element)
#
#         else:  # Operand
#             postfix.append(element)
#
#     # Pop remaining operators in the stack
#     while not exp_operator.isEmpty():
#         postfix.append(exp_operator.pop())
#
#     return postfix
#
#
# def calculator(op1, op2, operator):
#     match operator:
#         case '+':
#             return op1 + op2
#         case '-':
#             return op1 - op2
#         case '*':
#             return op1 * op2
#         case '/':
#             return op1 / op2
#         case '^':
#             return op1 ** op2
#
#
#
# # def Infix_to_Postfix(exp):
# #
# #     exp = exp.split(" ")
# #
# #     operators = {'+' , '-' , '*' , '/' , '^' , '(' , ')'}
# #
# #     postfix = []
# #     exp_operators = Stack()
# #
# #
# #     for element in exp:
# #
# #         if len(element) > 1:
# #             postfix.append(element)
# #
# #         elif len(element) == 1 and element not in operators:
# #             postfix.append(element)
# #
# #         elif element in operators:
# #
# #             if element == ')':
# #                 while exp_operators.top() != '(':
# #                     postfix.append(exp_operators.pop())
# #
# #                 exp_operators.pop()
# #
# #             elif element == '(':
# #                 exp_operators.push(element)
# #
# #             elif exp_operators.isEmpty():
# #                 exp_operators.push(element)
# #
# #             else:
# #                 while procedence[element] > procedence[exp_operators.top()] and exp_operators != '(':
# #                     postfix.append(exp_operators.pop())
# #
# #                 exp_operators.push(element)
# #
# #
# #
# #     while not exp_operators.isEmpty():
# #         postfix.append(exp_operators.pop())
# #
# #
# #
# #     return ' '.join(postfix)
#
#
#
# exp = "2 * ( 3 - 1 + 5 ^ 2 )"
# post = Infix_to_Postfix(exp)
# print("Postfix:", post)

precedence = {"(": 1, ")": 1, "^": 2, "*": 3, "×": 3, "/": 3, "+": 4, "-": 4, "−": 4}


def infix2postfix(infix):
    stack = []
    postfix = []

    for element in infix:
        if (element[0] == "-" or element[0] == "−") and element[1:].isdigit():
            postfix.append(element)
            print(element[1:])


        elif element.isalnum():
            # alphabet letter (a-z) and numbers (0-9)
            postfix.append(element)



        elif element == '(':
            stack.append(element)
        elif element == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses in expression")
            stack.pop()  # Remove ( from the stack
        else:
            if stack and not cls.precedence.get(stack[-1]) == 1:
                while (stack and cls.precedence.get(element, 0) <= cls.precedence.get(stack[-1], 0)):
                    # Send element as a key, if not found, return 0
                    postfix.append(stack.pop())
            stack.append(element)

    # Pop any remaining operators from the stack
    while stack:
        if stack[-1] == '(' or stack[-1] == ')':
            raise ValueError("Mismatched parentheses in expression")
        postfix.append(stack.pop())

    return ' '.join(postfix)



exp = "2 * ( 3 - 1 + 5 ^ 2 )"
post = infix2postfix(exp)
print("Postfix:", post)