# Jonathan You, youjohna@usc.edu
# ITP 216, Spring 2023
# Section: Tuesday 7pm
# Homework 6
# Description:
# The purpose of this homework is to practice web scraping specific data from webpages. I created a store and load function
# to prevent DOS and over-requesting data from webpages. I then found all elements with specific tags/classes
# and then iterated through all of them to print out a specific attribute that I wanted
# One difficulty that I had during this was finding webpages that either did not utilize script (since we didn't learn how to parse through it)
# and finding webpages that did have the 403 Forbidden error

import os
from bs4 import BeautifulSoup as bs
import urllib.request
import ssl

# stores webpage as a html file to prevent DOS a webpage
def store_webpage (url, ctx, fn):
    page = urllib.request.urlopen(url, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w')
    print(soup, file=f)
    f.close()

# loads the webpage
def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context = ctx)
    return bs(page.read(), 'html.parser')

def main():
    # ignores SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    """
    # Example provided in class
    web_url = 'https://www.npr.org'
    file_name = 'sites/npr_main.html'       # have to manually create file

    # Uncomment below line and run ONCE to save the file locally. comment after done
    # store_webpage(web_url, ctx, file_name)

    file_url = 'file:///'+os.path.abspath(file_name)
    soupsieve = load_webpage(file_url, ctx)

    # find all div tags with a class attribute of 'story-wrap'
    story_wraps = soupsieve.find_all('div', class_ = 'story-wrap')
    for story_wraps in story_wraps:
        # grab the first h3 tag's content under this tag
        print(story_wraps.h3.text)
   """
    # Code for Shrine Auditorium
    # Provided the url that the fill will copy data from
    web_url_first = 'https://www.shrineauditorium.com/events'
    file_name_first = 'first_venue.html'

    # Utilizes the store_webpage function to store the data
    # Comment after storage to prevent DOS
    # store_webpage(web_url_first, ctx, file_name_first)

    # Saves the file to specificed location (same directory as this python file)
    file_url = 'file:///' + os.path.abspath(file_name_first)
    soupsieve = load_webpage(file_url, ctx)                                 # loads the webpage file

    firstShows = soupsieve.find_all('div', class_="info span clearfix")     # finds all elements that meet this requirement
    firstDates = soupsieve.find_all('h4', class_="date")                    # finds all elements that meet this requirement
    firstCounter = 0                                                        # Counter to track index

    # Iterates through all the elements that have the class_="info span clearfix", and prints out the text
    print("Shows coming up at Shrine Auditorium")
    for show in firstShows:
        print('\t',firstDates[firstCounter].text.strip())                   # Utilizes index to find the corresponding date from firstDates
        print('\t\t', show.h3.text)                                         # Prints out the first h3
        firstCounter+=1                                                     # updates counter

    # separates the two concerts
    for number in range(20):
        print('#', end="")
    print()

    # Code for The Wiltern
    # Provided the url that the fill will copy data from
    web_url_second = 'https://www.thenovodtla.com/events'
    file_name_second = 'second_venue.html'

    # Utilizes the store_webpage function to store the data
    # Comment after storage to prevent DOS
    # store_webpage(web_url_second, ctx, file_name_second)

    # Saves the file to specificed location (same directory as this python file)
    file_url_second = 'file:///' + os.path.abspath(file_name_second)
    soupsieve_second = load_webpage(file_url_second, ctx)                   # loads the webpage file

    secondShows = soupsieve_second.find_all('div', class_='title')                      # finds all elements that meet this requirement
    secondShowsDate = soupsieve_second.find_all('div', class_='date-time-container')    # finds all elements that meet this requirement
    secondCounter=0                                                                     # Counter to track index

    print("Shows coming up at Nova DTLA")
    for show in secondShows:
        print('\t',secondShowsDate[secondCounter].span.text.strip())                    # Utilizes index to find the corresponding date from firstDates
        print('\t\t',show.h3.text.strip())                                              # Prints out the first h3
        secondCounter +=1                                                               # updates counter

if __name__ == '__main__':
    main()