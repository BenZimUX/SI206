# Use https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions

# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.


import requests
import re
from bs4 import BeautifulSoup

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url) #connecting to website and grabbing html code
soup = BeautifulSoup(r.text, "html.parser") #html code become a readable class

#1)
findstudent = soup.find_all(text = re.compile('student')) #finds all the places where student exists
empty = []
for word in findstudent:
    fixed_text = str(word).replace('student', 'AMAZING student') #replaces all instances of "student", with "AMAZING student"
    word.replace_with(fixed_text)
    empty.append(fixed_text)

#2)
for link in soup.findAll('iframe'): #replaces all instances of 'iframe', with my own photo
	link['src'] = "C:/Users/Ben/Desktop/206/SI206/Homework3/media/pic.jpg"

#3)
for img in soup.findAll('img'):  #replaces all instances of 'img', with the logo photo
	img ['src'] = "C:/Users/Ben/Desktop/206/SI206/Homework3/media/logo.png"

f = open("index.html", "w") 
f.write(soup.prettify()) #actually writes everything into html