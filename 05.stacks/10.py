pishvandi = ""
s = ""
stack = []
for i in pishvandi:
    if i in "+-*/(":
        stack.append(i)
    elif not s:
        stack.append(i)
    else:
        pass