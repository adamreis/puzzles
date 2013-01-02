"""	lottery.py
	written by Adam Reis for Spotify application
	adamhreis@gmail.com
	01/02/13

** 	please note -- this is the first program I've ever written in Python.
	I usually write in C/C++ and Java so my conventions may be a bit off!
"""

from math import floor, factorial

def choose(n,r):
	""" Calculates choose(n,r) using the factorial method """
	return float(factorial(n)/(factorial(r)*factorial(n-r)))

def main():
	""" Calculates and prints the probability that our entire group will be
		able to get tickets to the broadway show, given appropriate input.
	"""

	# Parse input line and cast variables to integers
	m,n,t,p = [int(i) for i in raw_input().split()]

	# If you choose as many (or more) winners than there
	# are in the lottery, the probability is always 1
	if n>=m:
		print '1'
		exit(1)

	winners = int(floor(p/t)+1) # number of winners required within our group

	#1-(probability of someone in our group not being able to go)
	probability = 1-choose(m-n,winners)/choose(m,winners)
	print probability

if __name__ == "__main__":
	main()