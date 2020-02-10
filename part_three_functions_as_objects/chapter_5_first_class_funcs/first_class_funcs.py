# First class funcs
# Can be created at runtime, assigned to var, passed as arg, returned
# example:

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

# factorial(42)
# 1405006117752879898543142606244511569936384000000000

factorial.__doc__
#'returns n!'

type(factorial)
# <class 'function'>

# help(factorial)
    #   1 Help on function factorial in module __main__:
    #   2 
    #   3 factorial(n)
    #   4     returns n!

fact = factorial
# >>> fact 
# <function factorial at 0x...>

fact(5)
# 120

map(factorial, range(11))
# <map object at 0x...>

list(map(factorial, range(11)))
#[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

## First class funcs let us program in functional style. One hallmark of functional programming is higher order funcs