correct_num = 5
guess = int(input('write something: '))
while guess != correct_num:
    guess = int(input('write something: '))
    if guess == correct_num:
        print('The right numebr')
