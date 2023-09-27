masivs = [['John', 'Doe', 11, 1.80, 'M'],['Mark', 'Gate', 24, 1.65, 'M'],['Tom', 'Xin', 18, 1.90, 'M'],['Sarah', 'Blake', 14, 2.00, 'F'],['Otto', 'Ming', 19, 1.95, 'M'],['Lee', 'Gato', 20, 1.88, 'M'],['Kate', 'Cote', 21, 1.60, 'F'],['Marta', 'Bell', 16, 1.78, 'F'],['Alice', 'York', 15, 1.65, 'F'],['Colm', 'Pete', 25, 1.99, 'M']]

# Iegūstam cik ierakstus izvadīt, ja vispār ieraksta
cik_izvadit = input("Cik ierakstus izvadīt?(Atstāj tukšu, ja visu): ")

# Izmantojot ļoti īsu pierakstu pārbaudam vai kaut kas tika ievadīts, ja jā tad pārveidojam to uz int, ja nē tad liekam -1
if cik_izvadit == "": cik_izvadit = -1
else: cik_izvadit = int(cik_izvadit)

# Izprintējam kolonnu nosaukumus izmantojot '\t' starp vārdiem, jo tas ievieto 'tab' atstarpi
print("N.p.k.\tVārds\tUzvārds\tVecums\tAugums\tDzimums")

if cik_izvadit > len(masivs) or cik_izvadit == -1:
    npk = 0 # Sākam ar 0, lai ciklā viegli pievienotu pa vienam.
    for persona in masivs:
        npk += 1

        # Pieliekam katram mainīgajam savu vērtību izmantojot zināmus saraksta indeksus
        vards = persona[0]
        uzvards = persona[1]
        vecums = persona[2]
        augums = persona[3]
        dzimums = persona[4]

        # Izprintējam personas rindiņu atkal izmantojot '\t'
        print(f"{npk}\t{vards}\t{uzvards}\t{vecums}\t{augums}\t{dzimums}")

else:
    # Veicam in range ciklu, pieliekam cik_izvadit klāt viens, jo in range neizpilda pēdējo ciklu
    for npk in range(1, cik_izvadit+1, 1):
        # Atņemam vienu no npk, jo indeks sākas ar 0 masīvos
        persona = masivs[npk-1]

        # Pieliekam katram mainīgajam savu vērtību izmantojot zināmus saraksta indeksus
        vards = persona[0]
        uzvards = persona[1]
        vecums = persona[2]
        augums = persona[3]
        dzimums = persona[4]

        # Izprintējam personas rindiņu atkal izmantojot '\t'
        print(f"{npk}\t{vards}\t{uzvards}\t{vecums}\t{augums}\t{dzimums}")