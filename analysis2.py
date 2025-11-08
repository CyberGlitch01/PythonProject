import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

# Plot histogram of Salary
plt.hist(df["Salary"], bins=8, color="skyblue", edgecolor="black")
plt.title("Salary Distribution of Employees")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.savefig("2.jpg")
