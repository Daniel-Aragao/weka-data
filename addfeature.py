from dataset import Dataset
from sentiment import SentimentAnalysis
import re

dtIMDB = Dataset('IMDB_1_1', r'(.*),(neg|pos),(neg|pos),(\d+)')
# dtIMDB = Dataset('IMDB.jdaniel', r'(.*),(neg|pos)')
dtSWN = Dataset('SentiWordNet_3.0.0_20130122', r'(a|n|r|v|u),(\d+),(\d+(?:.\d+)?),(\d+(?:.\d+)?),((?:\s*[^#]+#\d+\s*)*),(.*)')

# sa = SentimentAnalysis()

# print(len(dtSWN.find_by_feature_value('Pos', 'v')))
# print(len(dtSWN.lines))

# def calc_sentiment(line, index):
#     comment = line[0]
#     score = sa.score(comment)
#     positivity = 'neg' if score < 0 else ('pos' if score > 0 else 'neu')
#     print(str(index)+': ' + str(len(comment)), score, positivity)
#     return positivity

# dts.add_feature('SentiWordNetSentiment', '{pos,neg,neu}', calc_sentiment)

def calc_size(line, index):
    comment = line[0]
    size = len(comment)
    print(str(index)+': ' + str(size))
    return size

dtIMDB.add_feature('comment_size', 'NUMERIC', calc_size)

def interroga(line, index):
    comment = line[0]
    return comment.find('!') >= 0

dtIMDB.add_feature('interroga', '{True,False}', interroga)

def capslock(line, index):
    comment = line[0]
    counter = 0

    for e in comment:
        if e.isupper():
            counter += 1

    return counter

dtIMDB.add_feature('CAPSLOCK', 'NUMERIC', capslock)

# def exclama(line, index):
#     comment = line[0]
#     return comment.find('!') >= 0

# dtIMDB.add_feature('exclamacao', '{True,False}', exclama)


# adverbios = dtSWN.find_by_feature_value('Pos', 'v')
# adverbios = [i[4] for i in adverbios]

# def advs(line, index):
#     comment = line[0]
#     words = comment.split(' ')
#     print(index)

#     count = 0

#     for word in words:
#         for adverbio in adverbios:
#             if word == adverbio:
#                 count += 1
    
#     return count

# dtIMDB.add_feature('qtd_adverbios', 'NUMERIC', advs)

# def less_then_seven(line, index):
#     comment = line[0]
#     return len(re.findall(r'\d+\s*(?:\.\d+)?', comment)) > 0

# dtIMDB.add_feature('lessthenseven', '{True,False}', less_then_seven)


if dtIMDB.added_features:
    dtIMDB.export_file()
