# Valid paranthesis.

def isValid(sequence):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in sequence:
        if char in bracket_map:
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


print(isValid("{[}"))
print(isValid("{[]}"))
print(isValid("{}[]"))