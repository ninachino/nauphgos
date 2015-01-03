import re

with open('text.txt') as f:
    text = f.read()

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
newtext = []
print sentences
for sentence in sentences:
	print sentence
	newsentence = raw_input("replace?\n")
	newsentence = str(newsentence)
	newtext.append(newsentence)
newtext = '\n'.join(newtext)
print newtext
