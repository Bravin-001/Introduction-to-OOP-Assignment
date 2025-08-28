# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
        self.__secret_identity = "Unknown"  # Encapsulated attribute

    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__secret_identity}"

    def set_identity(self, identity):
        self.__secret_identity = identity

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!"

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.gadgets = gadgets

    def use_power(self):
        return f"{self.name} deploys {', '.join(self.gadgets)} to unleash {self.power}!"

# Example usage
hero1 = FlyingHero("Skyblade", "Wind Manipulation", "Cloud City", 800)
hero2 = TechHero("Circuit", "Electromagnetic Pulse", "Neo Tokyo", ["EMP Blaster", "Drone Swarm"])

hero1.set_identity("Ava Storm")
hero2.set_identity("Kenji Tanaka")

print(hero1.use_power())
print(hero1.reveal_identity())
print(hero2.use_power())
print(hero2.reveal_identity())