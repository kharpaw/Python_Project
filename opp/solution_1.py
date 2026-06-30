class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car+=1
    
    def get_brand(self):
        return self.__brand + " !" 
        
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or desel"
    
    @staticmethod
    def general_des():
        return "Cars are means of transport"
    
    @property
    def get_mode(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric"
        
       
# my_Tesla = ElectricCar("Tesla", "ModelX", "89kw")
# print(isinstance(my_Tesla, ElectricCar))











# print(my_Tesla.fuel_type())

# my_car = Car("Toyata", "Safari")
# print(Car.general_des())
    
    
    
# my_car = Car("Toyata", "corolla")
# print(my_car.model)
# print(my_car.fullname())


# my_new_car = Car("Toyata", "Safari")
# print(my_car.brand)
# print(my_car.model)


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

new_tesla = ElectricCar("Tesla", "Model S")
print(new_tesla.engine_info())