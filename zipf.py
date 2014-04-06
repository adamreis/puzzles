__author__="Adam Reis <ahr2127@columbia.edu>"
__date__ ="$Nov 3, 2013"

from sys import stdin
from Queue import PriorityQueue

def find_highest_quality_songs():
	""" Uses Zipf's law to compute and print best m tracks in a given album
		of with n songs.  Input is read from stdin in the form described at
		http://www.spotify.com/us/jobs/tech/zipfsong/ and printed to stdout
	"""
	ranked_songs = PriorityQueue()
	num_tracks, num_to_print = [int(i) for i in stdin.readline().rstrip().split()]


	for i in range(num_tracks):
		raw_line = stdin.readline().rstrip()

		line = raw_line.split()
		listen_count = int(line[0])
		song_name = line[1]
		score = -(listen_count*(i+1)) # more negative == better score

		ranked_songs.put((score,song_name))

	for i in range(num_to_print):
		score, song_name = ranked_songs.get() # pops song with lowest (most negative) score
		print song_name




if __name__ == '__main__':
	find_highest_quality_songs()
