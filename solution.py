def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
 
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                length = i - stack[-1]
                if length > max_len:
                    max_len = length
 
    return max_len
 
if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))   
    print(longest_valid_parentheses(")()())"))   
    print(longest_valid_parentheses(""))        
 