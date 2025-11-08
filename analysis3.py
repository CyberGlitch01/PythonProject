import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
plt.hist(df["Age"], bins=6)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
plt.savefig("3.jpg")
