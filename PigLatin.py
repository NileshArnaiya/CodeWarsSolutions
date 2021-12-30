# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


import re
def pig_it(text):
    #your code here
    myList = text.split(' ')
    myString = ""
    for i in myList:
        if re.search('[|^&+\-%*/=!?>]', i):
            myString+= i
        else:
            print(i[1:] + i[0] + 'ay')
            myString += i[1:] + i[0] + 'ay '
    return myString.strip()
    
    