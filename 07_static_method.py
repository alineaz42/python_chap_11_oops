class Employee:
    company = "Google"

    def getSalary(self, thank):
        print(
            f"Salary of this employee working in {self.company} is {self.salary} \n {thank} ")

    # def greeting(self):
    #     print("Good Morning sir")

    @staticmethod  # no need to pass self in staticmethod
    def greet():
        print("Good Morning sir")

    @staticmethod
    def time():
        print("the time is 9am")


harry = Employee()
harry.salary = "10K"
harry.greet()
harry.getSalary("Thanks")
Employee.greet()
Employee.time()
