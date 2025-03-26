#Program to generate N-grams in reverse order
from collections import Counter
txt=input("Enter a sentence: ")
n=int(input("Enter n-gram length: "))
words=txt.split()
a=[]
for i in range(len(words)-n+1):
    a.append(tuple(words[i:i+n]))
count=Counter(a)
for i in reversed(count):
    print(i)