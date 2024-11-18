queue = ["a","b","c","d","j","k","l"]
stack = ["c","b","a","d","e","f"]
intercept = []
for i in range(len(queue)):
    for j in range(len(queue)):
        if queue[0] in stack[0]:
            inter = stack.pop(0)
            queue.pop(0)
            intercept.append(inter)
        else:
            queue.append(queue.pop(0))

print(intercept)