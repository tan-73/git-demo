import pandas as pd
import matplotlib.pyplot as plt

data = {
"Math": [78,65,88,55,92,70],
"Physics": [72,60,85,58,90,68],
"Chemistry": [75,62,82,60,88,72],
"Programming": [85,70,90,65,95,75],
"Aptitude": [80,68,86,62,90,74]
}
students = ["S1","S2","S3","S4","S5","S6"]
df = pd.DataFrame(data, index=students)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

plt.scatter(pca_data[:,0], pca_data[:,1])
for i in range(len(students)):
    plt.text(pca_data[i,0], pca_data[i,1], students[i])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA Scatter Plot of Students")
plt.show()

df['PC1'] = pca_data[:, 0]
df['PC2'] = pca_data[:, 1]

low_performers = df.sort_values(by = 'PC1', ascending=True)

low_performers

