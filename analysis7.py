import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

departments = df["Department"].values
names = []
counts = []

for i in range(len(departments)):
    d = departments[i]
    if d not in names:
        names.append(d)
        c = len(df[df["Department"] == d])
        counts.append(c)

plt.bar(names, counts)
plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.savefig("7.jpg")
