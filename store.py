# ==========================================
# Proiect: Verificator Buget Magazin
# ==========================================

print("========== BUN VENIT LA MAGAZINUL MEU! ==========\n")

# Lista cu produsele și prețurile
stoc = [
    ("Penare", 25), 
    ("Ghiozdane", 75), 
    ("Culori", 3), 
    ("Pixuri", 2), 
    ("Carnete de note", 5)
]

# Afișăm stocul inițial
for produs, pret in stoc:
    print(f"Avem pe stoc : {produs}, care costa {pret} lei per buc")

print("-" * 50)

# Luăm bugetul de la utilizator
buget = float(input("Care este bugetul tau? "))

print("\n---------------- REZULTAT ----------------")

# Verificăm ce poate cumpăra
for produs, pret in stoc:
    if buget >= pret:
        print(f"Poti cumpara : {produs}, care costa {pret} lei per buc")
    else:
        print(f"Nu poti cumpara : {produs}, deoarece sunt prea scumpe pentru bugetul tau")

print("-" * 50)
print("========== LA REVEDERE! ==========")
