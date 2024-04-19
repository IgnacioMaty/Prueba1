import math

def calcular_circunferencia(radio):
    pi = round(math.pi, 6)  # Redondear pi a 6 decimales
    circunferencia = 2 * pi * radio
    return circunferencia

def main():
    radios = [3, 8, 10]

    for radio in radios:
        circunferencia = calcular_circunferencia(radio)
        print(f"Para un radio de {radio}, la circunferencia es: {circunferencia}")

if __name__ == "__main__":
    main()
