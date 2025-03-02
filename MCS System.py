import json

class ManagementControlSystem:
    def __init__(self):
        self.employees = []
        self.financials = []

    def add_employee(self, name, department, salary):
        employee = {"name": name, "department": department, "salary": salary}
        self.employees.append(employee)
        print(f"Employee {name} added successfully!")

    def add_financial_record(self, revenue, expenses):
        record = {"revenue": revenue, "expenses": expenses, "profit": revenue - expenses}
        self.financials.append(record)
        print("Financial record added successfully!")

    def generate_report(self):
        print("\n--- Management Control System Report ---\n")
        print("Employees:")
        for emp in self.employees:
            print(f"Name: {emp['name']}, Department: {emp['department']}, Salary: ${emp['salary']}")
            
        
        print("\nFinancial Records:")
        for fin in self.financials:
            print(f"Revenue: ${fin['revenue']}, Expenses: ${fin['expenses']}, Profit: ${fin['profit']}")

    def save_data(self, filename="mcs_data.json"):
        data = {"employees": self.employees, "financials": self.financials}
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Data saved successfully!")

    def load_data(self, filename="mcs_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.employees = data.get("employees", [])
                self.financials = data.get("financials", [])
                print("Data loaded successfully!")
        except FileNotFoundError:
            print("No previous data found.")

if __name__ == "__main__":
    mcs = ManagementControlSystem()
    mcs.load_data()
    while True:
        print("\n1. Add Employee\n2. Add Financial Record\n3. Generate Report\n4. Save & Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            mcs.add_employee(name, department, salary)
        elif choice == "2":
            revenue = float(input("Enter revenue: "))
            expenses = float(input("Enter expenses: "))
            mcs.add_financial_record(revenue, expenses)
        elif choice == "3":
            mcs.generate_report()
        elif choice == "4":
            mcs.save_data()
            break
        else:
            print("Invalid choice. Please try again.")
