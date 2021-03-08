import numpy as np
import pandas as pd
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

train_data = np.loadtxt('train_data.txt', dtype=np.float32, delimiter='	')
train_truth= np.loadtxt('train_truth.txt', dtype=np.float32, delimiter='	')
test_data = np.loadtxt('test_data.txt', dtype=np.float32, delimiter='	')
test_predict = np.loadtxt('test_predict.txt', dtype=np.float32, delimiter='	')
# df_news = pd.read_table('train_data.txt',header = None)
# print(df_news[0])
# df_news.as_matrix()
# train_data = np.array(df_news)
# print(train_data)
# print(a[1:])

# df_news = pd.read_table('train_truth.txt',header = None)
# print(df_news[0])
# df_news.as_matrix()
# train_truth = np.array(df_news)
# print(a[1:])

# df_news = pd.read_table('test_data.txt',header = None)
# print(df_news[0])
# df_news.as_matrix()
# test_data = np.array(df_news)
# print(a[1:])

# df_news = pd.read_table('test_predict.txt',header = None)
# print(df_news[0])
# df_news.as_matrix()
# test_predict = np.array(df_news)
# print(a[1:])

# print(train_data[1:][0])
# train_truth[1:].astype(np.float)
train_data = torch.from_numpy(train_data)
train_truth = torch.from_numpy(train_truth)
x , y =(Variable(train_data),Variable(train_truth))

test_data = torch.from_numpy(test_data)
test_predict = torch.from_numpy(test_predict)
testx, testy = (Variable(test_data), Variable(test_predict))
class simpleNet(nn.Module):
    def __init__(self,n_input,n_hidden,n_output):
        super(simpleNet,self).__init__()
        self.hidden1 = nn.Linear(n_input,n_hidden)
        self.hidden2 = nn.Linear(n_hidden,n_hidden)
        self.predict = nn.Linear(n_hidden,n_output)
    def forward(self,input):
        out = self.hidden1(input)
        out = F.relu(out)
        out = self.hidden2(out)
        out = F.sigmoid(out)
        out =self.predict(out)

        return out
spNet = simpleNet(3, 20, 1)
optimizer = torch.optim.SGD(spNet.parameters(),lr = 0.001)
loss_func = torch.nn.MSELoss()

for t in range(1000):
    prediction = spNet(x)
    loss = loss_func(prediction,y)
    print('第{}epoch，loss为{}'.format(t, loss))
	# losslist.append(loss)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()	
torch.save(spNet.state_dict(), 'car.pkl')

# predict
spNet.load_state_dict(torch.load('./car.pkl'))
spNet.eval()

prediction = spNet(testx)
