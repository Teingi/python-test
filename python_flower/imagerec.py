import sys, getopt  
  
from skimage import io, transform  
import tensorflow as tf  
import numpy as np  
  
  
flower_dict = {  
    0: '菊花',  
    1: '蒲公英',  
    2: '玫瑰',  
    3: '向日葵',  
    4: '郁金香'  
}  
  
def main(argv):  
    inputfile = ""  
    try:  
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile="])  
    except getopt.GetoptError:  
        print('Error: test_arg.py -i <inputfile> -o <outputfile>')  
        print('   or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')  
        sys.exit(2)  
  
    for opt, arg in opts:  
        if opt == "-h":  
            print('test_arg.py -i <inputfile> -o <outputfile>')  
            print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')  
  
            sys.exit()  
        elif opt in ("-i", "--infile"):  
            inputfile = arg  
    print(inputfile)  
    print(recgnize(inputfile))  
  
  
def read_one_image(path):  
        img = io.imread(path)  
        img = transform.resize(img, (100, 100))  
        return np.asarray(img)  
  
  
  
def recgnize(filename):  
            with tf.Session() as sess:  
                data = []  
                data.append(read_one_image(filename))  
  
                saver = tf.train.import_meta_graph('E:/code/python/python_flower/flower/model.ckpt.meta')  
                saver.restore(sess, tf.train.latest_checkpoint('E:/code/python/python_flower/flower/'))  
  
                graph = tf.get_default_graph()  
                x = graph.get_tensor_by_name("x:0")  
                feed_dict = {  
                x: data  
                }  
                logits = graph.get_tensor_by_name("logits_eval:0")  
                classification_result = sess.run(logits, feed_dict)# 打印出预测矩阵  
                #print(classification_result)# 打印出预测矩阵每一行最大值的索引  
                #print(tf.argmax(classification_result, 1).eval())# 根据索引通过字典对应花的分类  
                output = []  
                output = tf.argmax(classification_result, 1).eval()  
                for i in range(len(output)):  
                    #print("第", i + 1, "朵花预测:" + flower_dict[output[i]])  
                    return flower_dict[output[i]]  
  
if __name__ == "__main__":  
    main(sys.argv[1: ])  
