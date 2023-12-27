class imc:
        nombre = None
        altura = 0
        peso = 0

        def __init__(self, nombre, altura, peso) -> None:
            self.nombre = nombre
            self.altura = altura
            self.peso = peso

        def consulta(self):
            imc = self.peso / (self.altura * self.altura)

            if imc < 18.5:
                print(
                    f'El IMC de {self.nombre} es {imc} y se encuentra por debajo de lo ideal')
            elif imc >= 18.5 and imc <= 24.9:
                print(
                    f'El IMC de {self.nombre} es {imc} y tiene peso ideal')
            elif imc >= 25 and imc <= 25.9:
                    print(
                    f'El IMC de {self.nombre} es {imc} y tiene sobrepeso')
            elif imc >= 30 and imc <= 34.9:
                print(
                    f'El IMC de {self.nombre} es {imc} y tiene obesidad')
            elif imc > 35:
                    print(
                    f'El IMC de {self.nombre} es {imc} y tiene obesidad morbida')

test = imc("Johan",188,68)
test.consulta()
