from random import sample


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Libros disponibles: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Puedes utilizar este libro")
        else:
            print(f"libro listo para usar {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("libro añadido")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    sample = Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Librería de Ejemplo")

    while(True):
        print(f"Bienvendio a {sample.name} libreria. Eliga opción")
        print("1. Mostrar Libros")
        print("2. Cantidad de Libros")
        print("3. Añadir Libro")
        print("4. Devolver Libro")
        option = input()
        if option not in ['1','2','3','4']:
            print("Ingrese opcion valida.")
            continue

        else:
            option = int(option)

        if option == 1:
            sample.displayBooks()

        elif option == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Ingresa tu nombre")
            sample.lendBook(user, book)

        elif option == 3:
            book = input("Ingrese nombre del libro a agregar: ")
            sample.addBook(book)

        elif option == 4:
            book = input("Ingrese el nombre del libro a devolver: ")
            sample.returnBook(book)

        else:
            print("Opcion invalida")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue