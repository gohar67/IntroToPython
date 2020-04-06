name = 'Hovhannes'
age = 18
password = '182516*'
if name == 'Batman':
    print('Welcome Mr. Batman!')
elif age <16:
    print('Dear %s, you are too young to register' % name)
elif '*' not in password or '&' not in password:
        print('Please enter a different password.')