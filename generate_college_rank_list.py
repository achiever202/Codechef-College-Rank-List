import sys
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import check_user

def generate_college_rank_list(rank_list, college):

	write_file = open("college_rank_list.txt", "w")

	for participant in rank_list:
		user_name = check_user.check_user(participant.username, college)
		print participant.rank + ". " + participant.username
		if(user_name!=None):
			print "****************"+user_name+"******************"
			write_file.write(participant.rank + " " + user_name + " " + participant.score + "\n")
		

