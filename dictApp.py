import json
from difflib import get_close_matches


# Load the dictionary file
data = json.load(open('WebstersEnglishDictionary.json'))


def translate(w):
	# Mostly eliminate the case sensitivity issue
	w = w.lower()
	if w in data:
		return data[w]
	# In case of proper nouns
	elif w.title() in data:
		return data[w.title()]
	# In case of acronyms
	elif w.upper() in data:
		return data[w.upper()]
	# In case of no matches despite having input, suggest a close match
	elif len(get_close_matches(w, data.keys())) > 0:
		suggestion = get_close_matches(w, data.keys())[0]
		yn = input('Did you mean {} instead? Y/N: '.format(suggestion))
		if yn is 'Y':
			return data[suggestion]
	return 'This word does not exist in our dictionary.'


w = input('Please enter a word: ')

print(translate(w))
