from sklearn import tree
features = [[20,1],[21,1],[23,1],[45,2],[46,2],[50,2],[60,3],[61,3],[70,3],[85,4],[86,4],[88,4]]
labels= ["thin","thin","thin","normal","normal","normal","normal","normal","weight","weight","obese","obese"]
classifier = tree.DecisionTreeClassifier()
classifier.fit(features,labels)
print classifier.predict([[100,4]])