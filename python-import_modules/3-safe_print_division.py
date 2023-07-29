def safe_print_division(a,b):
    result=None
    try:
        result=a/b
    except:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result


result=safe_print_division(a,b)
print("{:d} / {:d} = {}".format(a,b,result))
    