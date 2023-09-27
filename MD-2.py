skaitlu_saraksts = []

def summa(skaitlu_saraksts: list):
    summa = 0
    for skaitlis in skaitlu_saraksts:
        summa += skaitlis

    return summa

def starpiba(skaitlu_saraksts: list):
    starpiba = 0
    for skaitlis in skaitlu_saraksts:
        starpiba -= skaitlis

    return starpiba

def reizinajums(skaitlu_saraksts: list):
    reizinajums = 1
    for skaitlis in skaitlu_saraksts:
        reizinajums *= skaitlis

    return reizinajums

def dalijums(skaitlu_saraksts: list):
    dalijums = skaitlu_saraksts[0]
    for skaitlis in skaitlu_saraksts:
        dalijums /= skaitlis

    return dalijums


print("Izvēlaties opciju:")
print("1 - Summa")
print("2 - Starpība")
print("3 - Reizinājums")
print("4 - Dalījums")


opcija = int(input())

# Cikls 6 ciparu ievadei, ejam līdz 7, jo pēdējo ciklu pitons neveic
for skaitlis in range(1, 7, 1):
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


match opcija:
    case 1:
        print("Izvēlēta summēšana")
        print(f"Summa no skaitļiem: {skaitlu_saraksts} = {summa(skaitlu_saraksts)}")

    case 2:
        print("Izvēlēta starpība")
        print(f"Starpība no skaitļiem: {skaitlu_saraksts} = {starpiba(skaitlu_saraksts)}")

    case 3:
        print("Izvēlēta reizināšana")
        print(f"Reizinājums no skaitļiem: {skaitlu_saraksts} = {reizinajums(skaitlu_saraksts)}")

    case 4:
        print("Izvēlēta dalīšana")
        print(f"Dalījums no skaitļiem: {skaitlu_saraksts} = {dalijums(skaitlu_saraksts)}")