class Car:
    def __init__(self, make, model, year, color, speed):
        self. make = make
        self.model = model
        self.year = year
        self. color = color
        self.speed = 0
        
    def get_speed(self):
        return self.speed
    
    def accelerate(self):
        while True:
            speed_increase = input("Enter an amount of speed to increase or 'Q' to quit")
            if speed_increase == "Q":
                break 
            if speed_increase == speed_increase < 0:
                raise ValueError("Speed increase must be above 0")
            self.speed += speed_increase
        
    
    def brake(self, speed_decrease):
        self.speed -= speed_decrease
        if speed_decrease < 0:
            raise ValueError("The amount of speed decreased can't result in less than 0")
        # ensure that the speed of the vehicle doesnt go below 0
        self.speed = max(0, self.speed - speed_decrease)
        
    # return a string that contains the vehicle info    
    def get_info(self):
        return f"The color of this vehicle is {self.color}, the year is {self.year}, the make is {self.make}, the model is {self.model}, and the current speed is {self.speed} mph."
    


    
    
    
    
        
        
        
        