from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
mykneighbourClassifier = KNeighborsClassifier(n_neighbors=3)
mykneighbourClassifier.fit(X,Y)

treeClassifier = tree.DecisionTreeClassifier()
treeClassifier.fit(X,Y)

svmClassifier = svm.SVC(probability=True)
svmClassifier.fit(X,Y)

forestClassifier = RandomForestClassifier()
forestClassifier.fit(X,Y)

print(mykneighbourClassifier.predict([[180,80,45]]))
print(forestClassifier.predict([[180,80,45]]))