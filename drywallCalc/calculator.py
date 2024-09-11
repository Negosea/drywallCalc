class DrywallCalculator:
    def __init__(self):
        print("Calculadora de Drywall iniciada")

    def calcular_quantitativo(self, comprimento_parede):
        return f"Quantitativo para {comprimento_parede} metros de parede calculado"

if __name__ == "__main__":
    calc = DrywallCalculator()
    resultado = calc.calcular_quantitativo(7)
    print(resultado)
    print("Hello, World!")

   