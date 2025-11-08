import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

x = df["Experience"].values
y = df["Salary"].values

plt.bar(x, y)
plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.savefig("8.jpg")
