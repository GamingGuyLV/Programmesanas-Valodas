pi = 3 # Kā jau teikts nosacījumos, pieņemam, ka Pi ir 3

# Riņķa laukuma funkcija, kas pieņem tikai INT vai FLOAT tipa mainīgos un uzreiz atgriež līdz 2 decimāldaļām noīsinātu laukumu
def rinkaLaukums(radiuss: int | float):
    return round(pi*radiuss**2, 2)

# Cilindra tilpuma funkcija, kas pieņem divus INT vai FLOAT tipa mainīgos un uzreiz atgriež līdz 2 decimāldaļām noīsinātu tilpumu
def cilindraTilpums(laukums: int | float, augstums: int | float):
    return round(laukums * augstums, 2)

# Iegūstam radiusu un augstumu
cilindra_radiuss = input("Ievadiet cilindra pamatnes radiusu: ")
cilindra_augstums = input("Ievadiet cilindra augstumu: ")

# Pārbaudam vai punkts nav ielikts, kas nozīmētu, ka tas ir decimālskaitlis
try:
    if "." in cilindra_radiuss:
        cilindra_radiuss = float(cilindra_radiuss)
    else:
        cilindra_radiuss = int(cilindra_radiuss)

    
    if "." in cilindra_augstums:
        cilindra_augstums = float(cilindra_augstums)
    else:
        cilindra_augstums = int(cilindra_augstums)

except ValueError as error: # Ja ir kāda kļūda pārveidojot, tad izmetam kļūdu un pārtraucam programmas darbību.
    print(f"Kaut kas nebija pareizi, kļūda: {error}")
    exit()

# Izsaucam funkcijas un uzreiz ieliekam rezultātu mainīgajos, lai gan izmantojot "format string" būtu varējis izsaukt tās funkcijas no tā. Komentārā pašā apakšā ir ielikts kā tas izskatītos.
cilindra_pamatnes_laukums = rinkaLaukums(cilindra_radiuss)
cilindra_tilpums = cilindraTilpums(cilindra_pamatnes_laukums, cilindra_augstums)


print(f"Ievadītie dati: radiuss = {cilindra_radiuss}, augstums = {cilindra_augstums}")
print(f"Cilindra pamatnes riņķa laukums: {cilindra_pamatnes_laukums}")
print(f"Cilindra tilpums: {cilindra_tilpums}")


"""
print(f"Ievadītie dati: radiuss = {cilindra_radiuss}, augstums = {cilindra_augstums}")
print(f"Cilindra pamatnes riņķa laukums: {rinkaLaukums(cilindra_radiuss)}")
print(f"Cilindra tilpums: {cilindraTilpums(cilindra_pamatnes_laukums, cilindra_augstums)}")
"""