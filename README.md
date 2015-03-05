# Yakult-Challenge

I spotted this challenge on a London Underground tube last year.

The task was to find a list of London Underground tube stations that did not inclue any letters
from the given word.

These are a collection of files that solves this puzzle.

get_tubestation_list.py
-----------------------

You will need the Requests and BeautifulSoup libraries to run this properly.
The script scrapes the names of the tubestations from the following Wikipedia page:

http://en.wikipedia.org/wiki/List_of_London_Underground_stations

The list is then added to a text file.


word_test.py
------------

This script can be launched from the terminal with the given name as an argument.

example:

  python word_test.py brazil
  
It will return a list of train stations that match the challenge.
