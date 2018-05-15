import numpy as np
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf

def create_captcha(text, shear=0, size=(100, 24)):
    im = Image.new("L", size, "black")#使用字母L来生成一张黑白图像，为ImageDraw类初始化一个实例
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(r"E:\code\python\test\chapter08\Coval.otf", 22)
    draw.text((2, 2), text, fill=1, font=font)
    #把 PIL图像转换为numpy数组，以便用scikit-image库为图像添加错切变化效果
    image = np.array(im)

    #然后，应用错切变化效果，返回图像。
    affine_tf = tf.AffineTransform(shear=shear)
    image = tf.warp(image, affine_tf)
    #这一行代码对图像特征进行归一化处理，确保特征值落在0到1之间
    return image / image.max()

#生成验证码图像并显示它
from matplotlib import pyplot as plt
image = create_captcha("ABCDE", shear=0.5)
implot = plt.imshow(image, cmap='gray')
plt.show()

################################将图像切分为单个的字母######################################
from skimage.measure import label, regionprops
#图像分割函数接收图像，返回小图像列表，每张小图像为单词的一个字母，函数声明如下：


def segment_image(image):
    #label函数的参数为图像数组，返回跟输入同型的数组。
    labeled_image = label(image > 0)
    #抽取每一张小图像，将它们保存到一个列表中。
    subimages = []
    #scikit-image库还提供抽取连续区域的函数： regionprops。遍历这些区域
    for region in regionprops(labeled_image):
        #这样，通过region对象就能获取到当前区域的相关信息。我们这里要用到当前区域的起始
        #和结束位置的坐标
        start_x, start_y, end_x, end_y = region.bbox
        subimages.append(image[start_x:end_x,start_y:end_y])
    if len(subimages) == 0:
        return [image,]
    return subimages

subimages = segment_image(image)
f, axes = plt.subplots(1, len(subimages), figsize=(10, 3))
for i in range(len(subimages)):
    axes[i].imshow(subimages[i], cmap="gray")
plt.show()


############################创建训练集#############################################
from sklearn.utils import check_random_state
random_state = check_random_state(14)
letters = list("ACBDEFGHIJKLMNOPQRSTUVWXYZ")
shear_values = np.arange(0, 0.5, 0.05)

#再来创建一个函数（用来生成一条训练数据），从我们提供的选项中随机选取字母和错切值
def generate_sample(random_state=None):
    random_state = check_random_state(random_state)
    letter = random_state.choice(letters)
    shear = random_state.choice(shear_values)
    #返回字母图像及表示图像中字母属于哪个类别的数值。字母A为类别0， B为类别1， C为类别2,依次类推
    return create_captcha(letter, shear=shear, size=(20, 20)), letters.index(letter)

#在上述函数体的外面，调用该函数，生成一条训练数据，用pyplot显示图像
image, target = generate_sample(random_state)
plt.imshow(image, cmap="gray")
plt.show()
print("The target for this image is: {0}".format(target))


#调用几千次该函数，就能生成足够的训练数据。把这些数据传入到numpy的数组里
dataset, targets = zip(*(generate_sample(random_state) for i in
range(3000)))
dataset = np.array(dataset, dtype='float')
targets = np.array(targets)

#我们共有26个类别，每个类别（字母）用从0到25之间的一个整数表示。神经网络一般不支
#持一个神经元输出多个值，但是多个神经元就能有多个输出，每个输出值在0到1之间。因此，我
#们对类别使用一位有效码编码方法，这样，每条数据就能得到26个输出。如果结果像某字母，使
#用近似于1的值；如果不像，就用近似于0的值。代码如下

from sklearn.preprocessing import OneHotEncoder
onehot = OneHotEncoder()
y = onehot.fit_transform(targets.reshape(targets.shape[0],1))

#我们用的库不支持稀疏矩阵，因此，需要将稀疏矩阵转换为密集矩阵。代码如下：
y = y.todense()

###################################根据抽取方法调整训练数据集############################
from skimage.transform import resize
#现在，就可以对每条数据运行segment_image函数，将得到的小图像调整为20像素见方
dataset = np.array([resize(segment_image(sample)[0], (20, 20)) for
sample in dataset])
#最后，创建我们的数据集。 dataset数组为三维的，因为它里面存储的是二维图像信息。
X = dataset.reshape((dataset.shape[0], dataset.shape[1] * dataset.shape[2]))
#使用scikit-learn中的train_test_split函数，把数据集切分为训练集和测试集
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
train_test_split(X, y, train_size=0.9)


