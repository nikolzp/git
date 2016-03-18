def trimmed_text(text, limit):    
    if len(text) <= limit:
        return text
    tri_tochki = '...'
    text_f = ''
    for num, word in enumerate(text.split()):
        text_f += word + ' '
        if len(text_f[:-1] + tri_tochki) > limit:
            if num == 0:
                return word[:limit - 3] + tri_tochki
            return text_f[:-len(word)-2] + tri_tochki
            

    