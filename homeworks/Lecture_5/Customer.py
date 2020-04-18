import Productcheck as pr

def buy(product, num, price):
    if pr.check(product, num) is True:
        print('You bought %s and spent %d'% (product, num*price))
    else:
        print('Sorry! We are out of this product.')

def main():
    buy('candy', 15, 1500)

if __name__ == '__main__':
    main()
