import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
it = df[df["Department"] == "IT"]

plt.bar(it["Experience"], it["Salary"])
plt.title("IT Department: Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.savefig("6.jpg")
