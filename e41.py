from itertools import combinations
n =3

text ="hello there this is a very cool course, but kinda waste of time lawl hello there this is a very cool course, but kinda waste of time lawl hello there this is a very cool course, but kinda waste of time lawl hello there this is a very cool course, but kinda waste of time lawl"
arr = text.split()
combs = []
for x in range(len(arr)):
    if(x+n<=len(arr)):
        combs.append(tuple(arr[x:x+n]))
print(combs)