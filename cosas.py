class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return  self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre} pseudonimo: {self.__pseudonimo}"

    def edcribir(self):
        print(f" {self.__pseudonimo} esta escribiendo su siguiente obra")

class Libro:
    def __init__(self, tit, aut, an, ed):
        self.__titulo = tit
        self.__autor = aut
        self.__anio = an
        self.__editorial = ed

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, tit):
        self.__titulo = tit

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, aut):
        self.__autor = aut

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, an):
        self.__anio = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, ed):
        self.__editorial = ed

    def __str__(self):
        return f"""
        Titulo = {self.__titulo}
        Autor = {self.__autor}
        Año = {self.__anio}
        Editorial = {self.__editorial}
        """

    @classmethod
    def libro_planeta(cls, titulo, autor, anio):
        return cls(titulo, autor, anio, "Planeta")

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

class Alumno(Persona):
    def __init__(self, nombre, edad, numer_cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.__numer_cuenta = numer_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

    def __str__(self):
        return f"""
        Nombre = {self.nombre}
        Edad = {str(self.edad)}
        Numero cuenta = {self.__numer_cuenta}
        Carrera = {self.__carrera}
        Promedio = {str(self.__promedio)}
        """