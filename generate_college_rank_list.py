import sys
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import check_user

def generate_college_rank_list(college):
	read_file = open("rank_list.txt", "r");
	write_file = open("college_rank_list.txt", "w")

	for line in read_file:
		user_info = line.split(" ");
		user_name = check_user.check_user(user_info[1], college)
		if(user_name!=None):
			write_file.write(user_info[0] + " " + user_name + " " + user_info[2] + "\n")
		

