import csv
import nltk
from nltk.corpus import stopwords
import re
import string
from collections import defaultdict
nltk.download('stopwords')
stop = stopwords.words('english')

inter1 = []
sentences_all = []
sentences_clean = []
sentences_unpun = []

dictionary1 = {}
d2_dict = defaultdict(dict)

with open('yelp_reviews_word_freq.csv') as f:
    rows = csv.reader(f, delimiter=';')
    for row in rows:
        inter1.append(row[2])

# Split the row into different sentences
for row in inter1:
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', row)
    for s in sentences:
        in1 = ''.join(s)
        out = re.sub('[%s]' % re.escape(string.punctuation), '', in1.lower())
        sentences_all.append(out)

# Remove stop words from sentence
for sentence in sentences_all:
    s = []
    for i in sentence.split():
        if i not in stop and i.isdigit() is False:
            s.append(i)
    sentences_clean.append(s)

# Add each words as key into a dictionary
for sentence in sentences_clean:
    # print sentence
    for word in sentence:
        dictionary1[word] = 0

# Update the frequency dictionary table
for sentence in sentences_clean:
    for word in sentence:
        dictionary1[word] = dictionary1[word] + 1

# Add each pair of words as key into a dictionary 2
for sentence in sentences_clean:
    for word in sentence:
        for word2 in sentence:
            if(word != word2):
                d2_dict[word][word2] = 0
# Update the frequency dictionary table
for sentence in sentences_clean:
    for word in sentence:
        for word2 in sentence:
            if(word != word2):
                d2_dict[word][word2] = d2_dict[word][word2] + 1

writer = csv.writer(open('word_freq.csv', 'w', newline=''))
for key, value in dictionary1.items():
    writer.writerow([key, value])

writer = csv.writer(open('word_pair_freq.csv', 'w', newline=''))
for key1, value1 in d2_dict.items():
    for key2, value2 in d2_dict[key1].items():
        writer.writerow([key1, key2, value2])

print("Wrote to word_freq.csv")
