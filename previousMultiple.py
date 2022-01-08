# Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a multiple of three.

# Return n if the input is already a multiple of three, and return null/nil/None/-1 if no such number exists.

# Examples
# 1      => null
# 25     => null
# 36     => 36
# 1244   => 12
# 952406 => 9


def prev_mult_of_three(n):
    res = [int(x) for x in str(n)]
    i = len(res)
    if n % 3 == 0:
        return n
    else:
        while i > 0:
            abc = int("".join(map(str, res[0:i])))
            if abc % 3 == 0:
                return abc
            i-=1
        
    