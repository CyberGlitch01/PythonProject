import pandas as pd
import os

file = "employees.csv"

if not os.path.exists(file):
    df = pd.DataFrame(columns=["EmpID", "Name", "Department", "Designation", "Salary", "Age", "Experience"])
    df.to_csv(file, index=False)

print("========== EMPLOYEE MANAGER ==========")

while True:
    print("\nMENU:")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Show Data Analysis")
    print("7. Open Graphical Analysis")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    df = pd.read_csv(file)

    if choice == '1':
        print("\n=== Add Employee ===")
        empid = input("Enter Employee ID: ")

        if not empid in df["EmpID"].values:
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            desig = input("Enter Designation: ")
            salary = float(input("Enter Salary: "))
            age = int(input("Enter Age: "))
            exp = int(input("Enter Experience (in years): "))
            next_index = len(df)
            df.loc[next_index] = [empid, name, dept, desig, salary, age, exp]
            df.to_csv(file, index=False)
            print("Employee added successfully!")
            print("\nRecently Added Record:")
            print(df.iloc[-1])
        else:
            print("Employee already exists, please choose another Employee ID.")

    elif choice == '2':
        print("\n=== All Employees ===")
        print(df)

    elif choice == '3':
        print("\n=== Search Employee ===")
        empid = input("Enter Employee ID to search: ")
        emp = df[df['EmpID'] == empid]
        if not emp.empty:
            print(emp)
        else:
            print("Employee not found!")

    elif choice == '4':
        print("\n=== Update Employee Salary ===")
        empid = input("Enter Employee ID: ")

        if empid in df['EmpID'].values:
            new_salary = float(input("Enter new salary: "))
            index = df[df['EmpID'] == empid].index[0]
            df.at[index, 'Salary'] = new_salary
            df.to_csv(file, index=False)
            print("Salary updated successfully!")
        else:
            print("Employee not found!")

    elif choice == '5':
        print("\n=== Delete Employee ===")
        empid = input("Enter Employee ID to delete: ")

        if empid in df['EmpID'].values:
            index_to_drop = df[df['EmpID'] == empid].index
            df = df.drop(index_to_drop)
            df.to_csv(file, index=False)
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")

    elif choice == '6':
        print("\n=== Data Analysis ===")
        print("Total Employees:", len(df))
        print("Average Salary:", df['Salary'].mean())
        print("Highest Salary:", df['Salary'].max())
        print("Lowest Salary:", df['Salary'].min())
        print("\nDepartment-wise Employee Count:")
        print(df['Department'].value_counts())
        print("\nAverage Salary by Department:")
        print(df.groupby('Department')['Salary'].mean())

    elif choice == '7':
        print("\nOpening Graphical Analysis...")
        os.system("python analysis.py")

    elif choice == '8':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
