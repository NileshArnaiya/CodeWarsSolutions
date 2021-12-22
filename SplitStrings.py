def solution(s):
    
    newList = []
    i = 0;
    length = len(s)
    while i < len(s) - 1:
        newList.append([s[i], s[i+1]])
        i += 2
        length -= 2
    if(length == 1):
        newList.append([s[-1], "_"])    
    # convert outer nested list to inner list 
    outerlist = [''.join([str(c) for c in lst]) for lst in newList]
    return outerlist