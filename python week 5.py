# Assignment 1: Smartphone class with inheritance and encapsulation

class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand  # Brand of the smartphone
        self.model = model  # Model of the smartphone
        self.__battery_level = battery_level  # Encapsulated battery level

    def call(self, number):
        # Simulate making a call
        print(f"{self.brand} {self.model} is calling {number}.")

    def charge(self, amount):
        # Charge the battery, but not above 100%
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"Battery charged to {self.__battery_level}%.")

    def get_battery_level(self):
        # Getter for the encapsulated battery level
        return self.__battery_level

class Smartwatch(Smartphone):  # Inherits from Smartphone
    def __init__(self, brand, model, battery_level, steps=0):
        super().__init__(brand, model, battery_level)
        self.steps = steps  # Track steps

    def track_steps(self, steps_walked):
        # Add walked steps to total
        self.steps += steps_walked
        print(f"Total steps: {self.steps}")

# Example usage:
phone = Smartphone("Apple", "iPhone 15", 80)
phone.call("123456789")
phone.charge(15)
print(phone.get_battery_level())

watch = Smartwatch("Samsung", "Galaxy Watch", 60)
watch.track_steps(500)
watch.charge(30)


# Superhero base class
class Superhero:
    def __init__(self, name, power, health):
        self.name = name  # Superhero's name
        self.power = power  # Main superpower
        self._health = health  # Encapsulated health attribute

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    def heal(self, amount):
        # Increase health, but not above 100
        self._health = min(100, self._health + amount)
        print(f"{self.name} heals to {self._health} health.")

    def get_health(self):
        # Getter for health
        return self._health

# Inherited class with polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed  # Additional attribute

    def attack(self):
        # Override attack method
        print(f"{self.name} swoops down at {self.flight_speed} mph and attacks with {self.power}!")

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph!")

# Example usage:
hero1 = Superhero("Thunderbolt", "Lightning", 80)
hero1.attack()
hero1.heal(15)
print(hero1.get_health())


# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        # Car-specific move
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        # Plane-specific move
        print("Flying ✈")

class Bicycle(Vehicle):
    def move(self):
        # Bicycle-specific move
        print("Pedaling 🚲")

# Example usage:
vehicles = [Car(), Plane(), Bicycle()]
for v in vehicles:
    v.move()  # Each vehicle moves differently due to polymorphism
