from pickle import FALSE
from unicodedata import name

delegaciones = []
class Deleg:
    nombre = None
    pais = None
    nDeportistas = 0
    medallasOro = 0
    medallasPlata = 0
    medallasBronce = 0

    def __init__(self,nombre, pais, nDeportistas, medallasOro, 
                medallasPlata, medallasBronce) -> None:
        self.nombre = nombre
        self.pais = pais
        self.nDeportistas = nDeportistas
        self.medallasOro = medallasOro
        self.medallasPlata = medallasPlata
        self.medallasBronce = medallasBronce
    
class Tools(Deleg):

    def mostrarDelegacion(self):
        print(
            f'la delegación {self.nombre} del pais {self.pais} tiene:\n {self.medallasOro} medalla/as de oro\n {self.medallasPlata} medalla/as de plata\n {self.medallasBronce} medalla/as de bronce'
        )

    def calMedallas(self):
        total = self.medallasOro + self.medallasPlata + self.medallasBronce
        print(
            f'La cantidad total de medallas es {total}'
        )
        
    def getNombre(self):
        return self.name

    def setNombre(self, name):
        self.nombre = name
        print(
            f'el nuevo nombre de la delegacion es {self.nombre}'
        )

    def addDelegation (self):
        nombre = input("Digite nombre delegacion: ")
        pais = input("Digite pais delegacion: ")
        deportistas = int(input("Digite deportistas delegacion: "))
        oro = int(input("Digite oro delegacion: "))
        plata = int(input("Digite plata delgacion: "))
        bronce = int(input("Digite bronce delgacion: "))
        nDelegation = Deleg(nombre, pais, deportistas, oro, plata, bronce)
        delegaciones.append(nDelegation)


ex1 = Tools("Asocamperos","Colombia",343,345,233,290)
ex1.getNombre



 



    

    # objColombia = delegacion(nombre, pais, deportistas, oro, plata, bronce)
    # objColombia.mostrarDelegacion()

# finish = False
# while (finish == False):

#     print('--------------------------MENÚ--------------------------')
#     print('1. Listar delegaciones \n2. Modificar medallas delegacion\n3. Delegacion mas medallas\n4. Delegacion menos medallas \n5. Salir')
#     op = input()
#     if op == 1:
#         objColombia.mostrarDelegacion()
#         objColombia.mostrarDelegacion()
#         objColombia.mostrarDelegacion()
#         objColombia.mostrarDelegacion()
#         objColombia.mostrarDelegacion()
#     elif op == 2:
#         newDelegacion = input('Digite delegacion')
#         if (newDelegacion == objColombia.nombre):
#             medal = input('que medalla')
#             if(medal == "oro"):
#                 cuantas = input('cuantas')
#                 objColombia.medallasOro = cuantas

#     salir = input('desea salir? \n1 para si \n2 para no')  
#     if salir == 1:
#             finish == True 
#     elif salir == 2:
#         pass
        
        
        
        


        



