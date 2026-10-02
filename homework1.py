import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
df = pd.read_csv('iris_data.csv')
 
c = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
 
plt.figure(figsize=(15, 8))
 
n = 1
for i in range(len(c)):
    for j in range(i + 1, len(c)):
        x_name = c[i]
        y_name = c[j]
        
        x = df[x_name]
        y = df[y_name]
        
        plt.subplot(2, 3, n)
        plt.scatter(x, y)
        
        p = np.polyfit(x, y, 1)
        k = p[0]
        b = p[1]
        
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = k * x_line + b
        
        plt.plot(x_line, y_line, color='red')
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(f"{x_name} vs {y_name}")
        plt.grid()
        
        print(x_name, "vs", y_name)
        print("k =", k)
        print("b =", b)
        print()
        
        n += 1
 
plt.tight_layout()
plt.show()