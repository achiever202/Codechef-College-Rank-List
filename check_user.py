import sys
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

# This function checks if a username belongs to a given college.
# It takes in as parameter, the username and the name of the college.
# If the username belongs to the college, it returns the name of the user, else returns 'None'
def check_user(username, college):

	# Obtaining the page of the user.
	user_page = urllib2.urlopen("http://www.codechef.com/users/"+username).read()

	# Parsing the html page.
	soup = BeautifulSoup(user_page)

	# is_college is the boolean flag which checks if the user belongs to the college.
	is_college = bool(0);

	# name stores the name of the user.
	name = ""

	for table in soup.find_all('table'):

		# obtaining the table in which user data exists.
		if str(table.get('class')) == "None" and str(table.get('id')) == "None" and str(table.get('cellpadding')) == "0":
			i = int(0);

			# for all columns in table with td tag.
			for column in table.find_all('td'):

				# this tag contains the name.
				if i == 3:
					name = name + column.string

				# this tag contains the institution/school
				if (i == 19) and (college in column.string):
						is_college = bool(1)
				i = i + 1

			# if college matches, returns name.
			if(is_college == True):
				return name
