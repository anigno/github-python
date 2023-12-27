def decoratorWithParameters(number, string):
    print('decoratorWithParameters', number, string)

    def wrapper(func):
        def wrapperFunc(*args, **kwargs):
            print('wrapperFunc', *args)
            func(*args, **kwargs)

        return wrapperFunc

    return wrapper

if __name__ == '__main__':
    @decoratorWithParameters(17, 'QQQQ')
    def testFunction(a, b, c):
        print('testFunction', a, b, c)

    testFunction(10, 20, 30)
