# Callback: When a function is passed to a function in order to maintain and order of operations ie. y cannot execute till x has finished.
# A decortator is a callable that takes another func as arg and returns it waith another func or callable object.

# @decorate
# def target():
#     print('running target()')

# is the same as:

# def target():
#     print('running target()')

# target = decorate(target)

# Decorators usually replaces a func with a different one

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

# >>> target()
# ... running inner()

# Decorators are invoked immedialty when module is loaded.

registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():       # register(<function at x>)
    print('running f1()')

@register
def f2():       # register(<function at y>)
    print('running f2()')

def f3():
    print('running f3()')

def main():     # Then runs main
    print('running main()')       # Inside main
    print('registry ->', registry)   # registry -> [<function at x>, <function at y>]
    f1()
    f2()
    f3()

if __name__=='__main__':
    main() 

# Although they are excuted at IMPORT time, they are not EXECUTED until runtime
# Decorator funcs are usually defined in seperate moduleds to the functions they are invoked upon
# The above decorator returns same func passed as arg> Usually they define an inner func and return

# Referring back to the promotions issue in chapter 6. function oriented.py. One issue is that if someone added a new offer, they had to remember to update
# the promo list which can easily cause bugs. This can be fixed with decorators.
