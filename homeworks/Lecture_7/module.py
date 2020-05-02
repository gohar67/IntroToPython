def h2(x):
    return x**3

try:
    import module12
    r = h2(5)
    module1.h1(r)
except ModuleNotFoundError:
    print('lalaa')
