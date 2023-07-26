def validate_password(pwd):
    upper=False
    lower=False
    digit=False
    if(" " in pwd or len(pwd)<8):
        return False

    for i in pwd:
        if((ord(i)>=65 and ord(i)<=90)):
            upper=True
        elif(ord(i)>=97 and ord(i)<=122):
            lower=True
        elif(ord(i)>=49 and ord(i)<=57):
            digit=True

    return True if(upper and lower and digit) else False


