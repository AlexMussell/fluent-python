import array

# genexp saves mem as it yields items one by one using iter protocol

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
# (36, 162, 163, 165, 8364, 164)

array.array('I', (ord(symbol) for symbol in symbols))  
# array('I', [36, 162, 163, 165, 8364, 164])
# can call tuple(), otherwise surrounding () mandatory


# genexp of cartesian product listexp
colours = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colours for s in sizes):
    print(tshirt)

# black S
# black M
# black L
# white S
# white M
# white L       yields one at a time
