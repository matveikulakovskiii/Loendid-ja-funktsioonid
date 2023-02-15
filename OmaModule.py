def pood(ostud:list,hinnad:list):
    a=int(input("Kui palju tooteid soovite osta? "))
    for i in range(a):
        toot = input("Sissesta toot: ")
        hind = float(input("Sissesta toote hind: "))
        ostud.append(toot)
        hinnad.append(hind)
    return toot,hind

def delete_toot(ostud:list,hinnad:list,ostetud:list):
    toot=input("Sisesta toot: ")
    if toot in ostud:
            ind=ostud.index(toot)
            ostetud.append(ind)
            print(f"Toot {toot} eest ostetud {hinnad[ind]}")
            ostud.pop(ind)
            hinnad.pop(ind)
    else:
        print("Vale toot")
    return ostud,hinnad,ostetud

def sorteerimine(ostud:list,hinnad:list):
    sorted_ostud = sorted(zip(ostud, hinnad))
    print("Ostunimekirjas:")
    for toot, hind in sorted_ostud:
         print(f"{toot}: {hind}")


def max_min_otsing(ostud:list,hinnad:list):
    max_hind = max(hinnad)
    min_hind = min(hinnad)
    max_ind = hinnad.index(max_hind)
    min_ind = hinnad.index(min_hind)
    print(f"Kõige kallim ese: {ostud[max_ind]} за {max_hind}")
    print(f"Odavaim kaup: {ostud[min_ind]} за {min_hind}")

def toode_otsing(ostud:list):
    toode_otsing = input("Sisesta toote nimi: ")
    if toode_otsing in ostud:
         index = ostud.index(toode_otsing)
         print(f"Hind {toode_otsing}: {ostud[index]}")
    else:
         print("Seda toodet ei ole ostunimekirjas.")

def toode_otsing_ostetud(ostetud:list):
    toode_otsing_ostetud = input("Sisesta toote nimi: ")
    if toode_otsing_ostetud in ostetud:
         index = ostetud.index(toode_otsing)
         print(f"Hind {toode_otsing_ostetud}: {ostetud[index]}")
    else:
         print("Seda toodet ei ole teie ostunimekirjas.")