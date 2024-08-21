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

model=RandomForestRegressor(random_state=1)

model.fit(X,y)

prediction=model.predict(X)
print(mean_absolute_error(prediction,y))

print("enter details")
inputdata={}
for feature in features:
     value=float(input(feature))
     inputdata[feature]=[value]
     
df=pd.DataFrame(inputdata)
predictions=model.predict(df)
predictions=predictions*100
print(predictions,"%")