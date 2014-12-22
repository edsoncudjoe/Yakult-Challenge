

import sys

user_input = sys.argv[1]
word = user_input.lower()

data = open('tubestations.txt', 'r').read()
get_stations = data.split('\n')

stations = [(g.lower()) for g in get_stations]

result = []
check = set(word)
results = [s for s in stations if not any(l for check for l in s)]

print results
