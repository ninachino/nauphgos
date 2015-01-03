import re

i = open('input.txt')
o = open('output.txt', 'r+')

text = i.read()

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

newtext = []
for sentence in sentences:
	print sentence
	newsentence = raw_input("replace?\n")
	newsentence = str(newsentence)
	o.write(newsentence + "\n")

