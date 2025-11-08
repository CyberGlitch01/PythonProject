import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")
plt.hist(df["Experience"], bins=7)
plt.title("Experience Distribution")
plt.xlabel("Years of Experience")
plt.ylabel("Count")
plt.savefig("4.jpg")
