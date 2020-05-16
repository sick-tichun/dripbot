from textblob import TextBlob

words_r = open("/home/tichun/Documents/python/words.txt", "r")
print(words_r.read())
words_r.close()

words_a = open("/home/tichun/Documents/python/words.txt", "a+")
n_word = input('add extra word: ')
words_a.write(str(n_word + ' \r\n'))
words_a.close()

words_r = open("/home/tichun/Documents/python/words.txt", "r")
n_list = words_r.read()
print(n_list)

