
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def getTitulo(self):
        return self.titulo
    
    def getAutor(self):
        return self.autor
    
    def getAño(self):
        return self.año
    
    def setTitulo(self, titulo):
        self.titulo = titulo
        
    def setAutor(self, autor):
        self.autor = autor
        
    def setAño(self, año):
        self.año = año
        
 # ---------------------------------------------------------------------------

lista = []
def crearLibro():
    titulo = input("Elija el título del libro\n")
    titulo = yaExiste(titulo)
    autor = input("Elija el autor del libro\n")
    año = input("Elija el año de publicación del libro\n")
    año=esNumero(año)
    libro = Libro(titulo, autor, año)
    lista.append(libro)

def yaExiste(titulo):
    for obj in lista:
            if obj.titulo.lower() == titulo.lower():
                print ("El libro con ese nombre ya existe en la biblioteca.")
                titulo = input("Introduzca el nuevo título: ")
                titulo = yaExiste(titulo)
    return titulo
        
            
def esNumero(año):
    if año.isdigit():
        año=int(año)
        if año >= 0 and año <=2024:
            return año
        else: 
            print("No introduzca caracteres fuera de rango (0 - 2024)")
            año = input("Elija el año de publicación del libro\n")
            return esNumero(año)
    else:
        print("No introduzca caracteres no numéricos")
        año = input("Elija el año de publicación del libro\n")
        return esNumero(año)
    
def buscarLibro():
    while True:
        print("Estos son los libros con los que contamos: \n")
        for i in range(len(lista)):
            imprimirLibro(i)
        op = (input("""
        *************************                   
        *   1. Por título       *
        *   2. Por autor        *
        *   3. Por año          *
        *   4. Volver           *
        *************************
        Elija una opcion numérica del 1 al 4                     
        """))
        cont = 0
        if op.isdigit() and op >= "1" and op <= "4":
            if op == "1":
                titulo = input("Introduzca el título: ")
                encontro = False
                for obj in lista:
                    if titulo.lower() in obj.getTitulo().lower():
                        cont + 1
                        imprimirLibro(cont)
                        encontro = True
                if not encontro:
                    print("No existe el libro")
            elif op == "2":
                autor = input("Introduzca el autor: ")
                encontro = False
                for obj in lista:
                    if autor.lower() in obj.getAutor().lower():
                        cont + 1
                        imprimirLibro(cont)
                        encontro = True
                if not encontro:
                    print("No existe el libro")
            elif op == "3":
                año = input("Año del libro: ")
                año = esNumero(año)
                encontro = False
                for obj in lista:
                    if año.lower() in obj.getAño().lower():
                        #ME DICE QUE AÑO ES INT
                        cont + 1
                        imprimirLibro(cont)
                        encontro = True
                if not encontro:
                    print("No existe el libro")
            elif op == "4":
                break

def borrarLibro(lista:[]):
    while True:
        for i in range(len(lista)):
            imprimirLibro(i)
        op = (input("""
        ************************************                   
        *   1. Borrar por título           *
        *   2. Borrar por autor y titulo   *
        *   3. Volver                      *
        ************************************   
        Elija una opcion numérica del 1 al 3                  
        """))
        if op.isdigit() and op >= "1" and op <= "3":
            if op == "1":
                titulo = input("Introduzca el título: ")
                for obj in lista:
                    if obj.getTitulo().lower() == titulo.lower():
                        lista.remove(obj)
                        print("Se eliminó")
            elif op == "2":
                autor = input("Introduzca el autor")
                titulo = input("Introduzca el título: ")
                for obj in lista:
                    if obj.getAutor().lower() == autor.lower() and obj.getTitulo().lower() == titulo.lower():
                        lista.remove(i)
                        print("Se eliminó")
            elif op == "3":
                break
                
def modificar():
    while True:
        for i in range(len(lista)):
            imprimirLibro(i)
        op = (input("""
        ****************************************                   
        *   1. Editar por título               *
        *   2. Editar por autor                *
        *   3. Editar por año                  *
        *   4. Volver                          *
        ****************************************   
        Elija una opcion numérica del 1 al 4                  
        """))
        
        if op.isdigit() and op >= "1" and op <= "4":
            if op == "1":
                modificarTitulo()
            elif op == "2":
                modificarAutor()
            elif op == "3":
                modificarAño()
            elif op == "4":
                break

def modificarTitulo():
    titulo = input("Introduzca el título del libro: ")
    for obj in lista:
        if obj.getTitulo().lower() == titulo.lower():
            titulo = input("Introduzca el nuevo título: ")
            titulo = yaExiste(titulo)
            obj.setTitulo(titulo)
            
def modificarAutor():
    titulo = input("Introduzca el título del libro: ")
    for obj in lista:
        if obj.getTitulo().lower() == titulo.lower():
            autor = input("Introduzca el nuevo autor: ")
            obj.setAutor(autor)
            
def modificarAño():
    titulo = input("Introduzca el título del libro: ")
    for obj in lista:
        if obj.getTitulo().lower() == titulo.lower():
            año = input("Introduzca qué nuevo año desea: ")
            año=esNumero(año)
            obj.setAño(año)

def imprimirLibro(pos):
    print ("Título del libro: ", lista[pos].titulo)
    print ("Autor del libro: ", lista[pos].autor)
    print ("Año de publicación: ", lista[pos].año)
    print ("--------------------------------------")
    
op = "0"
while True:
    op = input("""
    *********************************
    *               BIBLIOTECA      *
    *   1. Nuevo libro              *
    *   2. Busqueda                 *
    *   3. Borrar libro             *
    *   4. Modificar libro          *
    *   5. Mostrar libros           *    
    *   6. Salir                    *
    *********************************   
    Elija una opcion numérica del 1 al 6      
    """)
    if op.isdigit() and op >= "1" and op <= "6":
        if op == "1":
            crearLibro()
        elif op == "2":
            buscarLibro()
        elif op == "3":
            borrarLibro(lista)
        elif op == "4":
            modificar()
        elif op == "5":
            for i in range(len(lista)):
                imprimirLibro(i)
        elif op == "6":
            break
    



#autor: Alicia Rodríguez García
#DAM2A
#inicio --> 18/10/2023
#fin --> 03/11/2023