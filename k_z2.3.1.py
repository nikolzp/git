def func(var_a, var_b):
    if type(var_a) is str or type(var_b) is str:
        return 'str'
    else:
        if var_a > var_b:
            return '>'
        elif var_a < var_b:
            return '<'
        elif var_a == var_b:
            return '='

func(5, '2')

