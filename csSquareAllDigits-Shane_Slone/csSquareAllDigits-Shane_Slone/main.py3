def csSquareAllDigits(n):
    num_str = str(n)
    rtn_str = ""
    for digit in num_str:
        d = int(digit)
        d = str(d ** 2)
        rtn_str = rtn_str + d
    return int(rtn_str)    

