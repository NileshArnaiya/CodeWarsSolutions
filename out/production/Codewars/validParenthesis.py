# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100




def valid_parentheses(string):
    # the list way - long way
    openList = []
    closeList = []
    if len(string) == 0:
        return True
    flag = False
    for i in string:
        if "(" == i:
            openList.append("(")
        elif ")" == i:
            closeList.append(")")
        if len(closeList) > len(openList):
            flag = True
    if flag:
        return False
    elif len(closeList) == len(openList):
        return True
    return False     

    # the string way 