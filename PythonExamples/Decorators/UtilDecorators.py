import time


def decoratorWithParameters(number, string):
    print('decoratorWithParameters', number, string)

    def normalDecorator(func):
        def wrapperFunc(*args, **kwargs):
            print('wrapperFunc', *args)
            func(*args, **kwargs)

        return wrapperFunc

    return normalDecorator


def time_measure_between_calls(func):
    functionsDict = {}

    def wrapper(*args, **kwargs):
        t = time.clock()
        if func.__name__ in functionsDict:
            print(func.__name__, t - functionsDict[func.__name__], 'from last call')
        functionsDict[func.__name__] = t
        ret = func(*args, **kwargs)
        return ret

    return wrapper


def time_measure_function_decorator(func):
    def func_wrapper(*args, **kwargs):
        start = time.clock()
        ret = func(*args, **kwargs)
        end = time.clock()
        dif = end - start
        print(func.__name__, dif, 'time in function')
        return ret

    return func_wrapper


if __name__ == '__main__':

    @time_measure_function_decorator
    def measured_function():
        for i in range(1, 50):
            time.sleep(i / 1000)
        print('finished')


    @time_measure_function_decorator
    def other_measured_function(a, b, c):
        print('started', a, b, c)
        time.sleep(0.1)
        print('finished')
        return 'hello'


    measured_function()
    a = other_measured_function(1, b=2, c=3)
    print(a)


    @decoratorWithParameters(17, 'QQQQ')
    def testFunction(a, b, c):
        print('testFunction', a, b, c)


    testFunction(10, 20, 30)
