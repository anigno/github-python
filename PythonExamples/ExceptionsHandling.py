try:
    a=1/0
except (ZeroDivisionError,ValueError):
    print('Zero division detected')
    raise ValueError('aaaa',321)
except Exception as e:
    # e = sys.exc_info()[0]
    print(e)
else:
    print('No exception')
finally:
    print('finally')


