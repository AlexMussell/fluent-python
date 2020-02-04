import timeit


TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""

def timer(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

timer('listcomp:', '[ord(s) for s in symbols if ord(s) > 127]')    # ord() returns int repr for Unicode chars
timer('listcomp + func:', '[ord(s) for s in symbols if non_ascii(ord(s)) > 127]')
timer('filter + lambda:', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
timer('filter + func:', 'list(filter(non_ascii, map(ord, symbols)))')

# listcomp: 0.006 0.006 0.006 0.006 0.005
# listcomp + func: 0.008 0.008 0.008 0.008 0.008
# filter + lambda: 0.010 0.010 0.010 0.010 0.010
# filter + func: 0.009 0.009 0.009 0.009 0.009
