# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.


import re
def property309(n):
    	# Your code goes here
	n = n**5
	if(len(set("".join(re.findall(r'([\d])', str(n))))) == 10):
		return True
	return False
def nthwithproperty309(n):
	f = 0
	g = 0
	while(f<=n):
		g+=1
		if(property309(g)):
			f+=1
	return g