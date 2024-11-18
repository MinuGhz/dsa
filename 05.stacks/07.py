def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    tokens = list(expression.replace(" ", ""))

    for token in tokens:
        if token.isalnum():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] < precedence[stack[-1]]:
                postfix.append(stack.pop())
            while stack and stack[-1] != '(' and precedence[token] == precedence[stack[-1]] and token != '^':
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


infix_expression = "x - y - z * (a + b)"
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix:", postfix_expression)