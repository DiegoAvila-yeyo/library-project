class Libro:
    def __init__(self, tit, cod, aut, edi):
        self.__titulo = tit
        self.__codigo = cod
        self.autor = aut
        self.editorial = edi

    def setTitulo(self, tit):
        self.__titulo = tit

    def getTitulo(self):
        return self.__titulo
    
    def setCodigo(self, cod):
        self.__codigo = cod
    
    def getCodigo(self):
        return self.__codigo
        
    def mostrarAtrib(self):
        print("Título:", self.__titulo)
        print("Código:", self.__codigo)
        print("Autor:", self.autor)
        print("Editorial:", self.editorial)

    def verificarAutor(self, autorBuscado):
        if autorBuscado.lower() in self.autor.lower():
            return True
        else:
            return False


class Prestamo:
    def __init__(self, cod, nomb, fechsol):
        self.__codPedido = cod
        self.__nombalumno = nomb
        self.fecha = fechsol
        self.__fechaDevolucion = "Pendiente"

    def setCodPedido(self, cod):
        self.__codPedido = cod

    def getCodPedido(self):
        return self.__codPedido
 
    def setNombAlumno(self, nom):
        self.__nombalumno = nom

    def getNombAlumno(self):
        return self.__nombalumno
    
    def setFechaDevolucion(self, fech):
        self.__fechaDevolucion = fech

    def getFechaDevolucion(self):
        return self.__fechaDevolucion
    
    def mostrarObj(self):
        print("Libro Prestado (Código):", self.getCodPedido())
        print("Alumno:", self.getNombAlumno())
        print("Fecha Préstamo:", self.fecha)
        print("Fecha Devolución:", self.getFechaDevolucion())

    def validarFecha(self, fecha_texto):
        if len(fecha_texto) != 10: return False
        
        if fecha_texto[2] != "/" or fecha_texto[5] != "/": return False
        
        dia_txt = fecha_texto[0:2]
        mes_txt = fecha_texto[3:5]
        anio_txt = fecha_texto[6:10]

        if not (dia_txt.isdigit() and mes_txt.isdigit() and anio_txt.isdigit()):
            return False
        
        d = int(dia_txt)
        m = int(mes_txt)
        a = int(anio_txt)

        if a < 2025 or a > 2030: return False
        if m < 1 or m > 12: return False

        dias_limite = 31 # Por defecto la mayoría tiene 31
        
        # Meses con 30 días: Abril(4), Junio(6), Septiembre(9), Noviembre(11)
        if m == 4 or m == 6 or m == 9 or m == 11:
            dias_limite = 30
            
        # Febrero (2)
        elif m == 2:
            # Regla simple de bisiesto: divisible entre 4
            if a % 4 == 0:
                dias_limite = 29
            else:
                dias_limite = 28
        
        # Verificamos si el día se pasa del límite de ese mes
        if d < 1 or d > dias_limite:
            return False

        return True
    
    def corregirFechaPrestamo(self):
        if self.validarFecha(self.fecha):
            print("La fecha actual ya es correcta. No se requiere cambio.")
        else:
            print("La fecha actual está mal. Introduce la nueva fecha (dd/mm/aaaa):")
            nueva = input()
            if self.validarFecha(nueva):
                self.fecha = nueva
                print("Fecha corregida exitosamente.")
            else:
                print("Error: La nueva fecha tampoco es válida.")


# ==========================================
# BLOQUE 1: INICIALIZACIÓN Y DATOS FIJOS
# ==========================================

MAX_CAPACIDAD = 50 
librero = [None] * MAX_CAPACIDAD 
prestamos = [None] * MAX_CAPACIDAD

total_libros = 0 
total_prestamos = 0

