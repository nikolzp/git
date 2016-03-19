def find_most_frequent(text):
    if text == '':
        return []
    text = text.lower()
    znaki = [',', '.', ':', ';', '!', '?']
    lis = [] 
    dic = {} 
    
    for a in text.split():
        if a[-1] in znaki:
            a = a[:-1]
        lis.append(a)

    for a in lis:
        if a not in dic:
            dic[a] = a.count(a)
        else:
            dic[a] += a.count(a)
    ma = max(dic.values())
    return sorted([a for a in dic if dic[a] == ma])
