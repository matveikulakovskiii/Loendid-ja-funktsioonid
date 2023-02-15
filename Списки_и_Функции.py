from OmaModule import *
ostud=[]
hinnad=[]
ostetud=[]
pood(ostud,hinnad)
print(ostud,hinnad)
while True:
        print("\nValige toiming:\n1. Ostetud kauba eemaldamine loendist\n2. Ostude ja nende hindade loendi kuvamine tähestikulises järjekorras\n3. Leia kõige kallim/odavaim toode\n4. Leidke soovitud kauba hind\n5. Uurige oma toote hinda\n0. Mine välja")
        menu = input("Sisestage valitud toimingu number: ")
        if menu == "1":
            delete_toot(ostud, hinnad, ostetud)
        elif menu == "2":
            sorteerimine(ostud, hinnad)
        elif menu == "3":
            max_min_otsing(ostud, hinnad)
        elif menu == "4":
            toode_otsing(ostud, hinnad)
        elif menu == "5":
            toode_otsing_ostetud(ostetud)
        elif menu == "0":
            print("Hüvasti!")
            break
        else:
            print("Vale valik")
