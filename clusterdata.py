import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

cgpa=np.random.uniform(5,10,200)
cgpa=np.round(cgpa,2)

IQ=np.random.uniform(80,100,200)
IQ=np.round(IQ,2)
student = pd.DataFrame({
    'CGPA': cgpa,
    'IQ': IQ
})

student.to_csv('student_data.csv', index=False)
print("Data saved to student_data.csv")


    
    
 
    
   

