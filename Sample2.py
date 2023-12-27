class cuenta_bancaria:

    def __init__(self, saldo=0, propietario=None, tipo=None) -> None:
        self.saldo = saldo
        self.propietario = propietario
        self.tipo = tipo

    def depositar(self, monto):
        self.saldo += monto
        print('ahora saldo es' + str(self.saldo))

    def display(self):
            print(
                f'cuenta de tipo  {self.tipo}  de  {self.propietario}  con saldo  {str(self.saldo)}')

    def get_saldo(self):
        return self.saldo

    def retirar(self, monto):
        if(self.saldo > monto):
            self.saldo -= monto
            print('ahora el saldo es ' + str(self.saldo))
        else:
            print('saldo insuficiente')


yo = cuenta_bancaria(1000, 'me', 'ahorro')
yo.display()
yo.depositar(100)
yo.retirar(50)
yo.retirar(500)
yo.retirar(60)
yo.display()
