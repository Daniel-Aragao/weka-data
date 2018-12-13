from dataset import Dataset
from sentiment import SentimentAnalysis
import re

dtIMDB = Dataset('IMDB_DANIEL_JOSEVICTOR', r'(.*),(neg|pos),(neg|pos),(\d+)')
# dtIMDB = Dataset('IMDB.jdaniel', r'(.*),(neg|pos)')
dtSWN = Dataset('SentiWordNet_3.0.0_20130122', r'(a|n|r|v|u),(\d+),(\d+(?:.\d+)?),(\d+(?:.\d+)?),((?:\s*[^#]+#\d+\s*)*),(.*)')

# print(len(dtSWN.find_by_feature_value('Pos', 'v')))
# print(len(dtSWN.lines))

sa = None

def get_sentiment_analysis():
    if not sa:
        sa = SentimentAnalysis()

    return sa    

def calc_sentiment(line, index):
    comment = line[0]
    score = get_sentiment_analysis().score(comment)
    positivity = 'neg' if score < 0 else ('pos' if score > 0 else 'neu')
    print(str(index)+': ' + str(len(comment)), score, positivity)
    return positivity


def calc_size(line, index):
    comment = line[0]
    size = len(comment)
    print(str(index)+': ' + str(size))
    return size


def interroga(line, index):
    comment = line[0]
    return comment.find('?') >= 0


def capslock(line, index):
    comment = line[0]
    counter = 0

    for e in comment:
        if e.isupper():
            counter += 1

    return counter

def exclama(line, index):
    comment = line[0]
    return comment.find('!') >= 0


adverbios = None

def getAdverbios():
    if not adverbios:
        adverbios = dtSWN.find_by_feature_value('Pos', 'v')
        adverbios = [i[4] for i in adverbios]
    
    return adverbios
        
def advs(line, index):
    comment = line[0]
    words = comment.split(' ')
    print(index)

    count = 0

    for word in words:
        for adverbio in getAdverbios():
            if adverbio.find(word) >= 0:
                count += 1
    
    return count

def less_then_seven(line, index):
    comment = line[0]
    return len(re.findall(r'\d+\s*(?:\.\d+)?', comment)) > 0


# dtIMDB.add_feature('qtd_adverbios', 'NUMERIC', advs)
# dtIMDB.add_feature('lessthenseven', '{True,False}', less_then_seven)
# dtIMDB.add_feature('SentiWordNetSentiment', '{pos,neg,neu}', calc_sentiment)
# dtIMDB.add_feature('comment_size', 'NUMERIC', calc_size)
# dtIMDB.add_feature('CAPSLOCK', 'NUMERIC', capslock)
# dtIMDB.add_feature('exclamacao', '{True,False}', exclama)
# dtIMDB.add_feature('interroga', '{True,False}', interroga)

if dtIMDB.added_features:
    dtIMDB.export_file()
