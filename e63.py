# 3. Write a python program to extract all dates in various formats (DD/MM/YYYY, MM-DD-YYYY, Month Day, Year) from mixed text. 

import re
text = "Hello world 16/08/2003, 03-24-2025 and May 16, 2025 lol lol lol"
print(re.findall(r'\b\d{2}/\d{2}/\d{4}|\b\d{2}-\d{2}-\d{4}|\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{2}, \d{4}\b', text))