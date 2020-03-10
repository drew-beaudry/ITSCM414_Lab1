# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:43:40 2019

@author: platta
FROM: https://stackoverflow.com/questions/27889873/clustering-text-documents-using-scikit-learn-kmeans-in-python

"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

"***********SHOW BELOW WITH 2 AND 3 CLUSTERS"
true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per k-means cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print ("Cluster %d:" % i,)
    for ind in order_centroids[i, :10]:
        print (' %s' % terms[ind],)
    print

print(model.labels_)
    
"WORKS THROUGH HERE"
"NOW LETS TRY HAC"
from sklearn.cluster import AgglomerativeClustering

"***********SHOW BELOW WITH 2 AND 3 CLUSTERS"
cluster = AgglomerativeClustering(n_clusters=true_k, affinity='euclidean', linkage='ward')  
cluster.fit_predict(X.toarray())  