librero[0] = Libro("El Principito", 101, "Antoine de Saint-Exupery", "Salamandra")
total_libros = total_libros + 1
librero[1] = Libro("Cien anios de soledad", 102, "Gabriel Garcia Marquez", "Diana")
total_libros = total_libros + 1
librero[2] = Libro("Don Quijote", 103, "Miguel de Cervantes", "Alfaguara")
total_libros = total_libros + 1
librero[3] = Libro("Harry Potter", 104, "J.K. Rowling", "Salamandra")
total_libros = total_libros + 1
librero[4] = Libro("Steve Jobs", 105, "Walter Isaacson", "Debate")
total_libros = total_libros + 1

print("Sistema iniciado ", total_libros, "libros cargados correctamente.")


# ==========================================
# BLOQUE 2: AGREGAR NUEVOS LIBROS
# ==========================================

print("Cuántos libros nuevos deseas agregar?")
n = int(input())

for k in range(n):
    print( "Capturando Libro Nuevo", k+1)
    
    if total_libros >= MAX_CAPACIDAD:
        print("Error: El librero está lleno.")

    print("Introduce el código numérico:")
    new_cod = int(input())

     # Validación de código único
    repetido = False
    for i in range(total_libros):
        if librero[i].getCodigo() == new_cod:
            repetido = True

    if repetido==True:
        print("¡ERROR! Ese código ya existe. No se guardará.")
    else:
        print("Introduce el Título:")
        tit = input()
        print("Introduce el Autor:")
        aut = input()
        print("Introduce la Editorial:")
        edi = input()

        nuevo_libro = Libro(tit, new_cod, aut, edi)
        librero[total_libros] = nuevo_libro
        total_libros =total_libros + 1
        print("Libro guardado...")


# ==========================================
# BLOQUE 3: MENÚ PRINCIPAL
# ==========================================

opcion = ""

