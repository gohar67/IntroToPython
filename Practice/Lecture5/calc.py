
def calculate_cube(x):
    return x**3

def calculate_square(x):
    return x**2

import pretty_print

def main():
    result = calculate_cube(2)
    pretty_print.simple_print(result)
    result1 = calculate_square(4)
    pretty_print.pro_print(result1)
    

if __name__ == '__main__':
    main()
    
