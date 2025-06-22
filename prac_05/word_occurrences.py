"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

text = input("Text: ")
words = text.split()
word_to_count = {}

# Count each word
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1


sorted_words = sorted(word_to_count.keys())


max_word_length = max(len(word) for word in sorted_words)


for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")