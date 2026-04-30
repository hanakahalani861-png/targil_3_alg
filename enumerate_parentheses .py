def enumerate_parentheses(operands):
    n = len(operands)
    if n==1:
        return operands
    l = []
    for i in range(n-1):
        l1 = enumerate_parentheses(operands[:i+1])
        l2 = enumerate_parentheses(operands[i+1:])
        for j in range(len(l1)):
             for k in range(len(l2)):
                  l.append([l1[j], l2[k]])
    return l

l = ['A1']*15
print(len(enumerate_parentheses(l)))