pyg = 'ay'

original = raw_input("Enter a word to be morphed: ")

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word[1:len(word)] + first + pyg
	print new_word
else:
	print "No string input"
