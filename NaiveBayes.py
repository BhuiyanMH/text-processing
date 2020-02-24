import nltk
import csv

training_set = []
with open('C:/data/nbdata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        training_set.append((row['age'], row['income'], row['isStudent'], row['creditRating'], row['buysComputer']))
print(training_set)

#classifier = nltk.NaiveBayesClassifier.train(training_set)
#print(classifier.prob_classify({'age': 'youth', 'income': 'high', 'isStudent': 'no', 'creditRating': 'fair'}).prob('yes'))
