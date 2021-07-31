class Employee:
    company = "Google"
    salary = "40k"


harry = Employee()
rajni = Employee()
print(harry.salary)  # 40k from class attr
print(rajni.salary)  # 40k from class attr

harry.salary = "45k"
rajni.salary = "50k"
print(harry.salary)  # 45k from instance attr
print(rajni.salary)  # 50k from instance attr


harry.name = "Harry"
rajni.name = "Rajni"
print(harry.name)

# if attr does not present in instance or class will throw error always
