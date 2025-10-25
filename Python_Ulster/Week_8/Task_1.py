word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word_set1 = set(word1)
word_set2 = set(word2)

if  word_set1 == word_set2:
    print("These words are anagrams")
else:
    print("These words are not anagrams")

print(word_set2)