def exponent(base, exp, result=1):
    if exp == 0:
        print(result)
    else:
        result = result * base
        exp -= 1
        exponent(base, exp, result)
