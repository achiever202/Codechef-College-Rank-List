"""
This function generates the entire rank list of a contest on codechef.
It takes the name of the contest as parameter.
It generates a file "rank_list.txt" which contains the rank, username, and score on each line, sorted by rank (alphabetically for same score).
"""

import sys
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

def generate_rank_list(arguments):

	# Generating list for the contest.
	contest_name = str(arguments[0])

	# Open a file for writing the entire rank_list.
	f = open("rank_list.txt", "w")

	# This variable keeps track of the last_score in the data.
	last_score = float(1)

	# Current rank of the candidate.
	current_rank = 1;

	# While the last_score is more than 0, send request for the next 100 ranks.
	while(last_score>0):
		rank_list = urllib2.urlopen("http://www.codechef.com/ajax/ranks/contest/"+contest_name+"/"+str(current_rank-1)+"/1000").read()

		# Generate the tree for the html response.
		soup = BeautifulSoup(rank_list)

		# for all the table rows in the request
		for table_row in soup.find_all('tr'):

			# for all the rows that have a rank i.e. not the table header and the rest of the rows.
			if table_row.get('class') == ['row']:

				# get the contents of the row.
				table_row_content = table_row.contents;

				# table_row_contents[5] stores the username of the participant, and table_row_content[7] stores the score.
				line = str(current_rank) + " " + table_row_content[5].string + " " + table_row_content[7].string
				print line

				# writing the line to file.
				f.write(line+"\n")

				# updating the last_score and current_rank.
				last_score = float(table_row_content[7].string)
				current_rank = current_rank + 1