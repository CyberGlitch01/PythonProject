import pandas as pd
import matplotlib.pyplot as plt
import os

file = "employees.csv"

if not os.path.exists(file):
    df = pd.DataFrame(columns=[
        "EmpID", "Name", "Department", "Designation",
        "Salary", "Age", "Experience"
    ])
    df.to_csv(file, index=False)

df = pd.read_csv(file)

while True:
    print("\n========== GRAPHICAL EMPLOYEE ANALYSIS ==========")
    print("1. Department-wise Employee Count (Bar Graph)")
    print("2. Average Salary by Department (Bar Graph)")
    print("3. Salary vs Experience (Bar Graph)")
    print("4. Department-wise Employee Percentage (Pie Chart)")
    print("5. Exit")
    print("6. Total Salary Expenditure by Department (Bar Graph)")
    print("8. Salary to Experience Ratio (Line Chart)")
    print("9. Salary vs Age (Bar Graph)")

    plt.clf()
    choice = input("\nEnter your choice (1-9): ")

    if choice == '1':
        dept_count = df['Department'].value_counts()
        dept_count.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Department-wise Employee Count')
        plt.xlabel('Department')
        plt.ylabel('Number of Employees')
        plt.show()

    elif choice == '2':
        avg_salary = df.groupby('Department')['Salary'].mean()
        avg_salary.plot(kind='bar', color='lightgreen', edgecolor='black')
        plt.title('Average Salary by Department')
        plt.xlabel('Department')
        plt.ylabel('Average Salary')
        plt.show()

    elif choice == '3':
        df.plot(kind='bar', x='Experience', y='Salary', color='lightblue', edgecolor='black')
        plt.title('Salary by Experience')
        plt.xlabel('Experience (Years)')
        plt.ylabel('Salary')
        plt.show()

    elif choice == '4':
        dept_count = df['Department'].value_counts()
        dept_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True)
        plt.title('Department-wise Employee Percentage')
        plt.ylabel('')
        plt.show()

    elif choice == '5':
        print("Exiting program...")
        break

    elif choice == '6':
        total_salary = df.groupby('Department')['Salary'].sum()
        total_salary.plot(kind='bar', color='orange', edgecolor='black')
        plt.title('Total Salary Expenditure by Department')
        plt.xlabel('Department')
        plt.ylabel('Total Salary')
        plt.tight_layout()
        plt.show()

    elif choice == '8':
        ratio_df = df.groupby('Experience')['Salary'].mean()
        plt.plot(ratio_df.index, ratio_df.values, marker='o', linestyle='-', color='purple')
        plt.title('Salary to Experience Ratio')
        plt.xlabel('Experience (Years)')
        plt.ylabel('Average Salary')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif choice == '9':
        df.plot(kind='bar', x='Age', y='Salary', color='salmon', edgecolor='black')
        plt.title('Salary by Age')
        plt.xlabel('Age')
        plt.ylabel('Salary')
        plt.show()

    else:
        print("Invalid choice! Please enter a valid option (1-9).")
