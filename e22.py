import re
text = "#hello there lol##"
print(len(re.findall(r'[^\w^\s]', text)))
