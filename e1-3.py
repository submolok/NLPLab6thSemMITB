# 2. How would you use regular expressions to identify all phone numbers in a text document, regardless of their format (e.g., 123-456-7890, (123) 456-7890, etc.)? 

import re
text= " hello there 123-456-7890 and (123) 456-7890 and 1234567890"
p = re.findall(r"\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}", text)
print(p)