def find_most_frequent(text):
    if text == '':
        return []
    text = text.lower()
    red_text = ''
    lis_povt = []
    fin_list = []
    
    znaki = [',', '.', ':', ';', '!', '?']
    for a in text.split(' '):
        if a[-1] in znaki:
            a = a[:-1] 
        red_text += a + ' '
    
    for a in text.split():
        print a
        if text.count(a) > 1:
            list_povt = lis_povt.append(a)
    
    for a in lis_povt:
        if a in fin_list: continue
        fin_list.append(a)
    return sorted(fin_list)
            



text = "And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind."
s = find_most_frequent(text)
print s