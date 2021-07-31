class Employee:
    company = "Google"  # class attribute
    salary = "35k"


# instance attribute will print though having class attribute
# other wise will print class attribut
# else will throw error
harry = Employee()
rajni = Employee()
harry.salary = "30k"
rajni.salary = "32k"

print(harry.company)
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
# instance attribute

print(harry.salary)
print(rajni.salary)
