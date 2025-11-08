import pandas as pd
import matplotlib.pyplot as plt

file = "employees.csv"
df = pd.read_csv(file)

print("""
Choose an analysis option:
1. Salary vs Age
2. Salary Distribution (Histogram)
3. Age Distribution
4. Experience Distribution
5. Employees with Salary > 55000
6. IT Department: Experience vs Salary
7. Employees per Department
8. Experience vs Salary
""")

choice = int(input("Enter your choice (1-8): "))

if choice == 1:
    plt.bar(df['Age'], df['Salary'], color='purple')
    plt.title('Salary vs Age')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.grid(True)
    plt.savefig("plot1_salary_vs_age.png")
    plt.show()

elif choice == 2:
    plt.hist(df["Salary"], bins=8, color="skyblue", edgecolor="black")
    plt.title("Salary Distribution of Employees")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")
    plt.savefig("plot2_salary_distribution.png")
    plt.show()

elif choice == 3:
    plt.hist(df["Age"], bins=6)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig("plot3_age_distribution.png")
    plt.show()

elif choice == 4:
    plt.hist(df["Experience"], bins=7)
    plt.title("Experience Distribution")
    plt.xlabel("Years of Experience")
    plt.ylabel("Count")
    plt.savefig("plot4_experience_distribution.png")
    plt.show()

elif choice == 5:
    high = df[df["Salary"] > 55000]
    plt.bar(high["Name"], high["Salary"], color='orange')
    plt.title("Employees with Salary > 55000")
    plt.xticks(rotation=45)
    plt.ylabel("Salary")
    plt.savefig("plot5_high_salary.png", bbox_inches='tight')
    plt.show()

elif choice == 6:
    it = df[df["Department"] == "IT"]
    plt.bar(it["Experience"], it["Salary"], color='green')
    plt.title("IT Department: Experience vs Salary")
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.savefig("plot6_it_experience_salary.png")
    plt.show()

elif choice == 7:
    departments = df["Department"].values
    names = []
    counts = []
    for i in range(len(departments)):
        d = departments[i]
        if d not in names:
            names.append(d)
            c = len(df[df["Department"] == d])
            counts.append(c)

    plt.bar(names, counts, color='cyan')
    plt.title("Employees per Department")
    plt.xlabel("Department")
    plt.ylabel("Count")
    plt.savefig("plot7_employees_per_department.png")
    plt.show()

elif choice == 8:
    x = df["Experience"].values
    y = df["Salary"].values
    plt.bar(x, y, color='red')
    plt.title("Experience vs Salary")
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.savefig("plot8_experience_vs_salary.png")
    plt.show()

else:
    print("Invalid choice!")
