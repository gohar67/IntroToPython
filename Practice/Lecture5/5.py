def sum_func(user, *args):
    if len(args) > 0:
        x = sum(args)/len(args)
        print('%s your average grade is: %d'% (user, x)) 
    else:
        print('No grades availble for %s' % user)

sum_func('Gxxx', 15, 17, 1222 )