from sklearn.datasets import load_iris
from sklearn import tree
#from sklearn.cross_validtion import train_test_split
from sklearn.model_selection import train_test_split

#讀入鳶尾花資料
iris = load_iris()
iris_x = iris.data
iris_y = iris.target

#切分 訓練資料 與 測試資料
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y, test_size = 0.3)

#建立分類器
clf = tree.DecisionTreeClassifier()
iris_clf = clf.fit(train_x, train_y)

#預測
test_y_predicted = iris_clf.predict(test_x)
print(test_y_predicted)

#標準答案
print(test_y)

