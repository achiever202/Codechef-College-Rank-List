"""
This function generates the entire rank list of a contest on codechef.
It takes the name of the contest as parameter.
It generates a file "rank_list.txt" which contains the rank, username, and score on each line, sorted by rank (alphabetically for same score).
"""

import sys
import urllib2

from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

import class_participant

def generate_rank_list(arguments):

	# Generating list for the current contest.
	contest_name = str(arguments[0])

	# list for the participants from India.
	participants = list()
	pos = 0

	# This variable keeps track of the last_score in the data.
	last_score = float(1)

	# keeping track of current rank (unique).
	current_rank = 1

	# While the last_score is more than 0, send request for the next 100 ranks.
	while(last_score>0):
		rank_list = urllib2.urlopen("http://www.codechef.com/ajax/ranks/contest/"+contest_name+"/"+str(current_rank-1)+"/1000").read()

		# Generate the tree for the html response.
		soup = BeautifulSoup(rank_list)

		# Getting all the rows in the table.
		rows = soup.find_all('tr')

		# If there are only two rows, i.e no participants, break.
		if len(rows) == 2:
			break;

		# Looking at the participants in the current lot.
		i = int(1)
		while i < len(rows)-1:

			# Getting all the columns in a row, i.e. data for a participant.
			cols = rows[i].find_all('td')

			# Getting the image for the flag of the country.
			image = cols[1].find_all('img')

			# if the country code is India.
			if image[0].get('title') == "IN":

				# cols[2] stores the username of the participant, and cols[3] stores the score.
				participants.append(class_participant.Participant(cols[0].string, cols[2].string, cols[3].string)) 

				line = participants[pos].rank + " " + participants[pos].username + " " + participants[pos].score;
				print line

				pos = pos+1

			# updating the last_score and current_rank
			last_score = float(cols[3].string)
			current_rank = current_rank + 1

			i = i+1

	return participants