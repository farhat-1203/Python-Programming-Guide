from random import randint

class Train:

    def __init__(self, train_no, total_seats):
        self.train_no = train_no
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_ticket(self, fro, to):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print(f"Your train is booked from {fro} to {to} in train number {self.train_no}.")
        else:
            print("Sorry, no seats available.")

    def get_status(self):
        available_seats = self.total_seats - self.booked_seats
        print(f"The train number {self.train_no} has {available_seats} seats available.")

    def get_fare(self, fro, to):
        fare = randint(2222, 10000)
        print(f"Your ticket fare for your train from {fro} to {to} is {fare}.")


t = Train(21627, 10)
t.book_ticket("Mumbai", "Delhi")
t.get_status()
t.get_fare("Mumbai", "Delhi")
