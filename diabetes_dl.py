import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers,callbacks

path='/kaggle/input/diabetes-healthcare-dataset/Diabetes-Data.csv'
data=pd.read_csv(path)

data.columns

data.head()

data.describe()

y=data.Outcome

features=['Pregnancies', 'Glucose', 'BloodPressure', 'BMI','Age']
X=data[features]

early_stopping = callbacks.EarlyStopping(
       min_delta=0.001,
       patience=20,
)

model= keras.Sequential([
    layers.Dense(512,activation='relu',input_shape=[5]),
    layers.Dense(512,activation='relu'),
    layers.Dense(512,activation='relu'),
    layers.Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mae'
)

history=model.fit(
   X,y,batch_size=50,epochs=50
)

print("enter details")
inputdata={}
for feature in features:
     value=float(input(feature))
     inputdata[feature]=[value]
     
df=pd.DataFrame(inputdata)
predictions=model.predict(df)
predictions=predictions*100
print(predictions,"%")