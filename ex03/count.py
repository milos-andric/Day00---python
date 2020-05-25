import string
from sys import argv
def text_analyser(*phrase) :
	if len(phrase) == 1 :
		phrase = " ".join(phrase)
		prog(phrase)
	elif len(phrase) == 0 :
		print("What is the text to analyse?")
		phrase = input()
		prog(phrase)
	else :
		print("ERROR")

def prog(phrase) :
		upper = 0
		lower = 0
		espace = 0
		point = 0
		inc = 0
		for x in phrase :
			if x.islower() :
				lower += 1
			elif x.isupper() :
				upper += 1
			elif x.isspace() :
				espace += 1
			elif x in string.punctuation :
				point += 1
			inc += 1
		print("The text contains " + str(inc) + " characters:\n")
		print(str(upper) + " upper letters\n")
		print(str(lower) + " lower letters\n")
		print(str(point) + " punctuation marks\n")
		print(str(espace) + " spaces")
