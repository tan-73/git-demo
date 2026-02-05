'''
2. A college has collected data on student academic performance to analyze trends and patterns using
data visualization techniques.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Student_ID" : ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"],
    "Department" : ["CSE", "ME", "ECE", "AIML", "EEE", "ME", "ISE", "ECE"],
    "Attendance" : [85, 92, 70, 98, 90, 88, 92, 80],
    "IA_Marks" : [78, 98, 88, 76, 94, 90, 88, 83]    
}

df = pd.DataFrame(data)

'''
a) Write a Python program to create a bar chart showing the average internal marks department-wise.
'''
avg_marks = df.groupby("Department")["IA_Marks"].mean()

avg_marks.plot(kind = "bar")
plt.xlabel("Department")
plt.ylabel("Average Internal Marks")
plt.title("Average internal marks by department")
plt.show()

'''
b) Create a scatter plot to visualize the relationship between attendance percentage and internal marks
'''
plt.scatter(df["Attendance"], df["IA_Marks"])
plt.xlabel("Attendance (%)")
plt.ylabel("Internal Marks")
plt.title("Attendance vs Internal Marks")
plt.show()

'''
c) Draw a box plot for Internal_Marks to identify spread and outliers, and briefly comment on the distribution.
'''
plt.boxplot(df["IA_Marks"])
plt.ylabel("Internal Marks")
plt.title("Box plot of internal marks")
plt.show()

'''
d) Write a Python program to create a heatmap showing student performance across subjects
'''
marks_data = df.pivot_table (
    index = "Student_ID", 
    values = "IA_Marks", 
    aggfunc = "mean"
)

sns.heatmap(marks_data, annot = True, cmap = "coolwarm")
plt.title("Heatmap of students attendance and internal marks")
plt.show()