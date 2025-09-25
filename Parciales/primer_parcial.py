import os

titulos: list[str] = [
    "El Señor de los Anillos",
    "Orgullo y Prejuicio",
    "Matar un Ruiseñor",
    "Cien Años de Soledad",
    "1984",
    "Don Quijote de la Mancha",
    "Harry Potter y la Piedra Filosofal",
    "Crimen y Castigo",
    "La Odisea",
    "El Principito",
    "Rayuela",
    "Fahrenheit 451",
    "Drácula",
    "El Gran Gatsby",
    "La Metamorfosis",
    "Los Miserables",
    "Hamlet",
    "El Retrato de Dorian Gray",
    "La Divina Comedia",
    "El Código Da Vinci",
    "El Hobbit",
    "Cumbres Borrascosas",
    "El Viejo y el Mar",
    "Alicia en el País de las Maravillas",
    "Frankenstein",
    "La Sombra del Viento",
    "El Alquimista",
    "Moby Dick",
    "Anna Karenina",
    "Las Aventuras de Sherlock Holmes",
    "El Perfume",
    "Un Mundo Feliz",
    "La Isla del Tesoro",
    "El Guardián entre el Centeno",
    "La Casa de los Espíritus",
    "El Nombre de la Rosa",
    "Los Juegos del Hambre",
    "La Ladrona de Libros",
    "El Amor en los Tiempos del Cólera",
    "Ensayo sobre la Ceguera",
    "La Tregua",
    "Pedro Páramo",
    "El Padrino",
    "La Historia Interminable",
    "El Silmarillion",
    "El Camino",
    "La Ciudad y los Perros",
    "El Coronel no Tiene Quien le Escriba",
    "El Psicoanalista",
    "La Reina del Sur",
    "La Carretera",
    "El Niño con el Pijama de Rayas",
    "La Elegancia del Erizo"
]

ejemplares: list[int] = [0] * len(titulos)

while True:
    # Limpiar la pantalla (funciona en terminales compatibles)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[1] LISTA", end=" | ")
    print("[2] AGREGAR", end=" | ")
    print("[4] SALIR")

    opcion = input()

    if opcion == "4":
        break

    if opcion == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        max_len = max(len(titulo) for titulo in titulos)

        print(f"{'Título'.ljust(max_len)} | Ejemplares")
        print("-" * (max_len + 13))

        for i in range(len(titulos)):
            print(f"{titulos[i].ljust(max_len)} | {ejemplares[i]}")

        input()
