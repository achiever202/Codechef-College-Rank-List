import sys
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import generate_rank_list	

arguments = sys.argv[1:]

if len(arguments)>2:
	print "Too many arguments for the college rank list generator."
else:
	generate_rank_list.generate_rank_list(arguments)

	generate_college_rank_list("Indian Institute of Technology, Hyderabad")
		

