#---coding:utf-8----
#词频统计


import codecs
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

word = []
counter = {}

with codecs.open('E:\\code\\1.txt') as fr:
    for line in fr:
        line = line.strip()
        if len(line) == 0:
            continue
        for w in line:
            if not w in word:
                word.append(w)
            if not w in counter:
                counter[w] = 0
            else:
                counter[w] += 1

counter_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print(counter_list[:50])

label = list(map(lambda x: x[0], counter_list[:50]))
value = list(map(lambda y: y[1], counter_list[:50]))

plt.bar(range(len(value)), value, tick_label=label)
plt.show()
