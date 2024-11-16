import pandas as pd

# 读取标注数据
data = pd.read_csv('annotations.txt', sep='\t', header=None, names=['text', 'label'])

# 查看数据
print(data.head())
