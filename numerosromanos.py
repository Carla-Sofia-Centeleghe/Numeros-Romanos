import unittest
# Numero decimal a Romano
# Llega hasta el 3999
# Ni idea como se escribe el 4000 en romano
#Carla S. Centeleghe


def Roman(num):

    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    miles = m[num // 1000]
    cientos = c[(num % 1000) // 100]
    decenas = x[(num % 100) // 10]
    unos = i[num % 10]

    result = (miles + cientos + decenas + unos)

    return result


if __name__ == "__main__":
    number = int(input('Ingresa un numero: '))
    print(Roman(number))
