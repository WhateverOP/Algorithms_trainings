'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s):
    close_open_dict = {')':'(', ']':'[', '}':'{'}
    open_list = []
    for p in s:
        if p in close_open_dict.values():
            open_list.append(p)
        elif len(open_list) > 0 and p in close_open_dict.keys():
            last = open_list.pop()
            if close_open_dict[p] != last:
                return False
        else:
            return False
    if len(open_list) == 0:
        return True
    else:
        return False
    
# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "(()(()"
# s = "([)]"
s = "]"
ans = isValid(s)
print(ans)