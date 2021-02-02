plansza = [['-','-','-'], ['-','-','-'], ['-','-','-']]

wybor = ""
nr_gracz = 0

def sprawdz_wiersze(plansza):
    for wiersz in plansza:
        wynik_sprawdzenia = sprawdz_wiersz(wiersz)
        if wynik_sprawdzenia == True:
            return True

def sprawdz_wiersz(wiersz):
    if wiersz[0] == wiersz[1] == wiersz[2] and (wiersz[0] == "x" or wiersz[0] == "o"):
        print("WIN POZIOM")
        return True

def sprawdz_kolumna(plansza):
    if plansza[0][0] == plansza[1][0] == plansza[2][0] and (plansza[0][0] == "x" or plansza[0][0] == "o"):
        print("WIN PION")   
        return True 

def sprawdz_skosy1(plansza):
    if plansza[0][0] == plansza[1][1] == plansza[2][2] and (plansza[0][0] == "x" or plansza[0][0] == "o"):
        print("WIN SKOS 1")
        return True
    
def sprawdz_skosy2(plansza):
    if plansza[0][2] == plansza[1][1] == plansza[2][0] and (plansza[0][2] == "x" or plansza[0][2] == "o"):
        print("WIN SKOS 2")
        return True

def wez_znaczek(nr_gracz):
    if nr_gracz == 0:
        return 'X'
    else:
        return 'O'

while wybor != 'q':
    wybor = wez_znaczek(nr_gracz)
    print("Jesteś:", wez_znaczek(nr_gracz))
    x = input("Podaj pozycję x: ")
    y = input("Podaj pozycję y: ")
    if int(x) > 2:
        continue
    if int(y) > 2:
        continue
    if plansza[int(x)][int(y)] == "X" or plansza[int(x)][int(y)] == "O":
        continue
    
    plansza[int(x)][int(y)] = wybor

    for i in range(8):
        print('-', end='')

    for wiersz in range(3):
        print()    
        for kolumna in range(3):
            print(plansza[wiersz][kolumna], " ", end='')

    print()
    for i in range(8):
        print('-', end='')
    print()

    if (sprawdz_kolumna(plansza) == True or sprawdz_wiersze(plansza) == True or sprawdz_skosy1(plansza) == True or sprawdz_skosy2(plansza) == True):
        break
    

    nr_gracz = (nr_gracz + 1) % 2
    