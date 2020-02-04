
colours = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(colour, size) for colour in colours
                            for size in sizes]   # list by colour then size

print(tshirts)


# not as readable
for colour in colours:
    for size in sizes:
        print((colour, size))

# listcomp for building lists. Other sequence types used genexp
