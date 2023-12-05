import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.stats import multivariate_normal

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data[:, :2]  # 仅使用鸢尾花数据集的前两个特征
y = iris.target

# 仅保留两个类别（0和1）
X = X[y < 2]
y = y[y < 2]

# 将数据合并，并创建对应的标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 计算类别的先验概率
prior_class0 = np.sum(y_train == 0) / len(y_train)
prior_class1 = np.sum(y_train == 1) / len(y_train)

# 计算类别的类条件概率（假设服从正态分布）
class0 = X_train[y_train == 0]
class1 = X_train[y_train == 1]

class0_mean = np.mean(class0, axis=0)
class1_mean = np.mean(class1, axis=0)

class0_cov = class1_cov = np.cov(X_train.T)

# 定义贝叶斯分类器函数
def bayes_classifier(x):
    # 计算类条件概率
    class0_prob = multivariate_normal.pdf(x, class0_mean, class0_cov)
    class1_prob = multivariate_normal.pdf(x, class1_mean, class1_cov)
    
    # 计算后验概率
    posterior_class0 = class0_prob * prior_class0
    posterior_class1 = class1_prob * prior_class1
    
    # 返回后验概率较大的类别
    return 0 if posterior_class0 > posterior_class1 else 1

# 绘制散点图
plt.figure(figsize=(8, 6))
plt.scatter(class0[:, 0], class0[:, 1], label='Class 0')
plt.scatter(class1[:, 0], class1[:, 1], label='Class 1')

# 绘制决策边界
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = np.array([bayes_classifier(np.array([x, y])) for x, y in np.c_[xx.ravel(), yy.ravel()]])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.2, cmap='coolwarm')  # 修改透明度和颜色映射
plt.rcParams['image.interpolation'] = 'nearest'

plt.title('Iris Data with Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

# 对测试集进行分类预测
y_pred = np.array([bayes_classifier(x) for x in X_test])

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")