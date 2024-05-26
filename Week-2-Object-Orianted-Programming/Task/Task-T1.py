class Vehicle:
    def __init__(self,sc):
        self.sc = sc
    
    def standardFare(self):
        return self.sc * 100
    
class Bus(Vehicle):
    def __init__(self, sc):
        super().__init__(sc)
    
    def standardFare(self):
        stdFare = super().standardFare()
        mantCharge = stdFare * 0.1
        ultmAmount = stdFare + mantCharge
        return ultmAmount

if __name__ == "__main__":
    sc = int(input("Enter Seating capacity: "))
    bus = Bus(sc)
    print(f"Ultimate fare for the bus ride: ${bus.standardFare():.2f}\n")