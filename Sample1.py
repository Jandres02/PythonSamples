class Empleado():
    nombre = ''
    id = 0
    edad = 0
    estado_civil = ''
    salario = 0

    def __init__(self, nombre, id, edad, estado_civil, salario) -> None:
        self.nombre = nombre
        self.id = id
        self.edad = edad
        self.estado_civil = estado_civil
        self.salario = salario

    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id

    def get_edad(self):
        return self.edad

    def get_estado_civil(self):
        return self.estado_civil

    def get_salario(self):
        return self.salario


class Programador(Empleado):
    horas = 0
    lenguaje = ''

    def __init__(self, nombre, id, edad, estado_civil, salario, horas, lenguaje) -> None:
        super().__init__(nombre, id, edad, estado_civil, salario)
        self.horas = horas
        self.lenguaje = lenguaje

    def get_horas(self):
        return self.horas

    def get_lenguaje(self):
        return self.lenguaje


class Arquitecto(Empleado):
    proyectos = 0

    def __init__(self, nombre, id, edad, estado_civil, salario, proyectos) -> None:
        super().__init__(nombre, id, edad, estado_civil, salario)
        self.proyectos = proyectos

    def get_proyectos(self):
        return self.proyectos


class Director(Empleado):
    experiencia = 0

    def __init__(self, nombre, id, edad, estado_civil, salario, experiencia) -> None:
        super().__init__(nombre, id, edad, estado_civil, salario)
        self.experiencia = experiencia

    def get_experiencia(self):
        return self.experiencia


x = Programador('Luis', '1', 'soltero', )
