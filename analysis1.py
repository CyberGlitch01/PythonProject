import pandas as pd
import matplotlib.pyplot as plt

file = "employees.csv"

df = pd.read_csv(file)

plt.bar(df['Age'], df['Salary'], color='purple')
plt.title('Salary vs Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.savefig("1.jpg")
