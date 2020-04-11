def m_func(*args):
    for arg in args:
        if arg%2==0:
            print(arg)
m_func(1,2,3,4,5,6,7,8)