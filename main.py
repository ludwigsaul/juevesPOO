from cosas import *

def main():
    l1 = Libro.libro_planeta("El perfume",Autor("Patrick", "PS"), 1980)
    print(l1)

    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("-------Herencia-------")
    al2 = Alumno("Jose", 19, "23333", "ICO", 9)
    al2.nombre = "pepe"
    print(al2)

main()