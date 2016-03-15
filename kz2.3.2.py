def count_holes(value):
    count = 0
    li = []
    if len(value) == 0:
        return 'error'
    value = str(value)
    if value is not int:
        for a in filter(str.isdigit, value): li.append(a)
    if li[0] == '0':
        del li[0]
    for a in li:
        a = int(a)
        if a == 8:
            count = count + 2
        elif a == 0 or a==4 or a==6 or a==9:
            count +=1
    for a in value:
        if a == '.':
            return 'error'
    if not value.isalnum():
        return 'error'    
    return count
  
r = count_holes('')
print r
