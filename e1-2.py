# 1. Write a regex pattern to extract all dates in the format DD/MM/YYYY from a paragraph of text. 

import re

text = "hello there this is really cool and I really don't know what to do with this 16/08/2003 and 12/12/2012"
pattern = re.findall(r"\d{2}/\d{2}/\d{4}", text)
print(pattern)