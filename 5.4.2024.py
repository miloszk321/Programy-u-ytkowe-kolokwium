class Bohater:
    def __init__(self, imie, zycie_procent, punkty_tak):
        self.imie = imie
        self.zycie_procent = max(0, min(zycie_procent, 100))
        self.punkty_tak = punkty_tak

    def zmien_zycie(self, zmiana):
        self.zycie_procent = max(0, min(self.zycie_procent + zmiana, 100)) # zycie nie mniej niz 0% nie wiecej niz 100%


class Lucznik(Bohater):
    def __init__(self, imie, zycie_procent, zrecznosc, punkty_tak):
        super().__init__(imie, zycie_procent, punkty_tak)
        self.zrecznosc = zrecznosc

    def moc_ataku(self):
        return self.zrecznosc * self.punkty_tak * self.zycie_procent /100

class Wojownik(Bohater):
    def __init__(self, imie, zycie_procent, sila, punkt_tak):
        super().__init__(imie, zycie_procent,punkt_tak)
        self.sila = sila

    def zmien_zycie(self, zmiana):
        self.zycie_procent = max(0, min(self.zycie_procent + zmiana, 100))
        if self.zycie_procent < 20:
            self.zycie_procent = 150  # Wpadnięcie w szał


    def moc_ataku(self):
        return self.sila * self.punkty_tak * self.zycie_procent /100

lucznik = Lucznik("Edek", 80, 10, 5)
wojownik = Wojownik("Geralnd", 41, 15, 10)

print(f"{lucznik.imie}: Moc ataku = {lucznik.moc_ataku()}")
print(f"{wojownik.imie}: Moc ataku = {wojownik.moc_ataku()}")

lucznik.zmien_zycie(-30)
wojownik.zmien_zycie(-30)

print(f"{lucznik.imie}: Zmiana zycia = {lucznik.zycie_procent}%")
print(f"{wojownik.imie}: Zmiana zycia = {wojownik.zycie_procent}%")


class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Wektory muszą mieć tę samą długość")
        result = [x + y for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise ValueError("Wektory muszą mieć tę samą długość")
        result = [x - y for x, y in zip(self.elements, other.elements)]
        return Vector(result)

    def __mul__(self, scalar):
        result = [x * scalar for x in self.elements]
        return Vector(result)

    def __str__(self):
        return str(self.elements)


# Przykładowe użycie:

vec1 = Vector([1, 2, 3])
vec2 = Vector([4, 5, 6])

print("vec1:", vec1)
print("vec2:", vec2)

vec3 = vec1 + vec2
print("vec1 + vec2:", vec3)

vec4 = vec1 - vec2
print("vec1 - vec2:", vec4)

vec5 = vec1 * 2
print("vec1 * 2:", vec5)


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        terms = []
        for i, coef in enumerate(self.coefficients[::-1]):
            if coef != 0:
                if i == 0:
                    terms.append(str(coef))
                else:
                    if coef == 1:
                        terms.append(f"x^{i}")
                    elif coef == -1:
                        terms.append(f"-x^{i}")
                    else:
                        terms.append(f"{coef}x^{i}")
        if not terms:
            return "0"
        else:
            return " + ".join(terms[::-1])

    def degree(self):
        return len(self.coefficients) - 1

    def __mul__(self, other):
        degree_result = self.degree() + other.degree()
        result_coefficients = [0] * (degree_result + 1)

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result_coefficients)

    def evaluate_at(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result

# Przykładowe użycie
p1 = Polynomial([2, -2, 1, -1, 3])  # Tworzymy wielomian 3x^4 - x^3 + x^2 - 2x + 2
p2 = Polynomial([1, 2, -1])  # Tworzymy wielomian -x^2 + 2x + 1

print("Wielomian p1:", p1)
print("Stopień wielomianu p1:", p1.degree())

print("Wielomian p2:", p2)
print("Stopień wielomianu p2:", p2.degree())

print("Wynik mnożenia p1 * p2:", p1 * p2)

x_value = 2
print(f"Wartość wielomianu p1 w punkcie x={x_value}:", p1.evaluate_at(x_value))


