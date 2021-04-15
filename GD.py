# task 1
def sigmoid(x):
    s = 1/(1+np.exp(-x)) 
    return s
    
def sigmoid_der(x):
    s = sigmoid(x)
    ds = s*(1-s)
    return ds

def findxi(wg,data):
    var =np.array([])
    kk=[]
    m = len(data[1:])
    for i in range(0,m):
        var = wg[0] + (wg[1] * data.iloc[i,0]) + (wg[2] * data.iloc[i,1]) + (wg[3] * data.iloc[i,2]) + (wg[4] * data.iloc[i,3]) + (wg[5] * data.iloc[i,4]) + (wg[6] * data.iloc[i,5])
        kk.append(var)
    return(kk)

def piii(x):
    newvar=np.array([])
    mm=[]
    for i in range(1,len(x)):

        newvar = sigmoid(x[i])
        mm.append(newvar)
    return(mm)       

def coff(p,y,x):
    d = np.array([])
    tt=[]
    for i in  range(1,x):
        d = 2 * (y[i]-p[i]) * sigmoid_derivative(x[i])
        tt.append(d)
        return(tt)

def mse(x,y,ypred):
    
    n = len(x)
    return (1/n) * sum([val**2 for val in (y-y_predicted)])
    
def pred(wg,data):
    x=findxi(wg,data)
    s=sigmoid(x)
    return(s)

# task 2    

import numpy as np 
import pandas as pd 

data = pd.read_csv('../input/autompg-dataset/auto-mpg.csv')

data['high'] = data['mpg']>22
data['origin3']= data['origin']>2
data['origin2']= data['origin']==2
data['origin1']= data['origin']<2
data['high'] = pd.get_dummies(data['high'], drop_first=True)
data['origin3'] = pd.get_dummies(data['origin3'], drop_first=True)
data['origin2'] = pd.get_dummies(data['origin2'], drop_first=True)
data['origin1'] = pd.get_dummies(data['origin1'], drop_first=True)

data1 = data.drop(['mpg','cylinders','displacement','acceleration','car name'],axis=1)

y=data1['high']
x= data1.drop(['high'],axis=1)

# task 3

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=430)


wg=np.random.uniform(-0.7,0.7,7)
x=findxi(beta,train_data)
s=sigmoid(x)
c=coff(k,train-data,x)
MSE=mse(k,train_data)


