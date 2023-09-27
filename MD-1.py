import math # Ņēmu klāt math bibliotēku, jo tur ir kvadrātsaknes funkcija

# Pieņemam ievadītos skaitļus un uzreiz pārvēršam tos par float, jo tad pieņems gan int, gan float bez problēmām.
# Ja int ir pārtaisīts par float neko nemaina aprēķinos.
a = float(input("Ievadiet a: "))
b = float(input("Ievadiet b: "))
c = float(input("Ievadiet c: "))

# Pārbaudam vai a ir 0
if a == 0:
    print("Kvadrātvienādojumā a nedrīkst būt 0")
    exit()

# Parādam vienādojumu izmantojot unicode simbolus priekš superscripta
print(f"Vienādojums: {a}x\u00b2+{b}x+{c}=0")

# Aprēķinam diskriminantu
diskriminants = b**2-4*a*c

print(f"Diskriminants: {diskriminants}")

# Pārbaudām diskriminantu
if diskriminants < 0:
    print("Diskriminants ir negatīvs, vienādojumam nav atrisinājuma.")
    exit()

elif diskriminants == 0:
    print("Diskriminants ir 0, ir divas vienādas saknes.")

    # Cenšamies aprēķināt saknes, ja neizdodas tas tiek paziņots un darbību pārtraucam
    try:
        # Izmantoju bibliotēkas math kvadrātsaknes funkciju
        x1 = -b+math.sqrt(diskriminants)/2*a
        x2 = -b-math.sqrt(diskriminants)/2*a
    except:
        print("Neizdevās aprēķināt saknes...")
        exit()

    print(f"Tās saknes ir x\u2081: {x1} un x\u2082: {x2}")

elif diskriminants > 0:
    print("Diskriminants ir lielāks par 0, vienādojumam ir divas dažādas saknes.")

    # Cenšamies aprēķināt saknes, ja neizdodas tas tiek paziņots un darbību pārtraucam
    try:
        # Izmantoju bibliotēkas math kvadrātsaknes funkciju
        x1 = -b+math.sqrt(diskriminants)/2*a
        x2 = -b-math.sqrt(diskriminants)/2*a
    except:
        print("Neizdevās aprēķināt saknes...")
        exit()

    # Parādu aprēķinātās saknes, protams izmantoju arī unicode simbolus priekš subscripta
    print(f"Tās saknes ir x\u2081: {x1} un x\u2082: {x2}")