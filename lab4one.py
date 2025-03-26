from collections import Counter
txt="I like I two like like free two"
n=1
words=txt.split()
a=[]
for i in range(len(words)-n+1):
    a.append(tuple(words[i:i+n]))
count=Counter(a)
print(count)
