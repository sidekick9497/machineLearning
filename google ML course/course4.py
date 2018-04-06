from sklearn import datasets
#import the splitting module
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
#load data set
iris = datasets.load_iris()

x = iris.data
y = iris.target
# split the data into two parts now,, keep your blades sharp

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=.5)
#lets start the engine,, i mean load the classifier
my_tree_classifier = tree.DecisionTreeClassifier()
my_tree_classifier.fit(x_train,y_train)
predictions = my_tree_classifier.predict(x_test)
print accuracy_score(y_test,predictions)
my_neighbour_classifier = KNeighborsClassifier()
my_neighbour_classifier.fit(x_train,y_train)
ktest = my_neighbour_classifier.predict(x_test)
print accuracy_score(ktest,y_test)
