class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(
            f"The name of the programmer fo {self.company} is {self.name} and product is {self.product} ")


harry = Programmer("Harry", "Skype")
ali = Programmer("Ali Neaz", "GitHub")
harry.getInfo()
ali.getInfo()
