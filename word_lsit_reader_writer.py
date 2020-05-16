def word_add(word):
    words_a = open("words.txt", "a+")
    n_word = word
    words_a.write(str(n_word + ' \r\n'))
    words_a.close()
def word_read():
    words_r = open("words.txt", "r")
    listofword = (words_r.read())
    words_r.close()
    return(listofword)