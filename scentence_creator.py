import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.corpus import brown
from nltk.tag import UnigramTagger
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

def create():
    
    with open('words.txt', 'r') as f:
        words_list = [line.strip() for line in f]
    count=len(words_list)


    tagged_list =[[],[]]
    print(str(count) + ' words loaded')
    for i in range(0, count):
        tagged = nltk.pos_tag(nltk.tokenize.word_tokenize(words_list[i]), tagset='universal')
        tempword = tagged[0][0]
        temptag = tagged[0][1]
        tagged_list[0].append(tempword)
        tagged_list[1].append(temptag)

    
    adjectives = []
    nouns = []
    adverbs = []
    verbs = []

    for i in range(0, count):
        if tagged_list[1][i] == 'ADJ':
            adjectives.append(tagged_list[0][i])
        if tagged_list[1][i] == 'NOUN':
            nouns.append(tagged_list[0][i])
        if tagged_list[1][i] == 'ADV':
            adverbs.append(tagged_list[0][i])
        if tagged_list[1][i] == 'VERB':
            verbs.append(tagged_list[0][i])

    scentence_decider = random.randint(0, 1)
    if scentence_decider == 0:
        fin_scentence = 'the ' + adjectives[random.randint(0, len(adjectives))-1] + ' ' + nouns[random.randint(0, len(nouns)-1)] + ' ' + verbs[random.randint(0, len(verbs)-1)] + ' ' + adverbs[random.randint(0, len(adverbs)-1)] + '.'
    if scentence_decider == 1:
        fin_scentence = adverbs[random.randint(0, len(adverbs)-1)] + ' ' + nouns[random.randint(0, len(nouns)-1)] + ' ' + verbs[random.randint(0, len(verbs)-1)] + ' their ' + nouns[random.randint(0, len(nouns)-1)] + "'s " + adjectives[random.randint(0, len(adjectives)-1)] + ' ' + nouns[random.randint(0, len(nouns)-1)]
    return fin_scentence