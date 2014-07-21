#TODO
#calculate coverage
import utils
from pymongo import MongoClient
from collections import Counter

words = utils.getWords()
reviews = MongoClient()['nlp_test'].switch_reviews
query = reviews.find()

total, cover = 0, 0
cnt = Counter()
cnt2 = Counter()
for q in query:
    for w, p in q['cut']['pseg']:
        cnt2[w] += 1
        total += 1
        if w in words:
            cnt[w] += 1
            cover +=1

print("{}, {}, {}".format(cover, total, cover/total))

