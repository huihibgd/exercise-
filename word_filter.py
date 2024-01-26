import re
import string

def word_filter_counter(text, filter_words):
    result={}
    words=re.sub(f"[{string.punctuation}]"," ",text).split()
    filter=re.sub(f"[{string.punctuation}]"," ",str(filter_words)).split()
    for word2 in filter:
        count=0
        for word1 in words:
         if word1.upper() == word2.upper():
            count=count + 1
        result[word2]=count
    print(result)
word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"])
