def print_sorted(x):
    x = sort(x)
    print(x)
    return x

def sort(x):
    if isinstance(x,list):
        sorted_x = sorted(x)
        for i,new_x in enumerate(sorted_x):
            sorted_x[i] = sort(new_x)
        return sorted_x

    elif isinstance(x,tuple):
        sorted_x = sorted(x)
        for i, new_x in enumerate(sorted_x):
            sorted_x[i] = sort(new_x)
        return sorted_x

    elif isinstance(x,set):
        sorted_x = sorted(x)
        for i, new_x in enumerate(sorted_x):
            sorted_x[i] = sort(new_x)
        return sorted_x
    else:
        if isinstance(x,dict):
            sorted_list = sorted(x.items())
            sorted_x = {}
            for k,v in sorted_list:
                sorted_x[k]= sort(v)
            return sorted_x
        return x




