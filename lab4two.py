from collections import Counter
txt=input("Enter a sentence: ")
n=int(input("Enter n-gram length: "))
words=txt.split()
a=[]
for i in range(len(words)-n+1):
    a.append(tuple(words[i:i+n]))
count=Counter(a)
for i in count:
    prob=count[i]/sum(count.values())
    print(prob)