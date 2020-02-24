import nltk
#import nltk.data
#d = nltk.data.load("C:/data/marketdata.arff", "text")
#print(d)
'''file = open("C:/data/nbdata.csv")
nvdata = csv.reader(file)

for row in nvdata:
    print(row)
print(nvdata)'''


'''labeled_featuresets = [({'viagra': 'yes', 'hello': 'no'}, 'spam'), ({'viagra': 'no', 'hello': 'yes'}, 'ok')]
classifier = nltk.NaiveBayesClassifier.train(labeled_featuresets)
print(classifier.prob_classify({'viagra': 'yes', 'hello': 'no'}).prob('spam'))'''

labeled_featuresets = [({'age': 'youth', 'income': 'high','isStudent': 'no', 'creditRating': 'fair'}, 'no'),
                       ({'age': 'youth', 'income': 'high', 'isStudent': 'no', 'creditRating': 'excellent'}, 'no'),
                       ({'age': 'middleAged', 'income': 'medium', 'isStudent': 'no', 'creditRating': 'fair'}, 'yes'),
                       ({'age': 'senior', 'income': 'low', 'isStudent': 'yes', 'creditRating': 'fair'}, 'yes'),
                       ({'age': 'senior', 'income': 'low', 'isStudent': 'yes', 'creditRating': 'excellent'}, 'no'),
                       ({'age': 'middleAged', 'income': 'low', 'isStudent': 'yes', 'creditRating': 'excellent'}, 'yes')]

test_set = labeled_featuresets[3:]

classifier = nltk.classify.DecisionTreeClassifier.train(labeled_featuresets, entropy_cutoff=0, support_cutoff=0)
sorted(classifier.labels())
print(classifier)
print(classifier.classify({'age': 'youth', 'income': 'medium', 'isStudent': 'no', 'creditRating': 'fair'}))
print("Classifier Accuracy: " , (nltk.classify.accuracy(classifier, test_set)*100))

'''test_set = labeled_featuresets[3:]
training_set = labeled_featuresets[:3]
classifier  = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier Accuracy: " , (nltk.classify.accuracy(classifier, test_set)*100))
classifier = nltk.NaiveBayesClassifier.train(labeled_featuresets)
print(classifier.prob_classify({'age': 'youth', 'income': 'medium', 'isStudent': 'no', 'creditRating': 'fair'}).prob('no'))'''