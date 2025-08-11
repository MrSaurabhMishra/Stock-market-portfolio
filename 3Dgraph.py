
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
price=np.random.randint(100, 1000, size=30)
quantity=np.random.randint(1, 20, size=30)
amount=price*quantity
data= pd.DataFrame(data=np.array([price, quantity, amount]).T,columns=['price', 'quantity', 'amount'])
fig = plt.figure(figsize=(8,6))
ax=fig.add_subplot(111, projection='3d')
ax.scatter(data['price'], data['quantity'], data['amount'],)
ax.set_xlabel('Price')
ax.set_ylabel('Quantity')
ax.set_zlabel('Amount')
plt.show()




