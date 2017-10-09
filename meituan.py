def go(func):
    def wrapper(*args,**argss):
        print 'start'
        func(*args,**argss)
        print 'end'

    return wrapper


@go
def func(parameter):
    print parameter

func('abcd')