def m_func(user: str, **kwargs): 
    if user =='admin':
        for key, value in kwargs.items():
            print(key, ':', value)
    else:
        print('access denied to the user %s' % user)

m_func(user='admin', key1='value1', key8 ='hiii')