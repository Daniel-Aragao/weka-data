from dataset import Dataset
from sentiment import SentimentAnalysis

dts = Dataset('/media/daniel/Storage/Documentos/Unifor/IA/weka_data/IMDB_1', r'(.*),(neg|pos),(neg|pos)')

sa = SentimentAnalysis()

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

dts.add_feature('comment_size', 'NUMERIC', calc_size)

def qtd_oscar(line, index):
    comment = line[0]
    return comment.find('oscar') >= 0

dts.add_feature('have_oscar', '{True,False}', qtd_oscar)

# def qtd_oscar(line, index):
#     comment = line[0]
#     return comment.find('oscar') >= 0

# dts.add_feature('have_oscar', '{True,False}', qtd_oscar)

dts.export_file()