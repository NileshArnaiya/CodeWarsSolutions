# // Write a function
#
# // triple_double(num1, num2)
# // which takes numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
#
# // If this isn't the case, return 0
#
# // Examples
# // triple_double(451999277, 41177722899) == 1
# // # num1 has straight triple 999s and num2 has straight double 99s
#
# // triple_double(1222345, 12345) == 0
# // # num1 has straight triple 2s but num2 has only a single 2
#
# // triple_double(12345, 12345) == 0
#
# // triple_double(666789, 12345667) == 1



from itertools import groupby
def triple_double(num1, num2): 
        resultOne = [(i, sum(1 for _ in j)) for i, j in groupby(str(num1))]
        resultTwo = [(i, sum(1 for _ in j)) for i, j in groupby(str(num2))]
        dict2 = dict(resultTwo)
        if(num1 == num2):
            return 0
        val = 0
        for k,v in dict(resultOne).items():
            if v >= 3:
                val = k
        if val in dict2.keys():
            if dict2[val] >= 2:
                return 1
            else:
                return 0
        else:
            return 0