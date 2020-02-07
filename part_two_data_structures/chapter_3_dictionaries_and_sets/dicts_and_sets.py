# Object is hashable if it has a value that never changes over its lifetime
# immutable objects (str, bytes, numeric types) for example. Tuples are, but all elements must be immutable. 

# dicts can be built in multiple ways:
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'],[1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})

# a == b == c == d == e
# True

## Dict comp
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
    
country_code = {country: code for code, country in DIAL_CODES}
# basic methods: .get(k, [default]), .values(), .keys(), .pop(k, [default])

## Sets
# Sets only contains unique elements of a list
# its elements must be hashable
# Has mathematical set operations: intersection(), union(), difference() etc
