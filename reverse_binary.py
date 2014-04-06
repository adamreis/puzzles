__author__="Adam Reis <ahr2127@columbia.edu>"
__date__ ="$Nov 3, 2013"

from sys import stdin


def reverse_binary():
	""" Reverses a single integer read from stdin in binary and prints the
		result to stdout in the fashion described here:
		https://www.spotify.com/us/jobs/tech/reversed-binary/
		(base_10 input -> binary -> reverse binary -> base_10 output)
	"""

	num = int(stdin.readline().rstrip())
	binary_string = bin(num)[2:]
	reversed_binary_string = binary_string[::-1]
	reversed_int = int(reversed_binary_string,2)

	print reversed_int

if __name__ == '__main__':
	reverse_binary()
