
# ----------------- CLASE LIBRO (Se mantiene para encapsular datos) -----------------

class Libro:
    """Representa un libro en el librero."""
    
    def __init__(self, codigo, titulo, autores_str, editorial="Desconocida", edicion=1):
        self._codigo = codigo       
        self._titulo = titulo       
        # Almacenamos autores separados por comas
        self._autores_str = autores_str 
        self.__editorial = editorial 
        self._edicion = edicion
        
    def mostrar_info(self):
        """Muestra la información completa del libro."""
        print("-" * 40)
        print(f"Código: {self._codigo}")
        print(f"Título: {self._titulo}")
        print(f"Autores: {self._autores_str}")
        print(f"Editorial: {self.__editorial}")
        print(f"Edición: {self._edicion}")
        print("-" * 40)

    # El método de búsqueda simplificado usará el operador 'in' para cumplir con la necesidad funcional
    def buscar_autor_parcial(self, busqueda):
        """Verifica si la cadena de búsqueda coincide parcialmente con alguno de los autores."""
        busqueda_lower = busqueda.strip().lower()
        return busqueda_lower in self._autores_str.lower()
        
    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self._titulo

# ----------------- CLASE PRÉSTAMO (Se mantiene para encapsular datos) -----------------

class Prestamo:
    """Representa un registro de préstamo de un libro a un alumno."""
    
    def __init__(self, codigo_libro, nombre_alumno, fecha_prestamo):
        self._codigo_libro = codigo_libro      
        self._nombre_alumno = nombre_alumno    
        self._fecha_prestamo = fecha_prestamo  
        self._fecha_regreso = "PENDIENTE"      

    def mostrar_datos(self):
        """Muestra la información del registro de préstamo."""
        estado = "DEVUELTO"
        if self._fecha_regreso == "PENDIENTE":
            estado = "EN PRÉSTAMO"
            
        print(f"  > Libro (Cod: {self._codigo_libro}) prestado a {self._nombre_alumno}")
        print(f"  > Fecha de Préstamo: {self._fecha_prestamo}")
        print(f"  > Fecha de Devolución: {self._fecha_regreso}")
        print(f"  > ESTADO: **{estado}**")

    # Validación de fecha solo con if/else para cumplir la restricción
    def validar_formato_fecha(self, fecha):
        """Valida que la fecha tenga el formato dd/mm/2023 usando solo if/else."""
        
        if len(fecha) != 10:
            return False
            
        if fecha[2] != '/' or fecha[5] != '/':
            return False
            
        # Simplificación: Asumimos que si tiene el formato, el usuario ingresa números válidos,
        # pero revisamos que sean dígitos donde deben ir.
        i = 0
        while i < len(fecha):
            if i != 2 and i != 5:
                if not fecha[i].isdigit():
                    return False
            i += 1
            
        # Verificación de rangos (usando int() para obtener el valor)
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        anio = int(fecha[6:10])
        
        if not (1 <= dia <= 31):
            return False
        if not (1 <= mes <= 12):
            return False
        if anio != 2025:
            return False
            
        return True

    def get_codigo_libro(self):
        return self._codigo_libro
        
    def esta_en_prestamo(self):
        return self._fecha_regreso == "PENDIENTE"
        
# ----------------- PROGRAMA PRINCIPAL CLÁSICO Y SIMPLE -----------------

