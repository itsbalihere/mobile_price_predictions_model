# all importtent module 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# import data 
data = pd.read_csv('mobile_dataset_100k.csv')

# data to data frame
df = pd.DataFrame(data)

# drop unuse data 
df.drop("Model",axis=1,inplace=True)


# converd to x and y lebal
X = df[['Brand', 'RAM', 'Storage', 'Screen Type', 'Condition', 'Model Age']]
y = df["Price"]

# train and test data 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# import and train model 
model = LinearRegression()
model.fit(X_train,y_train)

# input convert to int
brand  = None
screen = None
candtion = None
model_age = None

brand1 = (input("enter a brend :"))
screen1 = (input("Enter a screen Type :"))
candtion1 = (input("Enter a Candetion :"))
model_age1 =(input('Enter a Model Age :'))
ram = int(input("Enter Youer Ram :"))
storge = int(input("Enter Youer Storge :"))


if brand1 == 'samsung':
    brand = 0
if brand1 ==  'vivo':
    brand = 1
if brand1 == "oppo":
    brand = 2
if brand1 == 'redmi':
    brand = 3
if screen1 == 'soper amoled':
    screen = 0
if screen1 == "amoled":
    screen = 1
if screen1 == 'lcd':
    screen = 2
if screen1 == 'ips':
    screen = 3
if candtion1 == 'new':
    candtion = 0
if candtion1 == 'good':
    candtion = 1
if candtion1 ==  'normal':
    candtion = 2
if candtion1 == 'bad':
    candtion = 3
if model_age1 == 'new':
    model_age = 0
if model_age1 == 'old':
    model_age = 1        

# new data 
new_data = [[brand,ram,storge,screen,candtion,model_age]]

# Model predictions
predictions= model.predict(new_data)
print (f'Youer Mobile Price Is : {predictions:.0f}')

# error = r2_score(y_test,predictions)
# print (f"Youer Error IS :\n {error:.2F}")






















# use this code to make a model help


# condetion = df['Condition'].unique()
# screen = df["Screen Type"].unique()
# print (screen)
# df['Storage'].hist()
# show()
# df['RAM'].hist()
# show()
# brand = df["Brand"].unique()  
# Model = df.groupby('Brand')['Model'].unique()