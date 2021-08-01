# Write the function lookAndSay(a) that takes a list of ns and returns a list of ns
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (c, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

# Prerequisite for the following problem is the above problem.
# Write the function inverseLookAndSay(a) that does the inverse of the above problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
    	# Your code goes here
	output = [ ]
	c = 0
	n = 0
	if len(a[0])==0:
		return output
	for i in range(len(a)):
		c = (a[i])[0]
		n = (a[i])[1]
		for c in range(c):
			output.append(n)
	return output