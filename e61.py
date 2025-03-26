# 1. Write a program to detect and remove emoticons or emojis from textual data. 
import re
text = "hello there this contains emojis 🪥 💤🪥 💤"

pattern = re.sub(r'[^\x00-\x7F]','', text, re.UNICODE)

print(pattern) 