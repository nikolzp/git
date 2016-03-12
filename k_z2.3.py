var_string = "sabrrtuwacaddabra" 
#longest = "abrrtuw"
var_string = list(var_string)
print var_string
lis = [[]]
st = ''

for a in var_string:
    if a < st:
        lis.append([])
    st = a
    lis[-1].append(a)
print lis
