#数据库导入
import numpy as np
import pandas as pd
#交叉验证
from sklearn.model_selection import StratifiedKFold, KFold
#模型的选择，导入模型
from sklearn.svm import SVR
#读入文件
train = pd.read_csv(r'E:\机器学习实验\工程\train.csv',engine='python')
test = pd.read_csv(r'E:\机器学习实验\工程\test.csv',engine='python')
#分离数据集
X_train_c = train.drop(['ID','CLASS'], axis=1).values
y_train_c = train['CLASS'].values
X_test_c = test.drop(['ID'], axis=1).values
#数据划分为5份
nfold = 5
kf = KFold(n_splits=nfold, shuffle=True, random_state=2020)
prediction1 = np.zeros((len(X_test_c), ))
i = 0
#分别对测试集和训练集进行
for train_index, valid_index in kf.split(X_train_c, y_train_c):
    print("\nFold {}".format(i + 1))
    X_train, label_train = X_train_c[train_index],y_train_c[train_index]
    X_valid, label_valid = X_train_c[valid_index],y_train_c[valid_index]
    # 定义一个SVR函数，kernel、gamma定义为超参数
    clf=SVR(kernel='rbf',C=1,gamma='scale')
    # 训练模型
    clf.fit(X_train,label_train)
    x1 = clf.predict(X_valid)
    y1 = clf.predict(X_test_c)
    prediction1 += ((y1)) / nfold
    i += 1
result1 = np.round(prediction1)
id_ = range(210,314)
df = pd.DataFrame({'ID':id_,'CLASS':result1})
#预测的结果数据放在baseline.csv中
df.to_csv(r'E:\机器学习实验\工程\baseline.csv', index=False)