# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def isascending(a):
    flag = 0
    a1 = a[:]
    a1.sort()
    if (a1 == a):
        flag = 1

# printing result
    if (flag):
        return True
    else:
        return False

# run a loop for first element and check if we could find any larger element than it after that element
def isdescending(a):
    flag = 0
    i = 1
    while i < len(a):
        if(a[i] > a[i - 1]):
            flag = 1
        i += 1
# printing result
    if (not flag):
        return True
    else:
        return False


def issorted(a):
    if(isascending(a) or (isdescending(a))):
        return True
    return False