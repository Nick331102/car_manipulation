class Car:
    def __init__(self, make, model, year, color, speed):
        self. make = make
        self.model = model
        self.year = year
        self. color = color
        self.speed = speed
        
    def accelerate_brake(self):
           while True:
            action = input("Enter 'A' to accelerate or 'B' to brake: ")
            if action.upper() == "A":
                speed_increase = input("Enter an amount of speed to increase: ")
                speed_increase = int(speed_increase)
                if speed_increase < 0:
                    raise ValueError("Speed increase must be above 0")
                self.speed += speed_increase
                print(f" The speed of your vehicle is now {self.speed} mph.")
            elif action.upper() == "B":
                speed_decrease = input("Enter an amount of speed to decrease: ")
                speed_decrease = int(speed_decrease)
                if speed_decrease < 0:
                    raise ValueError("Speed decrease must be above 0")
                self.speed = max(0, self.speed - speed_decrease)
                print(f" The speed of your vehicle is now {self.speed} mph.")
            else:
                break
            return
        
    def brake(self, speed_decrease):
        if speed_decrease < 0:
            raise ValueError("The speed of the vehicle cannot be less than 0")
        speed_decrease = int(speed_decrease) 
        self.speed = max(0, self.speed - speed_decrease)
            
    # return a string that contains the vehicle info    
    def get_info(self):
        return f"The color of this vehicle is {self.color}, the year is {self.year}, the make is {self.make}, the model is {self.model}, and the current speed is {self.speed} mph."
    
my_car = Car('Honda', "Pilot", 2023, "White", 25)

my_car.accelerate_brake()

car_info = my_car.get_info()
print(car_info)

    
    
    
    
        
        
        
        