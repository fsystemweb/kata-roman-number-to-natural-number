import sys


def getRomanNumber():
    print("Bienvenido, por favor ingrese el numero Romano a convertir")
    romanNumber = input()
    if not runValidation(romanNumber):
        print("No ha ingresado un numero romano valido, vuelva a intentarlo")
        return ""

    return romanNumber.upper()


def validateRomanNumber(romanNumber):
    romanNumbersList = ["I", "V", "X", "L", "C", "D", "M"]
    if romanNumber in romanNumbersList:
        return True
    return False


def validateIsString(param):
    if param.isnumeric():
        return False
    return True


def runValidation(param):
    for char in param:
        if not validateIsString(char):
            return False
        if not validateRomanNumber(char):
            return False
    return True


def romano_a_arabigo(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    entero = 0

    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i - 1]]:
            entero += romanos[romano[i]] - 2 * romanos[romano[i - 1]]
        else:
            entero += romanos[romano[i]]

    return entero


numero_romano = getRomanNumber()
if not numero_romano == "":
    print("Numero Arabigo:" + str(romano_a_arabigo(numero_romano)))
