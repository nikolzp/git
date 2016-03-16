def count_holes(value):
    if type(value) is not int and type(value) is not str:
        return 'error'
    value = str(value)
    if value.isalpha(): return 'error'
    elif len(value) == 0: return 'error'
    elif '.' in value: return 'error'
    
    count = 0
    s = ''
    for a in filter(str.isdigit, value): s += a
    s = str(abs(int(s)))
    for a in s:
        a = int(a)
        if a == 8:
            count = count + 2
        elif a == 0 or a==4 or a==6 or a==9:
            count +=1
    return count
