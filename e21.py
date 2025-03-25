# WRITE A PROGRAM TO REMOVE THE FIRST AND LAST CHARACTERS IF THEY ARE NOT LETTERS OR NUMBERS FROM A GIVEN SENTENCE. 

import re

text = "#hello there lol##"
text = re.sub(r'^[^a-zA-Z0-9]+','', text)
text = re.sub(r'[^a-zA-Z0-9]+$','', text)
print(text)