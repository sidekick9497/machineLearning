from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
import random
import matplotlib.pyplot as plt
class firstAlgortihm():
    def fit(self,x_train,y_train):
        self.x_train = x_train
        self.y_train = y_train
    def predict(self,x_test):
        predictions = []
        for i in range(len(x_test)):
             predictions.append(random.choice(self.y_train))
        return predictions
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_test,y_train = train_test_split(x,y,test_size=.5)
# myClassifier = KNeighborsClassifier()
# myClassifier.fit(x_train,y_train)
# predictions = myClassifier.predict(x_test)
sp_lenght_width = x_test[:,:2]
h = .02

myClassifier = firstAlgortihm()
myClassifier.fit(x_train,y_train)
myPredictions = myClassifier.predict(x_test)
plt.plot(x_train,y_train)
plt.show()
print(myPredictions)
