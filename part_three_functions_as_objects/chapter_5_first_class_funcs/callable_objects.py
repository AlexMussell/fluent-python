## Callable objects
# Operator ()
# 7 callable types: user defined funcs, built in funcs, built in methods, methods, classes, class instances, generator funcs
# only needs to implement __call__


import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty bingo cage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(13))
bingo.pick()
bingo()   # calls __call__
callable(bingo)
# >>>True
# implemeting __call__ is an easy way to create function like objects that have some internal state


