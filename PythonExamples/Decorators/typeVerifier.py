import inspect


def typeVerifier(func):
    """
    Decorator, verifies function's parameters values types and return type are as declared
    """

    def func_wrapper(*args, **kwargs):
        paramsDefinitions = inspect.getfullargspec(func)
        anotations = paramsDefinitions.annotations
        argsNames = paramsDefinitions.args

        expectedReturnType = anotations.get('return', None)
        # prepare parameters dictionary from **kwargs and *args
        params = dict()
        for a in range(len(args)):
            params[argsNames[a]] = args[a]
        params.update(**kwargs)
        # verify parameters types
        for key in params.keys():
            realType = type(params[key])
            requestedType = anotations.get(key, None)
            if requestedType is None:
                continue
            if not issubclass(realType, requestedType):
                raise Exception(f'Parameter type mismatch, function: [{func.__name__}], parameter: [{key}] expected: {requestedType} got: {realType}')
        # call function and verify return type
        ret = func(*args, **kwargs)
        realReturnType = type(ret)
        if not expectedReturnType is None and not issubclass(realReturnType, expectedReturnType):
            raise Exception(f'Parameter type mismatch, function: [{func.__name__}], return type, expected: {expectedReturnType} got: {realReturnType}')
        return ret

    return func_wrapper


if __name__ == '__main__':
    class myDict(dict):
        pass


    @typeVerifier
    def myFunc(a: int, b: str, c, e: dict, d: myDict) -> str:
        print(a, b, c, d, e)
        return 'aaa'


    val = myFunc(1, 'hello', 'qqq', e=myDict({1: 1, 2: 2}), d=dict({3: 3, 4: 4}))
    print(val)
