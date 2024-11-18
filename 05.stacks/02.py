queue = [1,2,3,4,5,6]
stack = [3,5,7,8,1,4]
intercept = []
for i in range(len(queue)):
    for j in range(len(queue)):
        if queue[0] == stack[0]:
            inter = stack.pop(0)
            queue.pop(0)
            intercept.append(inter)
        else:
            queue.append(queue.pop(0))

print(intercept)