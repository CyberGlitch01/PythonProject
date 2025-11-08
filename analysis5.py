import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
high = df[df["Salary"] > 55000]

plt.bar(high["Name"], high["Salary"])
plt.title("Employees with Salary > 55000")
plt.xticks(rotation=45)
plt.ylabel("Salary")
plt.savefig("5.jpg")
