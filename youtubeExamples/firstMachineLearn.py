from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()

irisData = iris.data
irisTarget = iris.target

featureNames = iris.feature_names
targetNames = iris.target_names
print featureNames
print targetNames

# print "type of x is :"
# print type(irisData)
# print irisData[:5]

x_train, x_test, y_train, y_test = train_test_split(irisData, irisTarget, test_size=0.4, random_state=1)

print(x_train.shape)
print(x_test.shape)
print(x_train[:5])
print x_test[:5]
