import torch
import torch.nn as nn
from torch.autograd import Variable
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(1000, 5) # 1000个样本，每个样本5个特征
y = np.argmax(X, axis=1) # 标签是最大值的索引
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)

# 定义网络
class TorchModel(nn.Module):

def __init__(self):
super(TorchModel, self).__init__()
self.linear = nn.Linear(5, 5) # 输入和输出都是5
self.activation = torch.sigmoid # sigmoid归一化函数

def forward(self, x):
return self.linear(x)


# 实例化网络和优化器以及损失函数
model = TorchModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# 训练模型
for epoch in range(1000):
optimizer.zero_grad()

outputs = model(X)
loss = criterion(outputs, y)
loss.backward()
optimizer.step()
# 每100轮打印一次损失值
if epoch % 100 == 0:
print('epoch {}, loss {}'.format(epoch, loss.item()))

# plt.plot(epoch, loss, label="loss") # 画loss曲线
# plt.legend()
# plt.show()

# 训练完成后计算预测准确率
test_vec = [[0.07889086,0.15229675,0.31082123,0.03504317,0.18920843],
[0.94963533,0.5524256,0.95758807,0.95520434,0.84890681],
[0.78797868,0.67482528,0.13625847,0.34675372,0.19871392],
[0.19349776,0.59416669,0.92579291,0.41567412,0.7358894]]
test_vec_tensor = torch.tensor(test_vec,dtype=torch.float32)
model.eval() # 切换到评估模式
with torch.no_grad():
outputs = model(test_vec_tensor)
_, predicted = torch.max(outputs, 1)

print("预测的类别：", predicted)