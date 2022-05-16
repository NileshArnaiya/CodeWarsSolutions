# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

# 'abba' & 'baab' == true

# 'abba' & 'bbaa' == true

# 'abba' & 'abbba' == false

# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


from itertools import permutations
def anagrams(word, words):
    convert_tuple_string_to_list = list(map(list, list(permutations(word))))
    join_strings_in_nested_list = [''.join(ele) for ele in convert_tuple_string_to_list]
    # get the sorted difference between two lists using set
    result = sorted(set([item for item in join_strings_in_nested_list if item in words]))
    #sort based on other list
    return [elem for elem in words if elem in result]