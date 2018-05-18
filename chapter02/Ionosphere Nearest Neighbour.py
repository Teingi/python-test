import os
import csv #导入csv模块
import numpy as np

#sklearn.cross_validation模块在0.18版本中被弃用，支持所有重构的类和函数都被移动到的model_selection模块
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split   
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import cross_val_score




# 数据存储地址
data_filename = "E:\\github\\Git\\test\\chapter02\\ionosphere.data"



#先创建好数组
#创建一个shape属性为（351,34），元素都为0的二维数组，存放351条数值数据，每条数值数据共有34个，数据类型为浮点型  
X = np.zeros((351, 34), dtype='float')
#创建一个shape属性为（351，）的一维数组，其形式为[0. 0. ....0.],其中每个数据对应X中的每条数据的判定结果，原始数据集中用‘g'或者’b'来表示，这里换成布尔值类型  
y = np.zeros((351,), dtype='bool')


#对数据进行转换处理
with open(data_filename, 'r') as input_file:
    reader = csv.reader(input_file)#用csv模块来导入数据及文件，并创建csv阅读器对象  
    for i, row in enumerate(reader):#遍历文件中的每一行数据
        #将每一条数据中最后一个数据前面的34个值强制转换成float类型
        data = [float(datum) for datum in row[:-1]] 
        # Set the appropriate row in our dataset
        X[i] = data#将每个索引i对应的转换后的data数据赋值给数组X中相应的每一行 
        # 1 if the class is 'g', 0 otherwise
        y[i] = row[-1] == 'g'


#scikit-learn估计器由两大函数组成： fit()和predict()，用fit方法在训练集上完成模型的创建，用predict方法在测试集上评估效果
#首先，需要创建训练集和测试集  
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)
print("训练集上有{}个样本".format(X_train.shape[0]))
print("测试集上有{}个样本".format(X_test.shape[0]))
print("每一个样本有{}个特征".format(X_train.shape[1]))


#利用K近邻分类器这个类，并为其初始化一个实例，该算法默认选择5个近邻作为分类依据
estimator = KNeighborsClassifier()
'''
函数默认参数说明
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')
'''


#估计器创建好后，接下来就要用训练数据进行训练
estimator.fit(X_train, y_train)


#接着，用测试集测试算法，评估它在测试集上的表现
y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print("在测试集上的准确率为：{0:.1f}%".format(accuracy))


#数据集分为训练集和测试集，用训练集训练算法，在测试集上
#评估效果。倘若碰巧走运，测试集很简单，我们就会觉得算法表现很出色。反之，我们可能会怀
#疑算法很糟糕。也许由于我们一时不走运，就把一个其实很不错的算法给无情抛弃了，这岂不是很可惜。
#交叉检验能解决上述一次性测试所带来的问题。
#scikit-learn提供了几种交叉检验方法。
scores = cross_val_score(estimator, X, y, scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("交叉检验后的平均准确率：{0:.1f}%".format(average_accuracy))


###################################对n_neighbors进行调参#########################################################
avg_scores = []
all_scores = []
parameter_values = list(range(1, 21))  # 测试一系列n_neighbors的值，比如从1到20，可以重复进行多次实验
for n_neighbors in parameter_values:
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(estimator, X, y, scoring='accuracy')
    #把不同n_neighbors值的得分和平均分保存起来，留作分析用
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)

#为了看起来更直观，我们可以用图表来表示n_neighbors的不同取值和分类正确率之间的关系
from matplotlib import pyplot as plt
plt.figure(figsize=(32,20))
plt.plot(parameter_values, avg_scores, '-o', linewidth=3, markersize=14)
# plt.axis([0, max(parameter_values), 0, 1.0])   #这行是设置纵坐标的起始位置的
plt.show()

#第二种图形展示
for parameter, scores in zip(parameter_values, all_scores):
    n_scores = len(scores)
    plt.plot([parameter] * n_scores, scores, '-o')

plt.plot(parameter_values, all_scores, 'bx')
plt.show()


############################################人为对数据进行破坏################################################################
X_broken = np.array(X)#为了不破坏原来的数据集，我们为其创建一个副本
X_broken[:,::2] /= 10#接下来，我们就要捣乱了，每隔一行，就把第二个特征的值除以10
estimator = KNeighborsClassifier()
original_scores = cross_val_score(estimator, X, y,scoring='accuracy')
# print("原始数据的平均准确率为：{0:.1f}%".format(np.mean(original_scores) * 100))
broken_scores = cross_val_score(estimator, X_broken, y,scoring='accuracy')
print("捣乱之后的数据平均准确率为：{0:.1f}%".format(np.mean(broken_scores) * 100))


##############################################对破坏的数据进行规范化处理######################################################
#用MinMaxScaler类进行基于特征的规范化，把特征值转变到0到1之间
from sklearn.preprocessing import MinMaxScaler#这个类可以把每个特征的值域规范化为0到1之间。最小值用0代替，最大值用1代替，其余值介于两者之间
X_transformed = MinMaxScaler().fit_transform(X)#直接调用fit_transform()函数，即可完成训练和转换


estimator = KNeighborsClassifier()
transformed_scores = cross_val_score(estimator, X_transformed, y,scoring='accuracy')
print("捣乱后经规范化处理后的平均准确率为：{0:.1f}%".format(np.mean(transformed_scores) * 100))