while opcion != "10":
    print("--- GESTIÓN DE BIBLIOTECA ---")
    print("1. Mostrar libros")
    print("2. Buscar libro por autor")
    print("3. Dar de baja un libro")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Mostrar historial de préstamos")
    print("7. Ver libros DISPONIBLES (Extra)")
    print("8. Corregir fecha de préstamo")
    print("9. Agregar un libro nuevo (extra)" ) 
    print("10. Salir")
    
    opcion = input("Elige una opción (número): ")

    opcionValida = False

    # 1. MOSTRAR LIBROS
    if opcion == "1":
        opcionValida = True
        if total_libros == 0:
            print("Librero vacío.")
        else:
            print("LISTADO DE", total_libros, "LIBROS")
            for i in range(total_libros):
                librero[i].mostrarAtrib()
                print("-------------------------")

    # 2. BUSCAR POR AUTOR
    if opcion == "2":
        opcionValida = True
        print("Introduce el nombre (o parte) del autor:")
        busqueda = input()
        encontrado = False
        for i in range(total_libros):
            if librero[i].verificarAutor(busqueda):
                librero[i].mostrarAtrib()
                print("-------------------------")
                encontrado = True
        if encontrado == False:
            print("No se encontraron coincidencias.")

    # 3. DAR DE BAJA
    if opcion == "3":
        opcionValida = True
        print("Introduce el CÓDIGO del libro a borrar:")
        cod_borrar = int(input())
        posicion = -1
        
        for i in range(total_libros):
            if librero[i].getCodigo() == cod_borrar:
                posicion = i
        
        if posicion != -1:
            print("Eliminando:", librero[posicion].getTitulo())
            for j in range(posicion, total_libros - 1):
                librero[j] = librero[j+1]
            librero[total_libros - 1] = None
            total_libros = total_libros - 1
            print("Libro eliminado.")
        else:
            print("Error: Código no encontrado.")

    # 4. REGISTRAR PRÉSTAMO
    if opcion == "4":
        opcionValida = True
        if total_prestamos >= MAX_CAPACIDAD:
            print("Error: Memoria llena.")
        else:
            print("Código del libro a prestar:")
            cod = int(input())
            existe = False
            
            for i in range(total_libros):
                if librero[i].getCodigo() == cod:
                    existe = True
                    print("Libro:", librero[i].getTitulo())
            
            if existe == True:
                print("Nombre del alumno:")
                alumno = input()
                print("Fecha (dd/mm/aaaa):")
                fecha = input()
                
                temp = Prestamo(0, "", "")
                if temp.validarFecha(fecha):
                    nuevo_p = Prestamo(cod, alumno, fecha)
                    prestamos[total_prestamos] = nuevo_p
                    total_prestamos = total_prestamos + 1
                    print("Préstamo registrado.")
                else:
                    print("Fecha inválida.")
            else:
                print("Libro no encontrado.")

    # 5. DEVOLUCIÓN
    if opcion == "5":
        opcionValida = True
        print("Código del libro devuelto:")
        cod = int(input())
        encontrado = False
        
        for i in range(total_prestamos):
            p_actual = prestamos[i]
            if p_actual.getCodPedido() == cod and p_actual.getFechaDevolucion() == "Pendiente":
                print("Alumno:", p_actual.getNombAlumno())
                print("Fecha devolución (dd/mm/aaaa):")
                f_dev = input()
                
                if p_actual.validarFecha(f_dev):
                    p_actual.setFechaDevolucion(f_dev)
                    print("Devolución registrada.")
                    encontrado = True
                else:
                    print("Fecha inválida.")
        
        if encontrado == False:
            print("No hay préstamo pendiente para ese libro.")

    # 6. HISTORIAL
    if opcion == "6":
        opcionValida = True
        if total_prestamos == 0:
            print("No hay historial.")
        else:
            print("--- HISTORIAL", total_prestamos, "REGISTROS ---")
            for i in range(total_prestamos):
                prestamos[i].mostrarObj()
                print("-----------------")

    # 7. LIBROS DISPONIBLES
    if opcion == "7":
        opcionValida = True
        print("--- LIBROS DISPONIBLES ---")
        for i in range(total_libros):
            cod_actual = librero[i].getCodigo()
            esta_prestado = False
            for k in range(total_prestamos):
                if prestamos[k].getCodPedido() == cod_actual and prestamos[k].getFechaDevolucion() == "Pendiente":
                    esta_prestado = True

            if esta_prestado == False:
                print(librero[i].getTitulo(), "Cod:", cod_actual)

    # 8. CORREGIR FECHA
    if opcion == "8":
        opcionValida = True
        print("Ingrese el CÓDIGO del libro del préstamo a corregir:")
        cod = int(input())
        encontrado = False

        for i in range(total_prestamos):
            if prestamos[i].getCodPedido() == cod and prestamos[i].getFechaDevolucion() == "Pendiente":
                print("Préstamo encontrado. Alumno:", prestamos[i].getNombAlumno())
                print("Fecha actual registrada:", prestamos[i].fecha)
                prestamos[i].corregirFechaPrestamo()
                encontrado = True
        
        if encontrado == False:
            print("No se encontró un préstamo activo con ese código.")
            
    # 9. AGREGAR NUEVO LIBRO
    if opcion == "9":
        opcionValida = True
        if total_libros >= MAX_CAPACIDAD:
            print("Error: El librero está lleno.")
        else:
            print("--- ALTA DE LIBRO ---")
            print("Introduce el código numérico:")
            cod_str = input()
            
            if cod_str.isdigit(): 
                new_cod = int(cod_str)
                repetido = False
                
                for i in range(total_libros):
                    if librero[i].getCodigo() == new_cod:
                        repetido = True
                
                if repetido == True:
                    print("¡ERROR! Ya existe un libro con ese código.")
                else:
                    print("Introduce el Título:")
                    tit = input()
                    print("Introduce el Autor:")
                    aut = input()
                    print("Introduce la Editorial:")
                    edi = input()

                    nuevo_libro = Libro(tit, new_cod, aut, edi)
                    librero[total_libros] = nuevo_libro
                    total_libros = total_libros + 1
                    print("Libro agregado exitosamente.")
            else:
                print("Error: El código debe ser un número.")

    # 10. SALIR
    if opcion == "10":
        opcionValida = True
        print("Saliendo...")
    
    if opcionValida == False:
        print("Opción no válida, intente de nuevo con un número del 1 al 10.")
