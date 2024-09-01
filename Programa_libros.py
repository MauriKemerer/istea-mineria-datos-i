class Libros:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
        
lista_libros = []

def agregar_libro():
    print("A continuación, indique los datos del libro a ingresar, gracias!\n")
    titulo = input("Titulo del libro, por favor: ")
    autor = input("Autor del libro, por favor: ")
    genero = input("Género del libro, por favor: ")
    puntuacion = float(input("Puntuación del libro, por favor: "))
    libro = Libros(titulo, autor, genero, puntuacion)
    lista_libros.append(libro)

def libros_genero():
    genero_usuario = input("Ingrese el género que desea buscar: ")
    genero = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero_usuario.lower()]
    
    if genero:
        print(f"Libros en el género {genero_usuario}:")
        for libro in genero:
            print(libro)
    else:
        print(f"No se encontraron libros en el género {genero_usuario}")
    
def recomendar_libro():
    genero_usuario = input("Ingrese el género que le interesa: ")
    libros_por_genero = [libro for libro in lista_libros if libro.genero.lower() == genero_usuario.lower()]
    if libros_por_genero:
        mejor_libro = max(libros_por_genero, key=lambda libro: libro.puntuacion)
        print(f"El libro más recomendado en el género {genero_usuario} es '{mejor_libro.titulo}' con una puntuación de {mejor_libro.puntuacion}.\n")
    else:
        print(f"No se encontraron libros en el género {genero_usuario}.")

while True:
    print("Indique que acción quiere realizar")
    print("1)Agregar libro")
    print("2)Buscar por género")
    print("3)Buscar el mejor del género")
    print("4)Salir del menú")
    opcion_usuario = input("Ingrese el número de opción que desea: ")

    if opcion_usuario == "1":
        agregar_libro()
    elif opcion_usuario == "2":
        libros_genero()
    elif opcion_usuario == "3":
        recomendar_libro()
    elif opcion_usuario == "4":
        print("Gracias por usar nuestro programa de recomendaciones")
        break
    else:
        print("La opción que pusiste no es válida, probá de nuevo el programa")

lista_libros = []
