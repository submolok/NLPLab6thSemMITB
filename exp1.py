import re
text = "hello there this is really cool and I really don't know what to do with this"
pattern = re.split(r"[^\w]", text)
print(pattern)
