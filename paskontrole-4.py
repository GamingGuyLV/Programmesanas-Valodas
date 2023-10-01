# Dotais masīvs jeb saraksts
masivs = [['John', 'Doe', '11'],['Mark', 'Gate', '24'],['Tom', 'Xin', '18'],['Sarah', 'Blake', '14'],['Otto', 'Ming', '14']]

# Izprintējam kolonnu nosaukumus izmantojot '\t' starp vārdiem, jo tas ievieto 'tab' atstarpi
print("N.p.k.\tVārds\tUzvārds\tVecums")
npk = 0 # Sākam ar 0, lai ciklā viegli pievienotu pa vienam.
for persona in masivs:
    npk += 1

    # Pieliekam katram mainīgajam savu vērtību izmantojot zināmus saraksta indeksus
    vards = persona[0]
    uzvards = persona[1]
    vecums = persona[2]

    # Izprintējam personas rindiņu atkal izmantojot '\t'
    print(f"{npk}\t{vards}\t{uzvards}\t{vecums}")