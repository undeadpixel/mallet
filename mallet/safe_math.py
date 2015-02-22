import math

def log10(value):
    if value == 0.0:
        return -1e50
    else:
        return math.log10(value)

def div(denominator, numerator):
    if numerator == 0.0:
        return 1e-50
    else:
        return denominator/numerator

