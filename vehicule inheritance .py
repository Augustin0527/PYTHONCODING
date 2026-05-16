class bus:
    def __init__(self,length,maxspeed,price,):
        self.length = length
        self.maxspeed = maxspeed
        self.price = price
    def display_info(self):
        print(f"length:{self.emp_id}")
        print(f"maxspeed:{self.maxspeed}")
        print(f"price:{self.price}euro")

class car_suv:
    def __init__(self,lenght,maxspeed,price,seats,):
       super().__init__(self,lenght,maxspeed,price)
       self.seats = seats
    def display_info(self):
       super().display_info()
       print(f"seats:{self.seats}")

class plane:
     def __init__(self,lenght,maxspeed,price,seats,selling_rate,):    
        super().__init__(self,lenght,maxspeed,price,seats)
        self.selling_rate = selling_rate
     def display_info(self):
        super().display_info()
        print(f"selling_rate :{self.selling_rate}")

employees = [
bus("10m", "100km/h", "100 000 $"),
car_suv("4m","250km/h","20 000-70 000$","5"),
plane("40m","km/h","1b-20b" ,"over 100"," 5 sales per year"),
]     
print ("======= vehicule management system ======== \n")
for employee in employees :
    employee.display_info()
    print("-" * 30) 