# 5) Librero y 6) 5 libros fijos
librero = [
    Libro(101, "Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 2),
    Libro(102, "El Principito", "Antoine de Saint-Exupéry", "Salamandra", 5),
    Libro(103, "Don Quijote de la Mancha", "Miguel de Cervantes", "Vicens Vives", 3),
    Libro(104, "Orgullo y Prejuicio", "Jane Austen", "Penguin Classics", 1),
    Libro(105, "Fundamentos de Python", "Alfredo Sánchez, Laura Gómez", "Alfaomega", 4),
]

# 8) Arreglo de préstamos
prestamos = []

print("\n--- INICIO DEL PROGRAMA: Carga Inicial ---")

# 7) Preguntar al usuario cuantos libros más quiere dar de alta
cantidad_extra_str = input("¿Cuántos libros adicionales desea dar de alta? ")

if cantidad_extra_str.isdigit():
    cantidad_extra = int(cantidad_extra_str)
    
    i = 0
    while i < cantidad_extra:
        print(f"\n- Libro adicional #{i+1} -")
        
        codigo_valido = False
        nuevo_codigo = 0
        
        # Bucle para validar el código y la unicidad
        while not codigo_valido:
            codigo_str = input("Ingrese el CÓDIGO del libro (numérico): ")
            
            if codigo_str.isdigit():
                nuevo_codigo = int(codigo_str)
                
                # Verificar unicidad
                codigo_existe = False
                j = 0
                while j < len(librero):
                    if librero[j].get_codigo() == nuevo_codigo:
                        codigo_existe = True
                        break
                    j += 1
                        
                if codigo_existe:
                    print("❌ ERROR: El código ya existe. Intente con otro.")
                else:
                    codigo_valido = True
            else:
                print("❌ ERROR: El código debe ser un número entero.")
        
        nuevo_titulo = input("Ingrese el TÍTULO: ")
        nuevo_autores = input("Ingrese los AUTORES (separados por coma): ")
        nueva_editorial = input("Ingrese la EDITORIAL: ")
        
        nueva_edicion_str = input("Ingrese la EDICIÓN (numérica, opcional): ")
        nueva_edicion = 1
        if nueva_edicion_str.isdigit():
            nueva_edicion = int(nueva_edicion_str)
            
        nuevo_libro = Libro(nuevo_codigo, nuevo_titulo, nuevo_autores, nueva_editorial, nueva_edicion)
        librero.append(nuevo_libro)
        i += 1
        
    print("✅ Libros adicionales cargados.")
else:
    print("ℹ️ Entrada no válida. No se cargaron libros adicionales.")


# 9) Menú de Opciones
opcion = ''
while opcion != '0':
    print("\n" + "=" * 50)
    print("      SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 50)
    print("a) Mostrar la información de los libros (Librero)")
    print("b) Buscar un libro por autor (Búsqueda parcial)")
    print("c) Dar de baja un libro (por código)")
    print("d) Registrar un préstamo")
    print("e) Registrar devolución de un libro")
    print("f) Mostrar el historial de préstamos")
    print("g) EXTRA: Mostrar libros prestados actualmente")
    print("0) Salir del programa")
    print("-" * 50)
    
    opcion = input("Seleccione una opción: ").lower()
    
    # ------------------ a) MOSTRAR LIBROS ------------------
    if opcion == 'a':
        print("\n### LISTA COMPLETA DE LIBROS ###")
        i = 0
        while i < len(librero):
            librero[i].mostrar_info()
            i += 1
            
    # ------------------ b) BUSCAR LIBRO POR AUTOR (PARCIAL) ------------------
    elif opcion == 'b':
        criterio = input("Ingrese el nombre o parte del nombre del autor a buscar: ")
        encontrado = False
        print(f"\n### RESULTADOS DE BÚSQUEDA PARA '{criterio}' ###")
        
        i = 0
        while i < len(librero):
            if librero[i].buscar_autor_parcial(criterio):
                librero[i].mostrar_info()
                encontrado = True
            i += 1
            
        if not encontrado:
            print("❌ Lo siento, no se encontró ningún libro con ese autor.")

    # ------------------ c) DAR DE BAJA UN LIBRO ------------------
    elif opcion == 'c':
        codigo_baja_str = input("Ingrese el CÓDIGO del libro a dar de baja: ")
        
        if codigo_baja_str.isdigit():
            codigo_baja = int(codigo_baja_str)
            
            # Buscar el libro y obtener su índice
            libro_a_borrar_indice = -1
            i = 0
            while i < len(librero):
                if librero[i].get_codigo() == codigo_baja:
                    libro_a_borrar_indice = i
                    break
                i += 1
                    
            if libro_a_borrar_indice != -1:
                # Obtenemos el título antes de borrar
                titulo_borrado = librero[libro_a_borrar_indice].get_titulo() 
                
                # Borrarlo (usamos la función .pop() que es simple y nativa)
                librero.pop(libro_a_borrar_indice) 
                print(f"✅ Libro (Cód: {codigo_baja}, Título: '{titulo_borrado}') dado de baja del librero.")
            else:
                print(f"❌ No se encontró un libro con el código {codigo_baja}.")
        else:
            print("❌ Por favor, ingrese un código numérico.")
            
    # ------------------ d) REGISTRAR UN PRÉSTAMO ------------------
    elif opcion == 'd':
        codigo_prestamo_str = input("Ingrese el CÓDIGO del libro a prestar: ")
        
        if not codigo_prestamo_str.isdigit():
            print("❌ ERROR: El código de libro debe ser numérico.")
            continue
            
        codigo_prestamo = int(codigo_prestamo_str)

        # Buscar el libro
        libro_a_prestar = None
        i = 0
        while i < len(librero):
            if librero[i].get_codigo() == codigo_prestamo:
                libro_a_prestar = librero[i]
                break
            i += 1
        
        if libro_a_prestar is None:
            print("❌ ERROR: El código de libro no existe en el librero.")
            continue

        # Validación: Verificar si el libro YA está en préstamo (Bucle simple)
        en_prestamo_actual = False
        i = 0
        while i < len(prestamos):
            p = prestamos[i]
            if p.get_codigo_libro() == codigo_prestamo and p.esta_en_prestamo():
                print("⚠️ ATENCIÓN: Este libro ya se encuentra en préstamo.")
                en_prestamo_actual = True
                break
            i += 1
        if en_prestamo_actual:
            continue

        nombre_alumno = input("Ingrese el NOMBRE del alumno: ")
        
        # Validación de fecha de préstamo
        p_temporal = Prestamo(0, "", "") # Objeto temporal para validación
        fecha_valida = False
        fecha_prestamo = ""
        while not fecha_valida:
            fecha_prestamo = input("Ingrese la FECHA de préstamo (dd/mm/2025): ")
            if p_temporal.validar_formato_fecha(fecha_prestamo):
                fecha_valida = True
            else:
                print("❌ ERROR: Formato de fecha incorrecto. Debe ser dd/mm/2025 .")

        nuevo_prestamo = Prestamo(codigo_prestamo, nombre_alumno, fecha_prestamo)
        prestamos.append(nuevo_prestamo)
        print(f"✅ Préstamo del libro '{libro_a_prestar.get_titulo()}' registrado con éxito.")

    # ------------------ e) REGISTRAR DEVOLUCIÓN ------------------
    elif opcion == 'e':
        codigo_devolver_str = input("Ingrese el CÓDIGO del libro devuelto: ")
        
        if not codigo_devolver_str.isdigit():
            print("❌ ERROR: El código de libro debe ser numérico.")
            continue
            
        codigo_devolver = int(codigo_devolver_str)
        
        # Buscar el préstamo ACTIVO más reciente
        prestamo_activo = None
        
        # Recorrer la lista al revés para obtener el más reciente (simulación de 'reversed' con índice)
        i = len(prestamos) - 1
        while i >= 0:
            p = prestamos[i]
            if p.get_codigo_libro() == codigo_devolver and p.esta_en_prestamo():
                prestamo_activo = p
                break
            i -= 1
                
        if prestamo_activo is None:
            print("❌ ERROR: No se encontró un préstamo activo (pendiente de devolución) para ese código de libro.")
            continue
            
        # Validación de la fecha de devolución
        fecha_devolucion_valida = False
        while not fecha_devolucion_valida:
            fecha_devolucion = input("Ingrese la FECHA de devolución (dd/mm/2023): ")
            if prestamo_activo.validar_formato_fecha(fecha_devolucion):
                prestamo_activo._fecha_regreso = fecha_devolucion
                print("✅ Devolución registrada con éxito.")
                fecha_devolucion_valida = True
            else:
                print("❌ La fecha de devolución no es válida (dd/mm/2023).")
        
    # ------------------ f) MOSTRAR HISTORIAL DE PRÉSTAMOS ------------------
    elif opcion == 'f':
        if len(prestamos) == 0:
            print("ℹ️ No hay registros de préstamos.")
        else:
            print("\n### HISTORIAL COMPLETO DE PRÉSTAMOS ###")
            i = 0
            while i < len(prestamos):
                p = prestamos[i]
                print(f"\n--- Préstamo #{i+1} ---")
                p.mostrar_datos()
                i += 1

    # ------------------ g) EXTRA: LIBROS PRESTADOS ACTUALMENTE ------------------
    elif opcion == 'g':
        libros_prestados = []
        i = 0
        while i < len(prestamos):
            if prestamos[i].esta_en_prestamo():
                libros_prestados.append(prestamos[i])
            i += 1
        
        if len(libros_prestados) == 0:
            print("✅ Actualmente NO hay libros en préstamo.")
        else:
            print("\n### LIBROS ACTUALMENTE EN PRÉSTAMO ###")
            i = 0
            while i < len(libros_prestados):
                p = libros_prestados[i]
                
                # Buscar el título del libro
                libro = None
                j = 0
                while j < len(librero):
                    if librero[j].get_codigo() == p.get_codigo_libro():
                        libro = librero[j]
                        break
                    j += 1
                        
                titulo = "Libro Desconocido"
                if libro:
                    titulo = libro.get_titulo()
                
                print(f"- **{titulo}** (Cód: {p.get_codigo_libro()})")
                print(f"  Prestado a: {p._nombre_alumno} | Fecha: {p._fecha_prestamo}")
                i += 1

    # ------------------ 0) SALIR ------------------
    elif opcion == '0':
        print("👋 Saliendo del programa. ¡Hasta luego!")
        # El bucle `while opcion != '0'` se encargará de salir.
        
    # ------------------ OPCIÓN INVÁLIDA ------------------
    else:
        print("⚠️ Opción no válida. Intente de nuevo.")