import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.linear_model import Perceptron

# 设置字体
font = FontProperties(fname=r'C:/Windows/Fonts/simhei.ttf', size=12)  # 使用黑体

# 生成线性可分或不可分数据
def generate_data(separable=True):
    np.random.seed(0)
    X = np.random.rand(100, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int) * 2 - 1
    if not separable:
        noise = np.random.normal(0, 0.1, size=y.shape)
        y = y * (1 - noise)
    return X, y

# 定义感知器算法
class MyPerceptron:
    def __init__(self, w, b=0, eta=0.1):
        self.w = np.array(w)
        self.b = b
        self.eta = eta

    def sign_y(self, xi):
        return np.dot(xi, self.w) + self.b

    def train_ppt(self, X_train, y_train, max_iter=1000):
        for _ in range(max_iter):
            wrong_count = 0
            for i in range(len(X_train)):
                xi = X_train[i]
                yi = y_train[i]
                if yi * self.sign_y(xi) <= 0:
                    self.w = self.w + self.eta * yi * xi
                    self.b = self.b + self.eta * yi
                    wrong_count += 1
            if wrong_count == 0:
                break

# 实验参数
etas = [0.01, 0.1, 0.5]
separable = True  # 尝试改为False查看不可分数据的情况
initial_weights = [[1, 1], [0.5, 0.5], [-1, -1]]

plt.figure(figsize=(15, 5))

for i, eta in enumerate(etas, 1):
    plt.subplot(1, 3, i)
    X, y = generate_data(separable)
    ppt = MyPerceptron(w=[1, 1], b=0, eta=eta)
    ppt.train_ppt(X, y)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolor='k', marker='o')
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    Z = ppt.sign_y(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, levels=[0], linewidths=2)
    plt.title(f'学习率={eta}', fontproperties=font)
    plt.xlabel('特征1', fontproperties=font)
    plt.ylabel('特征2', fontproperties=font)

plt.show()