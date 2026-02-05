'''
1. Write a Python program to compute the following descriptive statistics for both Study_Hours and
Exam_Score:
Mean
Median
Standard Deviation
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

study_hours = [2, 4, 6, 8, 10, 12]
exam_scores = [45, 55, 65, 75, 85, 95]

print("Study hours : ")
print("Mean : ", np.mean(study_hours))
print("Median : ", np.median(study_hours))
print("Standard deviation : ", np.std(study_hours))

print("Exam scores : ")
print("Mean : ", np.mean(exam_scores))
print("Median : ", np.median(exam_scores))
print("Standard deviation : ", np.std(exam_scores))

'''
a) Assume that the Exam_Score follows a normal distribution. Write a Python program to calculate the
probability that a randomly selected student scores more than 75 marks
'''
mean = np.mean(exam_scores)
std = np.std(exam_scores)

probability = 1 - norm.cdf(75, mean, std)
print(f"Probability of scoring more than 75 : {probability}")


'''
b) Plot a histogram for Exam_Score and interpret whether the distribution appears normal or skewed
'''
plt.hist(exam_scores, bins = 5)
plt.xlabel("Exam score")
plt.ylabel("Number of students")
plt.title("Histogram of exam scores")
plt.show()