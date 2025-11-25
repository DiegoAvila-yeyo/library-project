import random
class Biiblioteca:
    
    def __init__(self,libro, autor):
        self.__libro = libro
        self.__autor = autor 
    
    def setLibro(self, libro):
        self.__libro = libro
        
    def setAutor(self,autor):
        self.__autor = autor
        
    def getLibro(self):
        return self.__libro
    
    def getAutor(self):
        return self.__autor
    
    def mostrar(self):
        print(f'El nombre del libro es {self.__libro} El autor es {self.__autor}')
    
    def buscarAutor(self, busqueda):
        texto = self.__autor
        patron = busqueda
        
        n = len(texto)
        m = len(patron)
        
        if m > n:
            return False
        
        for i in range(n - m +  1):
            coincide = True

            for j in range(m):
                if texto[i + j] != patron[j]:
                    coincide = False
                    break
                    
            if coincide:
                return True
            
        return False
    
        
        
    




n = int(input("Librosn vas a meter en sistema?"))
listaC = [0] * n

for i in range(n):
    libro= input("Dime el nombre del libro")
    autor = input("Dime el Autor")
    
    p = Biiblioteca(libro, autor)
    
    listaC[i] = p
    
for i in range(n):
    listaC[i].mostrar()
    

buscar = input("A quien quieres bucar?")
encontrado = False

for i in range(n):
    persona_actual = listaC[i]
    
    if persona_actual.buscarAutor(buscar):
        print("Encontrado!")
        persona_actual.mostrar()
        encontrado = True
    
if encontrado == False:
    print("Lo siento, no encontrado")
    