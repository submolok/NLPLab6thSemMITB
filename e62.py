# 2. Write a program to normalize text by removing extra whitespace and converting all text to lowercase. 
import re
text = "Hello there    Lol this    will BE   CONVERTED TO LOWERCASE AND EXTRA SPACES     WILL BE REMOVED   "

pattern = re.sub(r'\s[\s]+', " ", text)
pattern = pattern.strip().lower()
print(pattern) 