##################################训练和分类####################################
'''
我们将使用之前创建的单个字母训练集。数据集本身很简单。每张图像为20像素大小，每个
像素用1（黑）或0（白）来表示。每张图像有400个特征，将把它们作为神经网络的输入。输出
结果为26个0到1之间的值。值越大，表示图像中的字母为该值所对应的字母（输出的第一个值对
应字母A，第二个对应字母B，以此类推）的可能性越大
'''
#我们用PyBrain库来构建神经网络分类器
from pybrain.datasets import SupervisedDataSet
#首先，遍历我们的训练集，把每条数据添加到一个新的SupervisedDataSet实例中
training = SupervisedDataSet(X.shape[1], y.shape[1])
for i in range(X_train.shape[0]):training.addSample(X_train[i], y_train[i])

#然后，遍历测试集，同样把每条数据添加到一个新的SupervisedDataSet实例中。
testing = SupervisedDataSet(X.shape[1], y.shape[1])
for i in range(X_test.shape[0]):testing.addSample(X_test[i], y_test[i])

"""
现在就可以创建神经网络了。我们将创建一个最基础的、具有三层结构的神经网络，它由输
入层、输出层和一层隐含层组成。输入层和输出层的神经元数量是固定的。数据集有400个特征，
那么第一层就需要有400个神经元，而26个可能的类别表明我们需要26个用于输出的神经元。
确定隐含层的神经元数量可能相当困难。如果神经元数量过多，神经网络呈现出稀疏的特点，
这时要训练足够多的神经元恰当地表示数据就有困难，这往往会导致过拟合训练数据的问题。相
反，如果神经元过少，每个对分类结果的贡献过大，再加上训练不充分，就很可能产生低拟合现
象。我发现一开始用漏斗形状不错，即隐含层神经元数量介于输入和输出层之间。本章，隐含层
用100个神经元，你可以尝试其他值，看看能不能取得更好的效果。
导入buildNetwork函数，指定维度，创建神经网络。第一个参数X.shape[1]为输入层神
经元的数量，也就是特征数（数据集X的列数）。第二个参数指隐含层的神经元数量，这里设置
为100。第三个参数为输出层神经元数量，由类别数组y的形状来确定。最后，除去输出层外，我
们每层使用一个一直处于激活状态的偏置神经元（bias neuron，它与下一层神经元之间有边连接，
边的权重经过训练得到）。代码如下：

"""
from pybrain.tools.shortcuts import buildNetwork
net = buildNetwork(X.shape[1], 100, y.shape[1], bias=True)


################################反向传播算法训练神经网络########################################
#反向传播算法（back propagation， backprop）的工作机制为对预测错误的神经元施以惩罚。
#从输出层开始，向上层层查找预测错误的神经元，微调这些神经元输入值的权重，以达到修复输出错误的目的。

#PyBrain提供了backprop算法的一种实现，在神经网络上调用trainer类即可
from pybrain.supervised.trainers import BackpropTrainer
trainer = BackpropTrainer(net, training, learningrate=0.01,weightdecay=0.01)

#运行代码固定的步数（epoch）我们这里训练时，使用了20步
trainer.trainEpochs(epochs=20)

predictions = trainer.testOnClassData(dataset=testing)
#得到预测值后，可以用scikit-learn计算F1值。
from sklearn.metrics import f1_score
print("F-score: {0:.2f}".format(f1_score(predictions,y_test.argmax(axis=1),average='micro')))

from sklearn.metrics import classification_report
print(classification_report(y_test.argmax(axis=1), predictions))


##################################预测单词#####################################################
#定义一个函数，接收验证码，用神经网络进行训练，返回单词预测结果

def predict_captcha(captcha_image, neural_network):
    #使用前面定义的图像切割函数segment_image抽取小图像
    subimages = segment_image(captcha_image)
    predicted_word = ""
    for subimage in subimages:
        #每张小图像不太可能正好是20像素见方。调整大小后，才能用神经网络处理
        subimage = resize(subimage, (20, 20))
        #把小图像数据传入神经网络的输入层，激活神经网络
        outputs = net.activate(subimage.flatten())
        prediction = np.argmax(outputs)
        #把上面得到的字母添加到正在预测的单词中
        predicted_word += letters[prediction]
        #循环结束后，我们就已经找到了单词的各个字母，将其拼接成单词，最后返回这个单词
    return predicted_word
    #可以使用下面代码来做下测试
word = "GENE"
captcha = create_captcha(word, shear=0.2)
print(predict_captcha(captcha, net))
    
        
