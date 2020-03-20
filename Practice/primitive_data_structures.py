x = - 5
y = 6
print(abs(x*y))

#pow equals a ** 2 or 3 or ... n
a = 5
print(pow(a, 3))

x = [2, 5, 11, 58, 14, 25]
print(min(x))
print(max(x))
x = 105.26786
print(round(x))
print(round(x, 2))
print(round(x, 4))

import math
x = 2.2
print(math.ceil(x))
print(math.floor(x))

print(math.exp(1))
print(math.e)
print(math.exp(2))
print(math.pi)

#string

print("hello! my name is Gohar!!! Nice' to meet you")
print('"hello! my name is Gohar!!! Nice to meet you"')
print('doesn\'t matter')
print("""Hello,
My name is Gohar.
Nice to meet you""")
print("""Hello, \
My name is Gohar.
Nice to meet you""")

print(r'doesn\'t matter')
print("the world is wonderful \n full of energy")
print('love of my live don\'t \blame me')
print('love of my live don\'t \\blame me')
print(r'love of my live don\'t \\blame me')

a = ('abcnsdjdhkkllsdghsjue')
print(a[5])
print(a[5:])
print(a[5:11])
print(a[1:11:2])
print(a[-1])
print(a[-11:])

print(len(a))

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(z[::-1])
word = "Anaconda"
print('ag' + word[0:])

g = 'My dreams always come true!'
print(g.lower())
print(g.upper())
g1 = g[1:5].upper() + g[7:]
print(g1)

#find
#replace
x = "My name is My name"
x1 = x.lower()
print(x1.find("my"))
print(x1.replace("my", "Gohar"))

#string input
name = "Gohar"
surename = "Aghajanyan"
age = 27
print('My name is %s %s. I\'m %d years old.'%(name, surename, age))


#count
a = 'We are the champions my friends! and We will be fighting till the end!'
print(a.count(' '))
print(a.count('we'))
a1 = a.lower()
print(a1.count('we'))