class Car:
    def __init__(self, brand, speed, motor, color, price):
        self.brand = brand
        self.speed = speed
        self.motor = motor
        self.color = color
        self.price = price

    def describe(self):
        print(f"""
        Značka: {self.brand}, Rychlost: {self.speed}, Objem motoru: {self.motor}, Barva: {self.color}, Cena: {self.price} ")

ford = Car(brend: "ford", speed: "201", motor: "1500", color: "red", price: "700000")
skoda = Car(brend: "skoda", speed: "200", motor: "1000", color: "blue", price: "800000")
fiat = Car(brend: "fiat", speed: "190", motor: "1800", color: "white", price: "600000")""")

