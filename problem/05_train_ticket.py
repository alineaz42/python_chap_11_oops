

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the Train is {self.name} ")
        print(f"The fare of the Train is Tk.{self.fare} ")
        print(f"The seats availabe of the Train is {self.seats} ")

    def fareInfo(self):
        print(f"The price of the ticket if Tk.{self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(
                f"Your ticket has been booked. Your seat number is {self.seats} ")
            self.seats = self.seats-1
            print(f" {self.seats} availabe ")
        else:
            print(f"Sorry No more seats availabe ")

        # def cancelTicket(self, seatNumb): #need to work in this one


intercity = Train("Intercity Express: 1024", 90, 10)
intercity.fareInfo()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
