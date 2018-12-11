from dataset import Dataset
from sentiment import SentimentAnalysis

dtIMDB = Dataset('/media/daniel/Storage/Documentos/Unifor/IA/weka_data/IMDB_1_1', r'(.*),(neg|pos),(neg|pos),\d+')
dtSWN = Dataset('/media/daniel/Storage/Documentos/Unifor/IA/weka_data/SentiWordNet_3.0.0_20130122', r'(a|n|r|v|u),(\d+),(\d+(?:.\d+)?),(\d+(?:.\d+)?),((?:\s*\w+#\d+\s*)*),(.*)')

sa = SentimentAnalysis()

# def calc_sentiment(line, index):
#     comment = line[0]
#     score = sa.score(comment)
#     positivity = 'neg' if score < 0 else ('pos' if score > 0 else 'neu')
#     print(str(index)+': ' + str(len(comment)), score, positivity)
#     return positivity

# dts.add_feature('SentiWordNetSentiment', '{pos,neg,neu}', calc_sentiment)

# def calc_size(line, index):
#     comment = line[0]
#     size = len(comment)
#     print(str(index)+': ' + str(size))
#     return size

# dtIMDB.add_feature('comment_size', 'NUMERIC', calc_size)

# def qtd_oscar(line, index):
#     comment = line[0]
#     return comment.find('oscar') >= 0

# dtIMDB.add_feature('have_oscar', '{True,False}', qtd_oscar)

# def qtd_oscar(line, index):
#     comment = line[0]
#     return comment.find('oscar') >= 0

# dts.add_feature('have_oscar', '{True,False}', qtd_oscar)

dtIMDB.export_file()
