import re

text = "Hii, My name is Tavleen Kaur and I am learning Python, i am CS student"

#Search for a pattern
match = re.search("Tavleen", text)
if match:
    print("Match found!!")
    print("Start index: ", match.start())
    print("End index: ", match.end())

#Find all ocurances of a pattern
matches = re.findall("I", text, re.IGNORECASE) #Case-insensitive serach
print("Matches: ", matches)

#Replace all occurances of a pattern
new_text = re.sub("Kaur", " ", text)
print("New text: ", new_text)

#Compile a regex for efficiency (if used multiple times)
pattern = re.compile(r"\b\w+\b")
words = pattern.findall(text)
print("Words: ", words)