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
