def multi_bracket_validation(string):
    paren = 0
    curly = 0
    square = 0
    for i in string:
        if i == '(':
            paren += 1
        if i == ')':
            if paren == 0:
                return False
            elif curly != 0 and not curly % 2 == 0 and square != 0 and not square % 2 == 0:
                return False
            else:
                paren -= 1
        if i == '{':
            curly += 1
        if i == '}':
            if curly == 0:
                return False
            elif paren != 0 and not paren % 2 == 0 and square != 0 and not square % 2 == 0:
                return False
            else:
                curly -= 1
        if i == '[':
            square += 1
        if i == ']':
            if square == 0:
                return False
            elif curly != 0 and not curly % 2 == 0 and paren != 0 and not paren % 2 == 0:
                return False
            else:
                square -= 1
    if paren == 0 and curly == 0 and square == 0:
        return True
    else:
        return False

# delete opening as it finds it's closing or run up upening and closing then compare
# run through if it picks up a closing of any kind before it picks up an opening of that ype return false
# if it doesnt pick up a closing to an opening return false


if __name__ == "__main__":
    print(multi_bracket_validation('w(o}r{d)s'))