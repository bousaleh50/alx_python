def no_c(my_string):
    no_c_string=""
    for i in my_string:
        if i not in ['c','C']:
            no_c_string+=i
    return no_c_string

