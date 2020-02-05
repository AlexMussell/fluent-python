## Argument assignment with sequences
# += - __iadd__ - inplace add - else  fallback - __add__  - if fallback, a += b same as a = a + b - making new object
# __iadd__ only works with mutable sequence, obviously. Therefore inefficient to keep *= immutable sequences
# Not a good idea to put mutable sequences in immutable as strange behavior. 


# changing lists in place should return None - Python convention
# list.sort in place, sorted() new list
# both take 2 optional KWargs: reverse, key
fruits = ['grape', 'apple', 'banana', 'melon']
sorted(fruits)  # ['apple', 'banana', 'grape', 'melon']
sorted(fruits, reverse=True)  # ['melon', 'grape', 'banana', 'apple']
sorted(fruits, key=len) # ['grape', 'apple', 'banana', 'melon']
fruits.sort()
# fruits = ['apple', 'banana', 'grape', 'melon']


## Bisect - binary search - 2 main funs: bisect, insort
# bisect(haystack, needle) - all items up in haystack up to needle are <= needle

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# DEMO: bisect_right
# haystack ->  1  4  5  6  8 12 15 20 21 23 23 26 29 30
# 31 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |31
# 30 @ 14      |  |  |  |  |  |  |  |  |  |  |  |  |  |30
# 29 @ 13      |  |  |  |  |  |  |  |  |  |  |  |  |29
# 23 @ 11      |  |  |  |  |  |  |  |  |  |  |23
# 22 @  9      |  |  |  |  |  |  |  |  |22
# 10 @  5      |  |  |  |  |10
#  8 @  5      |  |  |  |  |8 
#  5 @  3      |  |  |5 
#  2 @  1      |2 
#  1 @  1      |1 
#  0 @  0    0 


# A practical usage of this is to convert test scores to grades (table lookups by numeric value)
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
