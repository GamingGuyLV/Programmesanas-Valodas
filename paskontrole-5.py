import matplotlib.pylab as plt

x_koordinatas = [-11,-9,-7,-5,-3,-1,0,1,3,5,7,9,11,13,15,17,19]
y_koordinatas = [-5,5,-7,7,0,10,15,-23,-14,11,16,0,-1,9,2,3,-20]

# Izliekam punktus uz plaknes
plt.plot(x_koordinatas, y_koordinatas, marker="o")

# Atrodam maximalo X koordinatu
max_x_valuta = 0
for x in x_koordinatas:
    x = abs(x)
    if x > max_x_valuta:
        max_x_valuta = x

# Atrodam maximalo Y koordinatu
max_y_valuta = 0
for y in y_koordinatas:
    y = abs(y)
    if y > max_y_valuta:
        max_y_valuta = y

# Uzliekam limitus, lai centrētu asis
plt.xlim(-abs(max_x_valuta) * 1.1, max_x_valuta * 1.1)
plt.ylim(-abs(max_y_valuta) * 1.1, max_y_valuta * 1.1)

# Uzliekam virsrakstus
plt.title("Funkcijas grafiks", loc = "right")
plt.xlabel("Laiks (sekundes)")
plt.ylabel("Rādītājs")

# Uzliekam režģlīnijas
plt.grid(color = "green", linestyle = "--")

# Novelkam centra līnijas
plt.axhline(0, color = "red", linewidth = 2)
plt.axvline(0, color = "red", linewidth = 2)

# Attēlojam diagrammu
plt.show()