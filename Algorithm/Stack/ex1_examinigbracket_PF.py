def check_match(expression):
    stack = []

    matching_dict = {")":"(", "]":"[", "}":"{"}

    for char in expression:
        if char in matching_dict.values():
            stack.append(char)
        elif char in matching_dict.keys():
            
            # 스택이 비어있거나 
            if not stack or stack[-1] != matching_dict[char]:
                return False
            
            stack.pop()

    if len(stack) == 0:
        return True
    
    return False
    # return not stack  # 스택이 비어있으면 True, 요소있으면 False
            