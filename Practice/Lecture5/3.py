def g_func(password: str):
    count =0
    for i in password:
        if i>='0' and i<='9':
            count+=1
    if count > 2:
        print(password)
    if len(password)>=10:
        print(password)

g_func('mypasswo55477rdis')