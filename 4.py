import pandas as pd
data = {
"Offer": [1,0,1,0,1,0],
"Link": [1,1,1,0,0,1],
"Attachment": [0,0,1,0,0,1],
"Spam": [1,0,1,0,1,0]
}
df = pd.DataFrame(data)
print(df)


import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Create the dataset
data = {
    'Contains_Offer': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'Contains_Link': ['Yes', 'No', 'No', 'Yes', 'No', 'No'],
    'Contains_Attachment': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No'],
    'Is_Spam': ['Spam', 'Not Spam', 'Spam', 'Not Spam', 'Spam', 'Not Spam']
}
df = pd.DataFrame(data)
# Initialize LabelEncoder
le = LabelEncoder()
# Encode categorical variables into numerica
df_encoded = df.copy()
for col in ['Contains_Offer', 'Contains_Link', 'Contains_Attachment', 
'Is_Spam']:
    df_encoded[col] = le.fit_transform(df[col])
# Display encoded data (Yes=1, No=0 | Spam=1, Not Spam=0)
print(df_encoded)

from sklearn.naive_bayes import BernoulliNB
import numpy as np
# Features (X) and Target (y)
X = df_encoded[['Contains_Offer', 'Contains_Link', 
'Contains_Attachment']]
y = df_encoded['Is_Spam']
# Initialize and train the model (BernoulliNB for binary data)
model = BernoulliNB()
model.fit(X, y)
print("Model trained successfully.")

new_email = [[1, 0, 1]]
prediction = model.predict(new_email)
result = "Spam" if prediction[0] == 1 else "Not Spam"
print(f"Predicted Class: {result}")

accuracy = model.score(X, y)
print(f"Accuracy: {accuracy * 100:.2f}%")
