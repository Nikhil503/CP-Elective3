# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def longestdigitrun(n):
    	# Your code goes here
	n = abs(n)
	LR = 1
	LRD = n % 10
	CR = 1
	index = n
	count = 0
	while index != 0:
		index //= 10
		count += 1
	if (count == 1):
		return 1
	for j in range(0,count):
		temp1 = n % 10
		n = n // 10
		temp2 = n % 10
		if (temp1 == temp2):
			CR += 1
		elif(CR > LR):              
			LR = CR
			LRD = temp1
			CR = 1
		elif(CR == LR and temp1 < LRD):
			LRD = temp1
			CR = 1
		else:
			CR = 1
	return LRD