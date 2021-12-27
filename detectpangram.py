# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(s):
    # wanted to try without regex or string functions
    count = 0
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (a,b,c) in zip(s, alphabets, ALPHABETS):
        if b in s or c in s:
            count+=1
    return True if count == 26 else False