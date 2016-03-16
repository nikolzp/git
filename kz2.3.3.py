def hangman(word, letters):
    li = []
    lis = []
    lis1 = []
    for a in range(len(letters)):
        if letters[a] in word: 
            li.append(letters[a])
    for a in word:
        if a not in li:
            lis.append(' _ ')          
        else: lis.append(a)
    st = ''.join(lis)
    st = st.replace('  ', ' ')
    st = st.strip()
    return st


