
print("Vali programm:")
print("1 - Aastaaeg")
print("2 - Kiiruse kontroll")
print("3 - Taksosõit")

valik = input("Sisesta valik (1-3) => ")

if valik == "1":
    print("Aastaaeg")
    kuu = int(input("Sisesta kuu number (1-12) => "))

    if kuu in [12, 1, 2]:
        print("Talv")
    elif kuu in [3, 4, 5]:
        print("Kevad")
    elif kuu in [6, 7, 8]:
        print("Suvi")
    elif kuu in [9, 10, 11]:
        print("Sügis")
    else:
        print("Vigane kuu")

elif valik == "2":
    print("Kiiruse kontroll")
    kiirus = float(input("Sisesta kiirus (km/h) => "))

    if kiirus < 0:
        print("Kiirus ei tohi olla negatiivne!")
    elif kiirus > 90:
        print("Kiiruse ületamine!")
    else:
        print("Kiirus on lubatud.")

elif valik == "3":
    print("Taksosõit")
    pikkus = float(input("Sisesta sõidu pikkus (km) => "))
    oos = input("Kas sõit on öösel (jah/ei)? => ")

    hind = pikkus * 0.85

    if oos == "jah":
        hind *= 1.2

    if pikkus > 50:
        hind *= 0.9
        print("Pika sõidu allahindlus 10%")

    print(f"Sõidu hind: {hind:.2f} €")

else:
    print("Vigane valik")