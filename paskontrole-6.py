class Auto:
    regNo = "Nav norādīts"
    manufacturer = "Nav norādīts"
    model = "Nav norādīts"
    year = 0
    odo = 0

    # __init__ pieprasam VIN lai būtu str tipa
    def __init__(self, VIN: str):
        self.VIN = VIN

    # __str__ izvadam atpakaļ informāciju izmantojot formatētu string. Lai būtu smuki pa līnijām izmantoju '\n' kas pārliek uz nākamo rindu.
    def __str__(self):
        return f"Reģistrācijas numurs: {self.regNo}\nVIN numurs: {self.VIN}\nRažotājs: {self.manufacturer}\nModelis: {self.model}\nGads: {self.year}\nOdometra rādījums: {self.odo}"
    
    # Visas pārējās metodes man liekas ir pašizskaidrojošas.
    def regNo_maina(self, regNo: str):
        self.regNo = regNo

    def VIN_maina(self, VIN: str):
        self.VIN = VIN

    def manufacturer_maina(self, manufacturer: str):
        self.manufacturer = manufacturer

    def model_maina(self, model: str):
        self.model = model

    def year_maina(self, year: int):
        self.year = year

    def odo_maina(self, odo: int):
        self.odo = odo

    def parrakstisana(self, regNo: str, VIN: str, manufacturer: str, model: str, year: int, odo: int):
        self.regNo = regNo
        self.VIN = VIN
        self.manufacturer = manufacturer    
        self.model = model
        self.year = year
        self.odo = odo

    def odo_plus(self, added_odo: int):
        self.odo += added_odo

# Initializējam objektu ar VIN nr un izprintējam visu objektu
auto = Auto("KG-05112003")
print(auto)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

# Manuprāt tālāk viss ir pašizskaidrojošs, nav nekas sarežģīts.

print(auto.regNo)
print(">>>>")
auto.regNo_maina("12345")
print(auto.regNo)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

print(auto.VIN)
print(">>>>")
auto.VIN_maina("05112003-KG")
print(auto.VIN)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

print(auto.manufacturer)
print(">>>>")
auto.manufacturer_maina("BMW")
print(auto.manufacturer)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

print(auto.model)
print(">>>>")
auto.model_maina("E36 Skyline")
print(auto.model)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

print(auto.year)
print(">>>>")
auto.year_maina(2005)
print(auto.year)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

print(auto.odo)
print(">>>>")
auto.odo_maina(231687)
print(auto.odo)
print(">>>>")
auto.odo_plus(313)
print(auto.odo)

print("---- Atstarpe ----") # Atstarpe, lai konsolē būtu vieglāk visu apskatīt

print(auto)
print(">>>>")
auto.parrakstisana(regNo="54321", VIN="051-KG-103", manufacturer="Audi", model="Dievs vien zin", year=2010, odo=142698)
print(auto)