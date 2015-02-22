import math

def log10(value):
    if value == 0.0:
        return -1e50
    else:
        return math.log10(value)

def log2(value):
    if value == 0.0:
        return -1e50
    else:
        return math.log(value, 2)

def div(denominator, numerator):
    if numerator == 0.0:
        return 1e-50
    else:
        return denominator/numerator

