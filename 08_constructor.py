class Employee:
    company = "Google"

    # constructor automatically is called like react js
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of the employee is  {self.name} ")
        print(f"The salary of the employee is  {self.salary} ")
        print(f"The subunit of the employee is  {self.subunit} ")

    def getSalary(self, thank):
        print(
            f"Salary of this employee working in  {self.company} is {self.salary} \n {thank} ")

    @staticmethod  # no need to pass self in staticmethod
    def greet():
        print("Good Morning sir")

    @staticmethod
    def time():
        print("the time is 9am")


harry = Employee("Harry", 100, "YouTube")
# harry = Employee()  # --> will throw error
harry.getDetails()
