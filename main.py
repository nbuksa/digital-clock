import time
import os
import py_digital_clock as pdc
#from py_digital_clock import digital_clock (u tom slucaju samo pozovemo funkciju)

#u funkciji ne printamo jer mozemo funkciju ispisati na više mjesta, 
    #ali  ako je unutar funkcije print
    #onda smo definirali da se uvijek ispisuje u konzolu
    #ako funkcija vraća nešto to možemo ispisati i u bazi...

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(pdc.digital_clock(),'\t', pdc.digital_clock ('de_DE'))
        time.sleep(1)


if __name__ == '__main__': #osigurava da se izvršava samo ako se pokrene main datoteka
    main()
