skaitlu_saraksts = []

# Cikls 10 ciparu ievadei, ejam līdz 11, jo pēdējo ciklu pitons neveic
for skaitlis in range(1, 11, 1):
    ievades_skaitlis = input(f"Ievadiet {skaitlis}. skaitli: ")

    # Pārbaudam vai punkts nav ielikts, kas nozīmētu, ka tas ir decimālskaitlis
    try:
        if "." in ievades_skaitlis:
            ievades_skaitlis = float(ievades_skaitlis)
        else:
            ievades_skaitlis = int(ievades_skaitlis)

    except ValueError as error: # Ja ir kāda kļūda pārveidojot, tad izmetam kļūdu un pārtraucam programmas darbību.
        print(f"Kaut kas nebija pareizi, kļūda: {error}")
        exit()

    # Pievienojam skaitli sarakstam
    skaitlu_saraksts.append(ievades_skaitlis)

# Parādam opcijas
print("Izvēlaties opciju:")
print("1 - Summa")
print("2 - Starpība")
print("3 - Reizinājums")

# Uzreiz pārveidojam izvēli par int
operacija = int(input())

# Lai nevajadzētu izmantot vairākus IF/ELSE operatorus, var izmantot MATCH/CASE. Darbojas kopš Python 3.10
match operacija:
    case 1: # Saskaitīšana
        summa = 0
        for skaitlis in skaitlu_saraksts:
            summa += skaitlis

        print(f"Operācijas tips: Summēšana, rezultāts: {summa}")
        exit()

    case 2: # Atņemšana
        starpiba = 0
        for skaitlis in skaitlu_saraksts:
            starpiba -= skaitlis

        print(f"Operācijas tips: Starpiba, rezultāts: {starpiba}")
        exit()

    case 3: # Reizinājums. Sākas ar viens, jo tad pirmais skaitlis tiek tajā iereizināts.
        reizinajums = 1
        for skaitlis in skaitlu_saraksts:
            reizinajums *= skaitlis

        print(f"Operācijas tips: Reizinajums, rezultāts: {reizinajums}")
        exit()