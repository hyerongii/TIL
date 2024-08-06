bracket1 = '()()((()))'
bracket2 = '((()((((()()((()())((())))))'

def find_matchbracket(bracket):
    
    stack = []
    lst = list(bracket)
    for i in range(len(lst)):
        if bracket[i] == '(':
            stack.append(lst[i])
        elif bracket[i] == ')':
            stack.pop()
            
    if len(stack) > 0:
        return False
    else:
        return True
    
print(find_matchbracket(bracket1))
print(find_matchbracket(bracket2))