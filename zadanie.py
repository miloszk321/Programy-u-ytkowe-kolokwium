class Car:
    def __init__(self, marka, rok_produkcji):
        self.marka = marka
        self.rok_produkcji = rok_produkcji

car1 = Car("Toyota", 2019)

car2 = Car("Ford", 2020)
print("Marka samochodu car2:", car2.marka)
print("Rok produkcji samochodu car2:", car2.rok_produkcji)
car1 = car2
print("\nPo przypisaniu car1 = car2:")
print("Marka samochodu car1:", car1.marka)
print("Rok produkcji samochodu car1:", car1.rok_produkcji)


class Owoc:
    def __init__(self,kolor,waga):
        self.kolor = kolor
        self.waga = waga

    def jest_swiezy(self):
        #domyslnie swiezy
        return True

class Jablko(Owoc):
    def __init__(self, kolor="czerwony",waga=100):
        super().__init__(kolor,waga)


class Banan(Owoc):
    def __init__(self, kolor="żółty",waga=120):
        super().__init__(kolor,waga)

class Pomarancza(Owoc):
    def __init__(self, kolor="Pomaranczowy",waga=150):
        super().__init__(kolor,waga)


    def jest_swiezy(self):
        return self.kolor == "pomaranczowy"

jablko = Jablko()
banan = Banan()
pomarancza = Pomarancza()

print("Jablko:")
print("Kolor:",jablko.kolor)
print("Waga:",jablko.waga)
print("Czy jest swieze",jablko.jest_swiezy())

print("\nBanan:")
print("Kolor:",banan.kolor)
print("Waga:",banan.waga)
print("Czy jest swieze",banan.jest_swiezy())

print("\npomarancza:")
print("Kolor:",pomarancza.kolor)
print("Waga:",pomarancza.waga)
print("Czy jest swieze",pomarancza.jest_swiezy())

class Account:
    def __init__(self, saldo_poczatkowe):
        self.saldo = saldo_poczatkowe

    def wplata(self, kwota):
        self.saldo += kwota
        print("Wpłata udana. Aktualne saldo:", self.saldo)

    def wyplata(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print("Wypłata udana. Aktualne saldo:", self.saldo)
        else:
            print("Nie wystarczające środki na koncie.")

    def przelew(self, inne_konto, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            inne_konto.wplata(kwota)
            print("Przelew udany. Aktualne saldo:", self.saldo)
        else:
            print("Nie wystarczające środki na koncie.")

# Tworzenie kont
konto1 = Account(1000)
konto2 = Account(2000)
konto3 = Account(500)

# Wykonanie kilku operacji na kontach
konto1.wplata(500)
konto2.wyplata(100)
konto3.przelew(konto1, 200)

class PrivatAccount(Account):
    def przelew_wynagrodzenia(self, inne_konto, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            inne_konto.wplata(kwota)
            print("Przelew wynagrodzenia udany. Aktualne saldo:", self.saldo)
        else:
            print("Nie wystarczające środki na koncie.")

class FirmAccount(Account):
    def przelew_do_ZUS(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print("Przelew do ZUS udany. Aktualne saldo:", self.saldo)
        else:
            print("Nie wystarczające środki na koncie.")

    def przelew_do_US(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print("Przelew do US udany. Aktualne saldo:", self.saldo)
        else:
            print("Nie wystarczające środki na koncie.")

# Przykładowe użycie
konto_prywatne = PrivatAccount(5000)
konto_firmowe = FirmAccount(10000)

konto_prywatne.przelew_wynagrodzenia(konto_firmowe, 2000)
konto_firmowe.przelew_do_ZUS(1000)
konto_firmowe.przelew_do_US(1500)

class Romanian:
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral

    def to_int(self):
        result = 0
        prev_value = 0
        for numeral in reversed(self.roman_numeral):
            value = self.roman_numerals[numeral]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

    def __add__(self, other):
        return self.to_int() + other.to_int()

    def __sub__(self, other):
        return self.to_int() - other.to_int()

    def __mul__(self, other):
        return self.to_int() * other.to_int()

    def __str__(self):
        return self.roman_numeral

# Przykładowe użycie
roman1 = Romanian("XV")
roman2 = Romanian("III")

print("Suma:", roman1 + roman2)
print("Różnica:", roman1 - roman2)
print("Iloczyn:", roman1 * roman2)
