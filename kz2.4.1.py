def double_tuple(value):
    t_o = ()    
    t_d = ()
    t_o = tuple(zip(*[iter(value)] * 2))
    if len(t_o)*2<len(value):
        t_d = (value[-1]),
        return (t_o + (t_d,))
    else:
        return (t_o)

