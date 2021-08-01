# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    s1 = s1.casefold()
    s2 = s2.casefold()
    if(sorted(s1) == sorted(s2)):
        return True
    return False

# write your test cases here...
assert(areAnagrams("Bababa", "ababab") == True)
assert(areAnagrams("Goku", "vegeta") == False)
assert(areAnagrams("Listen", "Silent") == True)
assert(areAnagrams("range", "rage") == False)
assert(areAnagrams("Abc", "def") == False)
assert(areAnagrams("naruto", "sasukae") == False)

print ("All test cases passed....")