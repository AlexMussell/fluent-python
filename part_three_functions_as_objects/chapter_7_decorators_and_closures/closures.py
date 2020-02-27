# Closure is a function with extended scope. It encompasses nonglobal vars references 
# in the body of the func but not defined there.
# It retains the binding of the free variables that exist when the function is defined

# Take a simple average class

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# and here is a functional implementation

def make_averager():
    series = []     #<----- closure

    def average(new_value):
        series.append(new_value)     #<--- series is a free variable
        total = sum(series)
        return total/len(series)

    return average

# >>> avg = make_averager()
# >>> avg(10)
# 10.0
# >>> avg(11)
# 10.5

# So the above works as we do not assign series to anything, and lists are immutable
# But what about with immutable types like numbers, strings, tuples?
# For example, a better way to write our function is to store the total and the amount of numbers
# we have inputted so far. As otherwise we have to save the whole array in memory

def make_averager_wrong():
    counter = 0
    total = 0

    def average(new_value):
        counter += 1
        total = new_value
        return total/counter

    return average

# We are manipulating counter, which is an immutable type, meaning we are assigning counter to counter,
# making it a local variable to average and not a free variable. Therefore it isn't a part of the closure
# However, nonlocal in Python3 solves this.

def make_averager_correct():
    counter = 0
    total = 0

    def average(new_value):
        nonlocal counter, total
        counter += 1
        total = new_value
        return total/counter

    return average
