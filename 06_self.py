class Employee:
    company = "Google"

    def getSalary(self):
        print(
            f"Salary of this employee working in {self.company} is {self.salary} ")


harry = Employee()
harry.salary = "10K"
# harry.setSalary()
Employee.getSalary(harry)

# jscript has this and bactic leterals
# python has self f string
