def trimmed_text(text, limit):
    text_f = text[:limit]
    print text_f
#    if text != text_f:
#        text = text_f.replace((text_f.rfind([-1]), '...'))
#    print text
    
    

text = 'Python is simple to use, but it is a real programming language.'
a = trimmed_text(text, 27)
a = a.rfind()
print a
