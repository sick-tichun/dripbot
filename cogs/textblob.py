import discord, nltk, random
from discord.ext import commands
from textblob import TextBlob, Word
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.corpus import brown
from nltk.tag import UnigramTagger



def create():
    
    with open('words.txt', 'r') as f:
        words_list = [line.strip() for line in f]
    count=len(words_list)

    
    adjectives = []
    nouns = []
    adverbs = []
    verbs = []
    tagged_list =[[],[]]


    print(str(count) + ' words loaded')
    for i in range(0, count):
        tagged = nltk.pos_tag(nltk.tokenize.word_tokenize(words_list[i]), tagset='universal')
        tagged_list[0].append(tagged[0][0])
        tagged_list[1].append(tagged[0][1])
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





class textblob(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def nltk_update(self, ctx):
        "updates nltk libaries, use if word tagging isnt working"
        nltk.download('wordnet')
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('universal_tagset')


    @commands.command()
    async def trans(self, ctx, text, lang):
        "translates your message (remember speach marks!!)"
        await ctx.send(TextBlob(text).translate(to=lang))

    @commands.command()
    async def meaning(self, ctx, defword):
        "defines a word"
        defenition_w = Word(defword).definitions
        await ctx.send(defenition_w)

    @commands.command()
    async def sentence(self, ctx):
        "creates a (usually) gramatically scentance"
        await ctx.send(create())

    @commands.command()
    async def addword(self, ctx, word_to_add):
        "adds words to the scentance creation dictionary"
        word_add(word_to_add)
        await ctx.send('added ' + word_to_add + ' to the list of words')

    @commands.command()
    async def readwords(self, ctx):
        "sends the entire dictionary of words so fat but gets cut off"
        await ctx.send(word_read())

def setup(client):
    client.add_cog(textblob(client))