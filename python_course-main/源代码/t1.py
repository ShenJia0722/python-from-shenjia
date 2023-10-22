import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 读取数据文件
data = pd.read_csv('E:\使用\大三上学期\模式识别\irisdata.txt', sep='\s+')

# 提取特征列
X = data[['x1', 'x2', 'x3', 'x4']]

# 使用“肘部法”找到最优的聚类数量
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# 绘制“肘部法”图像
plt.plot(range(1, 11), wcss)
plt.title('肘部法', fontdict={'family': 'SimSun', 'size': 12})  # SimSun 是宋体
plt.xlabel('聚类数量', fontdict={'family': 'SimSun', 'size': 12})
plt.ylabel('聚类内平方和', fontdict={'family': 'SimSun', 'size': 12})
plt.show()

# 通过“肘部法”可知最优聚类数量为3
# 使用K均值算法进行3类的聚类
kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(X)

# 可视化聚类结果
plt.scatter(X[y_kmeans == 0]['x1'], X[y_kmeans == 0]
            ['x2'], s=100, c='red', label='聚类1')
plt.scatter(X[y_kmeans == 1]['x1'], X[y_kmeans == 1]
            ['x2'], s=100, c='blue', label='聚类2')
plt.scatter(X[y_kmeans == 2]['x1'], X[y_kmeans == 2]
            ['x2'], s=100, c='green', label='聚类3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[
            :, 1], s=300, c='yellow', label='聚类中心')

# 设置字体为微软雅黑
font_properties = {'family': 'Microsoft YaHei', 'size': 12}

plt.title('聚类后的数据', fontdict=font_properties)
plt.xlabel('x1', fontdict=font_properties)
plt.ylabel('x2', fontdict=font_properties)

# 设置legend的字体
plt.legend(prop=font_properties)

plt.show()

# 打印每个样本属于哪个聚类
for i in range(len(X)):
    print(f"样本{i+1} 属于聚类 {y_kmeans[i]+1}")