import pandas as pd

file = "employees.csv"

print("========== EMPLOYEE MANAGER ==========")

while True:
    print("\nMENU:")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by ID")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    df = pd.read_csv(file)

    if choice == '1':
        print("\n=== Add Employee ===")
        empid = input("Enter Employee ID: ")

        if empid not in df["EmpID"].values:
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            desig = input("Enter Designation: ")
            salary = float(input("Enter Salary: "))
            age = int(input("Enter Age: "))
            exp = int(input("Enter Experience (in years): "))
            df.loc[len(df)] = [empid, name, dept, desig, salary, age, exp]
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
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
