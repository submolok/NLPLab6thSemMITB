# divide progs into ngrams
from itertools import combinations
n =3

text ="hello there this is a very cool course, but kinda waste of time lawl"

print(list(combinations(text.split(),n)))
