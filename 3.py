'''
3. Using the given dataset, apply Linear Regression to predict a student’s Internal Marks based on 
Study Hours and Attendance. Apply Logistic Regression to classify whether a student will be placed
'''
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Study_Hours": [2,4,6,8,10,5,7,9],
    "Attendance": [65,70,75,80,90,72,78,85],
    "Internal_Marks": [45,55,65,78,90,60,70,85],
    "Placed": [0,0,1,1,1,0,1,1]
}
df = pd.DataFrame(data)

'''
a) Write a Python program to load the dataset and visualize the relationship between:
- Study Hours vs Internal Marks
'''
plt.scatter(df["Study_Hours"], df["Internal_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Internal Marks")
plt.show()

'''
- Attendance vs Internal Marks
'''
plt.scatter(df["Attendance"], df["Internal_Marks"])
plt.xlabel("Attendance %")
plt.ylabel("Internal Marks")
plt.show()

'''
b) Build a Multiple Linear Regression model using Python to predict Internal_Marks. Predict the internal
marks of a student who studies 7 hours with 80% attendance. Evaluate the model using Mean Squared
Error (MSE) and briefly interpret the result. 
'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = df[["Study_Hours", "Attendance"]]
y = df["Internal_Marks"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[7, 80]])
print("Predicted internal marks : ", prediction)

mse = mean_squared_error(y, model.predict(X))
print("MSE : ", mse)

'''
Perform data preprocessing and visualize the relationship between Internal Marks and Placement status
using a suitable plot.
'''
plt.boxplot([df[df["Placed"] == 0]["Internal_Marks"], 
            df[df["Placed"] == 1]["Internal_Marks"]], 
           labels = ["Not Placed", "Placed"])
plt.ylabel("Internal Marks")
plt.show()