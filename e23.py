import re
text = "#hello there lol##"
text= re.sub(r'[^\w^\s]', "123", text)
print(text)
