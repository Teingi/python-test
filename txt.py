filename = 'tangqing.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径
pos = []
Efield = []
with open(filename, 'r') as file_to_read:
  while True:
    lines = file_to_read.readline() # 整行读取数据
    if not lines:
      break
      pass
     p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
     pos.append(p_tmp)  # 添加新读取的数据
     Efield.append(E_tmp)
     pass
   pos = np.array(pos) # 将数据从list类型转换为array类型。
   Efield = np.array(Efield)
   pass