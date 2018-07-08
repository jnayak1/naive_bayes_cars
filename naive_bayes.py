import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
import numpy as np
from sklearn.pipeline import Pipeline
import pymysql
import random
from env import *

host = HOST
port = 3306
dbname = DB_NAME
user = USER
password = PASSWORD

CONN = pymysql.connect(host, user=user,port=port,
                                   passwd=password, db=dbname)

def get_data():
    cursor = CONN.cursor()
    cursor.execute("""
        SELECT Year, Title, Make, Model, Trim, Color, Dealership, Location
        FROM price_difference
        WHERE PriceDifference > 100;
    """)
    change = cursor.fetchall()

    cursor.execute("""
        SELECT Year, Title, Make, Model, Trim, Color, Dealership, Location
        FROM price_difference
        WHERE PriceDifference < 101;
    """)
    no_change = cursor.fetchall()

    corpus = []
    test = []
    test_target = []
    for tup in change:
        line = ""
        for word in tup:
            line += str(word) + " "
        if random.random() < 0.7:
            corpus.append(line)
        else:
            test.append(line)
            test_target.append(1)
    count1 = len(corpus)

    for tup in no_change:
        line = ""
        for word in tup:
            line += str(word) + " "
        if random.random() < 0.7:
            corpus.append(line)
        else:
            test.append(line)
            test_target.append(0)
    count0 = len(corpus) - count1
    
    target = [1] * count1
    target.extend([0] * count0)

    return (corpus, target, test, test_target)


def naive_bayes(corpus, target):
    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                                alpha=1e-3, random_state=42,
                                                max_iter=5, tol=None)),
    ])
    text_clf.fit(corpus, target)
    return text_clf

def test_model(text_clf, test, test_target):
    predicted = text_clf.predict(test)
    print(metrics.classification_report(test_target, predicted,
        target_names=["no_change", "change"]))
    return np.mean(predicted == test_target) 

if __name__ == '__main__':
    data = get_data()
    corpus = data[0]
    target = data[1]
    test = data[2]
    test_target = data[3]
    text_clf = naive_bayes(corpus, target)
    print(test_model(text_clf, test, test_target))
















