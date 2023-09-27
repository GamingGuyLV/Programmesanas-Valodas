# Skaitļu ievade
pirmais_skaitlis = input("Ievadiet pirmo skaitli: ")
otrais_skaitlis = input("Ievadiet otro skaitli: ")


# Pārbaudu vai decimālpunkts ir ielikts, ja ir pārveidoju par Float, ja nē tad Integer
try:
    if "," in pirmais_skaitlis or "," in otrais_skaitlis: # Pārbaudu vai ir ielikts komats
        print(f"Kādā no skaitļiem ir komats ',' , kuru šī programma neatbalsta: {pirmais_skaitlis} | {otrais_skaitlis} . Lūdzu palaižiet programmu vēlreiz un komata vietā liekat punktu.")

    if "." in pirmais_skaitlis:
        pirmais_skaitlis = float(pirmais_skaitlis)
    else:
        pirmais_skaitlis = int(pirmais_skaitlis)


    if "." in otrais_skaitlis:
        otrais_skaitlis = float(otrais_skaitlis)
    else:
        otrais_skaitlis = int(otrais_skaitlis)

except ValueError as error: # Ja ir kāda kļūda pārveidojot, tad izmetam kļūdu un pārtraucam programmas darbību.
    print(f"Kaut kas nebija pareizi, kļūda: {error}")
    exit()


if pirmais_skaitlis > otrais_skaitlis: # Pārbaudam vai pirmais skaitlis ir lielāks par otro
    print(f"Pirmais skaitlis: {pirmais_skaitlis} ir lielāks par otro skaitli: {otrais_skaitlis}")

elif pirmais_skaitlis < otrais_skaitlis: # Pārbaudam vai pirmais skaitlis ir mazāks par otro
    print(f"Pirmais skaitlis: {pirmais_skaitlis} ir mazāks par otro skaitli: {otrais_skaitlis}")

elif pirmais_skaitlis == otrais_skaitlis: # Pārbaudam vai pirmais skaitlis ir vienāds ar otro
    print(f"Pirmais skaitlis: {pirmais_skaitlis} un otrais skaitlis: {otrais_skaitlis} ir vienādi")

else: # Ja neviens no tiem neatbilst, to arī pasakam.
    print("Kaut kas aizgāja grīstē... oops!")