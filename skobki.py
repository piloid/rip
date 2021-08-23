def valid_parentheses(string):
    s=0
    for i in string:
        if i == '(':
            s+=1
        elif i == ')':
            s-=1
        if s<0:
            return False
            break
    if s==0:
        return True
    else:
        return False

print(valid_parentheses("hi(hi)()"))