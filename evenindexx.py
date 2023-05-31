word = input('Enter word: ')
size = len(word)
for i in range(0, size, 2):
    print("index[", i, "]", word[i])