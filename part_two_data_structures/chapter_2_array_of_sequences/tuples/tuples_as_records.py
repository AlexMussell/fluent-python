# tuples arent just immutable lists, the can be records with no name field
# note: sorting city, etc would destroy the information because each pos is vital
import os

lax_coordinates = (33.9425, -119.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveller_ids = [('USA', '31196855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveller_ids):
    print('%s/%s' % passport)

# BRA/CE342567
# ESP/XDA205856
# USA/31196855

for country, _ in traveller_ids:
    print(country)

# USA
# BRA
# ESP

# Further tuple unpacking examples
latitude, longtitude = lax_coordinates

import os

divmod(20, 8)
# (2, 4)
t = (20, 8)
divmod(*t)
# (2, 4)
quotient, remainder = divmod(*t)

_, filename = os.path.split('/home/default/.ssh/id_rsa.pub')
print(filename)
# id_rsa.pub

# Using * to get excess
a, b, *rest = range(5)

# a, b, rest
# (0, 1, [2, 3, 4])

# * can go anywhere
a, *body, b = range(5)
# a, *body, b
# (0, [1, 2, 3], 4)


# can unpack nested tuples
metro_areas =[
    ('Tokyo', 'JP', 36.933,(35.6897222, 139.691667)),
    ('Delhi', 'IN', 21.935,(29.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142,(19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104,(40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649,(-23.547778, -46.635833))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longtitude) in metro_areas:
    if longtitude <= 0:  # western hemisphere
        print(fmt.format(name, latitude, longtitude))   # overridden and created own fmt object


# Named Tuple
# collections.namedtuple produces subclasses of tuple with field names and class name
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933,(35.6897222, 139.691667))
#City(name='Tokyo', country='JP', population=36.933, coordinates=(35.6897222, 139.691667))

tokyo.population
# 36.933

tokyo.coordinates
# (35.6897222, 139.691667)

tokyo[1]
# 'JP'

City._fields
#('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
dehli_data = ('Dehli', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(dehli_data)   # _make instantiate a named tuple from iterable. Same as City(*delhi_data)
delhi._asdict()     # {'name': 'Dehli', 'country': 'IN', 'population': 21.935, 'coordinates': LatLong(lat=28.613889, long=77.208889)}

for key, value in delhi._asdict().items():
    print(key + ": " + str(value))
    