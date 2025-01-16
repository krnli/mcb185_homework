import math

# Testing Functions
def char_to_prob(c):
    return print(c, ord(c))
char_to_prob('Z')

def prob_to_char(p):
    if type(p) == int: print(p, chr(p))
    else: print('None', type(p))
prob_to_char(76)


# Phred score conversions

"""
From Google: a phred quality score of 'Q' is directly related to an error rate 
    + error rate = 10^(-Q/10)
    + higher phred score indicates a lower error rate
    + each phred score is also correlated with an ASCII value
"""

def phred_error_rate(q):
    if type(q) == int: 
        E = 10 ** (-q / 10)
        return print(round(E, ndigits = 5))
    elif type(q) == float: 
        Q = -math.log10(q) * 10
        return print(round(Q, ndigits = 0))
phred_error_rate(16)
phred_error_rate(0.00032)
