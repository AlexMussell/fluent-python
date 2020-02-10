# Higher order funcs is a function that either takes a func as an argument, or returns a func

fruits = ['grape', 'apple', 'banana', 'melon', 'fig']
sorted(fruits, key=len)    # Higher order func
# any one-arg func can be passed into sorter()

def reverse(word):
    return word[::-1]

sorted(fruits, key=reverse)

# map, reduce, filter are all higher order funcs. Not that necessary anymore as listcomp and genexp easier to read
# reduce demoted to functools, all 3 return generators

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial

list(map(fact, range(6)))
test_map = [fact(n) for n in range(6)]
# [1, 1, 2, 6, 24, 120] 

list(map(fact, filter(lambda n: n % 2, range(6))))
test_filt = [fact(n) for n in range(6) if n % 2]
# [1, 6, 120]


## Lambda funcs
# Anyonymous funcs that are limited to pure expressions
# Best use is in context of arg list.


sorted(fruits, key=lambda word: word[::1])    # Higher order func
