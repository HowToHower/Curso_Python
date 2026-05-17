#Títulos de los libros
titulo1 = "Cien años de soledad"
titulo2 = "El señor de los anillos"
titulo3 = "Don Quijote de la Mancha"

LongTitulo1 = len(titulo1)
LongTitulo2 = len(titulo2)
LongTitulo3 = len(titulo3)

print(LongTitulo1,LongTitulo2,LongTitulo3)

print(f"{titulo1}")

print(f"""
-------------------------------------
|Longitud del titulo de cada libro :)|
|{titulo1}: {LongTitulo1}            |
|{titulo2}: {LongTitulo2}            |
|{titulo3}: {LongTitulo3}            |
-------------------------------------
""")