from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import tree
iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.5)
myclassifier = tree.DecisionTreeClassifier()
myclassifier.fit(x,y)