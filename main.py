import os
import matplotlib.pyplot as plt


class Populacja:
    def __init__(self, przyrost_naturalny):
        self.przyrost_naturalny = przyrost_naturalny

def oblicz_srednia(dane):
    suma = 0
    liczba_wierszy = 0

    for wiersz in dane:
        przyrost_naturalny = float(wiersz.replace(',', ''))
        suma += przyrost_naturalny
        liczba_wierszy += 1

    if liczba_wierszy > 0:
        srednia = suma / liczba_wierszy
        return srednia
    else:
        return None


try:
    nazwa= input("Podaj nazwe pliku wejściowego: ")
    with open(nazwa, 'r') as plik:
        dane = plik.readlines()

        sredni_przyrost = oblicz_srednia(dane)

        if sredni_przyrost is not None:
            print("Przyrost naturalny wynosi: ", sredni_przyrost)

            etykiety = [str(i) for i in range(1, len(dane)+1)]
            wartosci = [float(wiersz.replace(',', '')) for wiersz in dane]

            plt.bar(etykiety, wartosci)
            plt.title('Statystyki przyrostu naturalnego')
            plt.xlabel('Numer przyrostu naturalnego')
            plt.ylabel('Wartość przyrostu naturalnego')
            plt.show()
            #plt.savefig('wykres.png')


            nazwa_pliku = input("Podaj nazwę pliku do zapisu wyników: ")
            sciezka = os.path.join(os.getcwd(), nazwa_pliku)

            with open(sciezka, 'w') as wyniki_plik:
                wyniki_plik.write(f"Przyrost naturalny wynosi: {sredni_przyrost}\n")

        else:
            print("Brak danych w pliku.")

except FileNotFoundError:
    print("Plik nie został znaleziony")
