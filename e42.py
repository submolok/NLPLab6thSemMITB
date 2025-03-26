# from itertools import combinations
# n =3

# text ="Once upon a time in a faraway land, there lived a curious rabbit named Benny. Benny loved to explore the woods and meadows around his cozy little burrow. One sunny afternoon, while hopping through a particularly dense thicket, Benny stumbled upon a hidden clearing. In the center of the clearing stood an old, gnarled tree, its branches twisted and tangled in a way that seemed almost magical. Benny felt drawn to the tree, as if it held secrets and stories that only he could hear. As he approached, the wind rustled through the leaves, whispering ancient tales of wonder and adventure"
# arr = text.split()
# combs = []
# for x in range(len(arr)):
#     if(x+n<=len(arr)):
#         combs.append(tuple(arr[x:x+n]))
# print(combs)
# h={}
# for x in combs:
#     if(x not in h):
#         h[x] = 1
#     else:
#         h[x]+=1
# print(h)    

# IM SORRY I'M PERPLEXIETY-ING THIS



import re

n = 3
text = "Once upon a time in a faraway land, there lived a curious rabbit named Benny. Benny loved to explore the woods and meadows around his cozy little burrow. One sunny afternoon, while hopping through a particularly dense thicket, Benny stumbled upon a hidden clearing. In the center of the clearing stood an old, gnarled tree, its branches twisted and tangled in a way that seemed almost magical. Benny felt drawn to the tree, as if it held secrets and stories that only he could hear. As he approached, the wind rustled through the leaves, whispering ancient tales of wonder and adventure"

# Improved tokenization with lowercase and punctuation removal
words = re.findall(r'\w+', text.lower())  # Better tokenization [2][5]

# Generate trigrams and bigrams
trigrams = []
bigrams = []
for i in range(len(words)):
    if i + n <= len(words):
        trigrams.append(tuple(words[i:i+n]))
    if i + 2 <= len(words):
        bigrams.append(tuple(words[i:i+2]))

# Count frequencies
trigram_counts = {}
for t in trigrams:
    trigram_counts[t] = trigram_counts.get(t, 0) + 1

bigram_counts = {}
for b in bigrams:
    bigram_counts[b] = bigram_counts.get(b, 0) + 1

# Calculate probabilities [3][7]
probabilities = {}
for trigram, count in trigram_counts.items():
    prefix = trigram[:2]  # Get first two words of trigram
    prefix_count = bigram_counts.get(prefix, 0)
    
    # Apply Laplace smoothing to avoid zero probability [3]
    probability = (count + 1) / (prefix_count + len(bigram_counts))
    probabilities[trigram] = probability

# Print top 10 probabilities
sorted_probs = sorted(probabilities.items(), key=lambda x: -x[1])
for trigram, prob in sorted_probs[:10]:
    print(f"{' '.join(trigram)}: {prob:.4f}")
