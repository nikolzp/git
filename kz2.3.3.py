def hangman(word, letters):
    st = []
    for a in range(len(letters)):
        if letters[a] in word: 
           st.append(letters[a])
    print st
        
s = hangman('python', ['a', 'r', 'y', 'i', 'o'])

print s

