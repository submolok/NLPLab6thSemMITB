# Greedy Tokenizer

text = "shesellsseashellslol"
vocab = ["she", "sells", "sea", "shells", "he"]
vocab.sort(key= lambda x: len(x), reverse= True)
ans =[]
while text:
    print(text)
    for x in vocab:
        if(len(text)<len(x)):
            continue
        if(text[:len(x)]==x):
            ans.append(x)
            text = text[len(x):]
            break
# someone please add a condition to quit the loop when the remaining token is not int the vocab plz
print(ans)