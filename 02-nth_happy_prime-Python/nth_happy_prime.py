# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
	a=0
	b=0
	while(a<=abs(n)):
		b+=1
		if(happyprime(b)):
			a+=1
	return b

def prime(n):
	if n<2:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
		return True 

def happy(n):
	s=0
	while(n):
		r=n%10
		s+=r**2
		n=n//10
	if s==1:
		return True
	elif s<10:
		return False
	else:
		return happy(s)

def happyprime(n):
	if prime(n)==True and happy(n)==True:
		return True
	else:
		return False

	