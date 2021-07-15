# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")

def fun_applycaesarcipher(msg, shift):
    	#r = result
	res = ""
	for i in range(len(msg)):
		#c = char
		c = msg[i]
		#this is for upper case
		if ( c.isupper()):
			res += chr((ord(c) + shift - 65) % 26 + 65)
		#this is for spacing of words
		elif c == " ":
			res += " "
		#this is for lower case
		else:
			res += chr((ord(c) + shift - 97) % 26 + 97)
	return res




