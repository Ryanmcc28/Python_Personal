words = open('word_list', 'r')

word_set = set()
for word in words:
    word_set.add(word.strip('\n'))
print(word_set)