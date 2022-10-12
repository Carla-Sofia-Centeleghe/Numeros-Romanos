# Convierto numeros romanos a numeros decimales
# Carla S. Centeleghe

class decimal():
    def romano_a_decimal(romano):
        decimal = 0
        Numeros_romanos = ['C', 'L', 'X', 'V', 'I']
        significado_numeros_romanos = {
            'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        lastchar = Numeros_romanos[0]

        for char in Numeros_romanos:
            caracteres_repetidos = romano.count(char)
            if caracteres_repetidos == 4 and 'IIII' in romano or 'VVVV' in romano or 'XXXX' in romano or 'LLLL' in romano or 'CCCC' in romano:
                return 'ERROR'
            if caracteres_repetidos > 4 and (char == "I" or char == 'V' or char == 'X' or char == 'L' or char == "C"):
                return "ERROR"

        for char in romano:
            if lastchar == char or Numeros_romanos.index(char) > Numeros_romanos.index(lastchar):
                if char == 'C':
                    decimal += 100
                if char == 'L':
                    decimal += 50
                if char == 'X':
                    decimal += 10
                if char == 'V':
                    decimal += 5
                if char == 'I':
                    decimal += 1
            else:
                if char == 'C' and lastchar == 'X':
                    decimal += 80
                if char == 'L' and lastchar == 'X':
                    decimal += 30
                if char == 'X' and lastchar == 'I':
                    decimal += 8
                if char == 'V' and lastchar == 'I':
                    decimal += 3
            lastchar = char

        return decimal
