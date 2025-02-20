import math

# Testing Functions
def char_to_prob(c):
    return print(c, ord(c))
char_to_prob('A')

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
    if type(q) == float: 
        Q = -math.log10(q) * 10
        Q = round(Q)
        return print(chr(Q + 33))
    elif type(q) == str:
        Q = 10 ** (-(ord(q) - 33) / 10)
        return print(round(Q, ndigits = 5))
phred_error_rate('A')
phred_error_rate(0.501)
