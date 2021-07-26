def ispalindrome(n):
    reverse= int(str(n)[::-1])
    if(int(n)==reverse):
        return True
    else:
        return False

def isprime(n):
	if n> 1:	
		for i in range(2, int(n/2)+1):
			if (n % i) == 0:
				print(False)
				#break
			else:
				return True
	else:
		return False

def ispalindromicprime(n):
	if (ispalindrome(n)):
		if (isprime(n)):
			return True
	else:	
		return False

assert(ispalindromicprime(10)==False)
