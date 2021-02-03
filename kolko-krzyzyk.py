plansza = [['-','-','-'], ['-','-','-'], ['-','-','-']]


wybor = ""
nr_gracz = 0

def sprawdz_wiersze(plansza):
    for wiersz in plansza:
        wynik_sprawdzenia = sprawdz_wiersz(wiersz)
        if wynik_sprawdzenia == True:
            return True

def sprawdz_wiersz(wiersz):
    if wiersz[0] == wiersz[1] == wiersz[2] and ((wiersz[0] == "X") or (wiersz[0] == "O")):
        print("WIN POZIOM")
        return True

def sprawdz_kolumna(plansza):
    if plansza[0][0] == plansza[1][0] == plansza[2][0] and ((plansza[0][0] == "X") or (plansza[0][0] == "O")):
        print("WIN PION") 
        return True
    elif plansza[0][1] == plansza[1][1] == plansza[2][1] and ((plansza[0][1] == "X") or (plansza[0][1] == "O")):
        print("WIN PION") 
        return True
    elif plansza[0][2] == plansza[1][2] == plansza[2][2] and ((plansza[0][2] == "X") or (plansza[0][2] == "O")):
        print("WIN PION") 
        return True

def sprawdz_skosy1(plansza):
    if plansza[0][0] == plansza[1][1] == plansza[2][2] and ((plansza[0][0] == "X") or (plansza[0][0] == "O")):
        print("WIN SKOS 1")
        return True
    
def sprawdz_skosy2(plansza):
    if plansza[0][2] == plansza[1][1] == plansza[2][0] and ((plansza[0][2] == "X") or (plansza[0][2] == "O")):
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

    if int(x) > 2 or int(x) < 0:
        print("x poza zakresem [0, 2]")
        continue

    if int(y) > 2 or int(y) < 0:
        print("y poza zakrestem [0, 2]")
        continue

    if plansza[int(x)][int(y)] == "X" or plansza[int(x)][int(y)] == "O":
        print("Pole zajęte, wybierz inne.")
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

    if ((sprawdz_kolumna(plansza) == True) or (sprawdz_wiersze(plansza) == True) or (sprawdz_skosy1(plansza) == True) or (sprawdz_skosy2(plansza) == True)):
        break
    
    nr_gracz = (nr_gracz + 1) % 2   
    