# ----------------- CLASE LIBRO (Sin Cambios) -----------------

class Libro:
    """Representa un libro en el librero."""
    
    def __init__(self, codigo, titulo, autores_str, editorial="Desconocida", edicion=1):
        self._codigo = codigo       
        self._titulo = titulo       
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

    # ----------------------------------------------------
    # --- FUNCIONES DE UTILIDAD (Programación Básica) ---
    # ----------------------------------------------------

    def _to_lower_manual(self, cadena):
        """
        Convierte una cadena a minúsculas manualmente (COMPLETA).
        """
        resultado = ""
        i = 0
        while i < len(cadena):
            caracter = cadena[i]
            
            # Lógica de conversión (completa para evitar errores de sintaxis)
            if caracter == 'A':
                caracter = 'a'
            elif caracter == 'B':
                caracter = 'b'
            elif caracter == 'C':
                caracter = 'c'
            elif caracter == 'D':
                caracter = 'd'
            elif caracter == 'E':
                caracter = 'e'
            elif caracter == 'F':
                caracter = 'f'
            elif caracter == 'G':
                caracter = 'g'
            elif caracter == 'H':
                caracter = 'h'
            elif caracter == 'I':
                caracter = 'i'
            elif caracter == 'J':
                caracter = 'j'
            elif caracter == 'K':
                caracter = 'k'
            elif caracter == 'L':
                caracter = 'l'
            elif caracter == 'M':
                caracter = 'm'
            elif caracter == 'N':
                caracter = 'n'
            elif caracter == 'O':
                caracter = 'o'
            elif caracter == 'P':
                caracter = 'p'
            elif caracter == 'Q':
                caracter = 'q'
            elif caracter == 'R':
                caracter = 'r'
            elif caracter == 'S':
                caracter = 's'
            elif caracter == 'T':
                caracter = 't'
            elif caracter == 'U':
                caracter = 'u'
            elif caracter == 'V':
                caracter = 'v'
            elif caracter == 'W':
                caracter = 'w'
            elif caracter == 'X':
                caracter = 'x'
            elif caracter == 'Y':
                caracter = 'y'
            elif caracter == 'Z':
                caracter = 'z'
                
            resultado += caracter
            i += 1
        return resultado
        
    def _strip_manual(self, cadena):
        """Elimina espacios al inicio y al final de una cadena (sin .strip() ni slicing)."""
        
        inicio = 0
        while inicio < len(cadena) and cadena[inicio] == ' ':
            inicio += 1
            
        if inicio == len(cadena):
            return ""
            
        final = len(cadena) - 1
        while final > inicio and cadena[final] == ' ':
            final -= 1
            
        resultado = ""
        i = inicio
        while i <= final:
            resultado += cadena[i]
            i += 1
            
        return resultado

    def _manual_substring_search(self, texto, subcadena):
        
        len_texto = len(texto)
        len_subcadena = len(subcadena)
        
        if len_subcadena == 0 or len_subcadena > len_texto:
            return False
            
        i = 0
        while i <= len_texto - len_subcadena:
            es_match = True
            j = 0
            while j < len_subcadena:
                if texto[i + j] != subcadena[j]:
                    es_match = False
                    break
                j += 1
            
            if es_match:
                return True
            
            i += 1
            
        return False
    
    # ----------------------------------------------------
    # --- MÉTODOS DE BÚSQUEDA (Sin Cambios) ---
    # ----------------------------------------------------

    def buscar_autor_parcial(self, busqueda):
        busqueda_limpia = self._strip_manual(busqueda)
        busqueda_norm = self._to_lower_manual(busqueda_limpia)
        autores_norm = self._to_lower_manual(self._autores_str)
        return self._manual_substring_search(autores_norm, busqueda_norm)

    def buscar_titulo_parcial_manual(self, criterio):
        criterio_limpio = self._strip_manual(criterio)
        criterio_norm = self._to_lower_manual(criterio_limpio)
        titulo_norm = self._to_lower_manual(self._titulo)
        return self._manual_substring_search(titulo_norm, criterio_norm)

    # ----------------------------------------------------
    # --- Getters (Sin Cambios) ---
    # ----------------------------------------------------
    
    def get_codigo(self):
        return self._codigo

    def get_titulo(self):
        return self._titulo

# ----------------- CLASE PRÉSTAMO (Con Validaciones COMPLETAS) -----------------

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
            
        print(f"   > Libro (Cod: {self._codigo_libro}) prestado a {self._nombre_alumno}")
        print(f"   > Fecha de Préstamo: {self._fecha_prestamo}")
        print(f"   > Fecha de Devolución: {self._fecha_regreso}")
        print(f"   > ESTADO: **{estado}**")

    # 🟢 FUNCIÓN DE UTILIDAD: Sustituye .isdigit()
    def _manual_isdigit(self, caracter):
        """
        Verifica si un carácter individual es un dígito (0-9).
        """
        if caracter == '0' or \
           caracter == '1' or \
           caracter == '2' or \
           caracter == '3' or \
           caracter == '4' or \
           caracter == '5' or \
           caracter == '6' or \
           caracter == '7' or \
           caracter == '8' or \
           caracter == '9':
            return True
        else:
            return False

    # ----------------------------------------------------
    # --- MÉTODOS AUXILIARES DE FECHA (NUEVOS) ---
    # ----------------------------------------------------

    def _es_bisiesto(self, anio):
        """Determina si un año es bisiesto. Asume el año > 1582."""
        # Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
        
        # Lógica sin usar 'and', 'or', 'not' directamente, solo comparaciones.
        # Devuelve True (1) o False (0).
        es_divisible_por_4 = (anio % 4 == 0)
        es_divisible_por_100 = (anio % 100 == 0)
        es_divisible_por_400 = (anio % 400 == 0)
        
        # Implementando: (A % 4 == 0 AND A % 100 != 0) OR (A % 400 == 0)
        
        caso1 = False
        if es_divisible_por_4:
            if es_divisible_por_100 == False: # A % 100 != 0
                caso1 = True
                
        caso2 = False
        if es_divisible_por_400:
            caso2 = True
            
        if caso1:
            return True
        
        if caso2:
            return True
            
        return False


    def _dias_en_mes(self, mes, anio):
        """Devuelve el número máximo de días en un mes específico para un año dado."""
        
        # Meses de 31 días: 1, 3, 5, 7, 8, 10, 12
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return 31
            
        # Meses de 30 días: 4, 6, 9, 11
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            return 30
            
        # Febrero (2)
        if mes == 2:
            if self._es_bisiesto(anio):
                return 29
            else:
                return 28
                
        # Caso de error (si el mes no es válido, aunque se valida antes)
        return 0 
        
    def _parse_fecha(self, fecha_str):
        """Convierte 'dd/mm/aaaa' en una tupla (aaaa, mm, dd) para comparación."""
        # Asume que la fecha ya pasó la validación de formato dd/mm/aaaa.
        d = int(fecha_str[0:2])
        m = int(fecha_str[3:5])
        a = int(fecha_str[6:10])
        return (a, m, d)


    # ----------------------------------------------------
    # --- MÉTODOS DE VALIDACIÓN DE FECHA (ACTUALIZADOS) ---
    # ----------------------------------------------------

    def validar_formato_fecha(self, fecha):
        """
        Valida que la fecha tenga el formato dd/mm/aaaa Y la coherencia de días/mes.
        Devuelve True si es válida, de lo contrario devuelve el mensaje de error.
        """
        
        if len(fecha) != 10:
            return "El formato de fecha debe ser dd/mm/aaaa (10 caracteres)."
            
        if fecha[2] != '/' or fecha[5] != '/':
            return "Los separadores deben ser '/' en las posiciones 3 y 6."
            
        # Revisamos que sean dígitos donde deben ir
        i = 0
        while i < len(fecha):
            if i != 2 and i != 5:
                if self._manual_isdigit(fecha[i]) == False: 
                    return "Día, Mes y Año deben contener solo números."
            i += 1 
            
        # Extracción y conversión a enteros
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        anio = int(fecha[6:10])
        
        # Validación de Rangos
        if (1 <= mes <= 12) == False:
            return "El mes debe estar entre 01 y 12."
            
        # Validación de Días por Mes
        max_dias = self._dias_en_mes(mes, anio)
        if (1 <= dia <= max_dias) == False:
            # Construcción de mensaje de error detallado
            msg = "El día es inválido. "
            if mes == 2:
                if self._es_bisiesto(anio):
                    msg = "Febrero en año bisiesto (29 días)."
                else:
                    msg = "Febrero en año no bisiesto (28 días)."
            elif max_dias == 30:
                msg = "Mes de 30 días (Abril, Junio, Septiembre, Noviembre)."
            else:
                msg = "Mes de 31 días."

            return f"El día ingresado ({dia}) excede el límite de {max_dias} para el mes {mes}. ({msg})"

        # Si todo es válido
        return True


    def validar_fecha_devolucion(self, fecha_prestamo_str, fecha_devolucion_str):
        """
        Valida que la fecha de devolución sea posterior o igual a la de préstamo.
        """
        fecha_prestamo_tuple = self._parse_fecha(fecha_prestamo_str)
        fecha_devolucion_tuple = self._parse_fecha(fecha_devolucion_str)
        
        # Comparación de tuplas (Año, Mes, Día)
        # Si la fecha de devolución es MENOR a la de préstamo, es inválida.
        devolucion_es_anterior = False
        if fecha_devolucion_tuple < fecha_prestamo_tuple:
            devolucion_es_anterior = True
            
        if devolucion_es_anterior:
            return f"La fecha de devolución ({fecha_devolucion_str}) no puede ser anterior a la de préstamo ({fecha_prestamo_str})."
        else:
            return True


    def get_codigo_libro(self):
        return self._codigo_libro
        
    def esta_en_prestamo(self):
        return self._fecha_regreso == "PENDIENTE"
        
# ----------------- PROGRAMA PRINCIPAL CLÁSICO Y SIMPLE (AJUSTADO) -----------------

# ... (El código de inicialización de librero y la carga extra de libros no ha cambiado) ...

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

validador_principal = Prestamo(0, "", "")

print("\n--- INICIO DEL PROGRAMA: Carga Inicial ---")


cantidad_extra_str = input("¿Cuántos libros adicionales desea dar de alta? ")


es_digito_cantidad_extra = True
i = 0
while i < len(cantidad_extra_str):
    if validador_principal._manual_isdigit(cantidad_extra_str[i]) == False:
        es_digito_cantidad_extra = False
        break
    i += 1

if es_digito_cantidad_extra:
    cantidad_extra = int(cantidad_extra_str)
    
    i = 0
    while i < cantidad_extra:
        print(f"\n- Libro adicional #{i+1} -")
        
        codigo_valido = False
        nuevo_codigo = 0
        
        while codigo_valido == False: 
            codigo_str = input("Ingrese el CÓDIGO del libro (numérico): ")
            
            # Sustitución de .isdigit()
            es_digito_codigo = True
            j = 0
            while j < len(codigo_str):
                if validador_principal._manual_isdigit(codigo_str[j]) == False:
                    es_digito_codigo = False
                    break
                j += 1
            
            if es_digito_codigo:
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
        
    
        es_digito_edicion = True
        k = 0
        while k < len(nueva_edicion_str):
            if validador_principal._manual_isdigit(nueva_edicion_str[k]) == False:
                es_digito_edicion = False
                break
            k += 1

        nueva_edicion = 1
        if es_digito_edicion and len(nueva_edicion_str) > 0: 
            nueva_edicion = int(nueva_edicion_str)
            
        nuevo_libro = Libro(nuevo_codigo, nuevo_titulo, nuevo_autores, nueva_editorial, nueva_edicion)
        librero = librero + [nuevo_libro]
        i += 1
        
    print("✅ Libros adicionales cargados.")
else:
    print("ℹ️ Entrada no válida. No se cargaron libros adicionales.")


# 9) Menú de Opciones
opcion = ''

if len(librero) > 0:
    conversor_lower = librero[0]
else:
    conversor_lower = Libro(0, "Temp", "Temp")
while opcion != '0':
    print("\n" + "=" * 50)
    print("           SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=" * 50)
    print("a) Mostrar la información de los libros (Librero)")
    print("b) Buscar un libro por autor (Búsqueda parcial, MANUAL)")
    print("c) Buscar un libro por título (Búsqueda parcial, MANUAL) 💡 NUEVO")
    print("d) Dar de baja un libro (por código)")
    print("e) Registrar un préstamo")
    print("f) Registrar devolución de un libro")
    print("g) Mostrar el historial de préstamos")
    print("h) EXTRA: Mostrar libros prestados actualmente")
    print("0) Salir del programa")
    print("-" * 50)
    
    entrada_usuario = input("Seleccione una opcion: ")
    opcion = conversor_lower._to_lower_manual(entrada_usuario)
    
    # ------------------ a) MOSTRAR LIBROS ------------------
    if opcion == 'a':
        print("\n📚 Listado Completo de Libros en el Librero:")
        hay_libros = False
        i = 0
        while i < len(librero):
            librero[i].mostrar_info()
            hay_libros = True
            i += 1
            
        if hay_libros == False:
            print("⚠️ El librero está vacío.")
        
    # ------------------ b) BUSCAR LIBRO POR AUTOR (PARCIAL) ------------------
    elif opcion == 'b':
        criterio_busqueda = input("Ingrese el nombre/apellido/parte del autor a buscar: ")
        print(f"\n🔍 Resultados de la búsqueda por Autor ('{criterio_busqueda}'):")
        
        encontrados = False
        i = 0
        while i < len(librero):
            if librero[i].buscar_autor_parcial(criterio_busqueda):
                librero[i].mostrar_info()
                encontrados = True
            i += 1
            
        if encontrados == False:
            print("❌ No se encontraron libros con ese autor.")
            
    # ------------------ c) BUSCAR LIBRO POR TÍTULO (PARCIAL MANUAL)  ------------------
    elif opcion == 'c':
        criterio_busqueda = input("Ingrese una palabra clave del título a buscar: ")
        print(f"\n🔍 Resultados de la búsqueda por Título ('{criterio_busqueda}'):")
        
        encontrados = False
        i = 0
        while i < len(librero):
            if librero[i].buscar_titulo_parcial_manual(criterio_busqueda):
                librero[i].mostrar_info()
                encontrados = True
            i += 1
            
        if encontrados == False:
            print("❌ No se encontraron libros con ese título.")

    # ------------------ d) DAR DE BAJA UN LIBRO ------------------
    elif opcion == 'd':
        codigo_baja_str = input("Ingrese el CÓDIGO del libro a dar de baja: ")
        
        
        es_digito_baja = True
        i = 0
        while i < len(codigo_baja_str):
            if validador_principal._manual_isdigit(codigo_baja_str[i]) == False:
                es_digito_baja = False
                break
            i += 1
            
        
        if es_digito_baja:
            codigo_baja = int(codigo_baja_str)
            
            libro_a_borrar_indice = -1
            i = 0
            while i < len(librero):
                if librero[i].get_codigo() == codigo_baja:
                    libro_a_borrar_indice = i
                    break
                i += 1
                        
            if libro_a_borrar_indice != -1:
                titulo_borrado = librero[libro_a_borrar_indice].get_titulo() 
                
                librero.pop(libro_a_borrar_indice) 
                print(f"✅ Libro (Cód: {codigo_baja}, Título: '{titulo_borrado}') dado de baja del librero.")
            else:
                print(f"❌ No se encontró un libro con el código {codigo_baja}.")
        else:
            print("❌ Por favor, ingrese un código numérico.")
            
    # ------------------ e) REGISTRAR UN PRÉSTAMO (VALIDACIÓN COMPLETA) ------------------
    elif opcion == 'e':
        codigo_prestamo_str = input("Ingrese el CÓDIGO del libro a prestar: ")
        
        # Sustitución de .isdigit()
        es_digito_prestamo = True
        i = 0
        while i < len(codigo_prestamo_str):
            if validador_principal._manual_isdigit(codigo_prestamo_str[i]) == False:
                es_digito_prestamo = False
                break
            i += 1

        if es_digito_prestamo == False:
            print("❌ ERROR: El código de libro debe ser numérico.")
            
        else: 
            codigo_prestamo = int(codigo_prestamo_str)

            # Buscar el libro (código existente)
            libro_a_prestar = None
            i = 0
            while i < len(librero):
                if librero[i].get_codigo() == codigo_prestamo:
                    libro_a_prestar = librero[i]
                    break
                i += 1
            
            if libro_a_prestar is None:
                print("❌ ERROR: El código de libro no existe en el librero.")
                
            else: 
                
                en_prestamo_actual = False
                i = 0
                while i < len(prestamos):
                    p = prestamos[i]
                    if p.get_codigo_libro() == codigo_prestamo and p.esta_en_prestamo():
                        print("⚠️ ATENCIÓN: Este libro ya se encuentra en préstamo.")
                        en_prestamo_actual = True
                        break
                    i += 1
                
                
                if en_prestamo_actual == False:
                    nombre_alumno = input("Ingrese el NOMBRE del alumno: ")
                    
                    
                    p_temporal = Prestamo(0, "", "") 
                    fecha_valida = False
                    fecha_prestamo = ""
                    while fecha_valida == False: 
                        fecha_prestamo = input("Ingrese la FECHA de préstamo (dd/mm/aaaa): ")
                        
                        resultado_validacion = p_temporal.validar_formato_fecha(fecha_prestamo)
                        
                        if resultado_validacion is True: # Es la forma de preguntar si devolvió True o un string de error.
                            fecha_valida = True
                        else:
                            print(f"❌ ERROR: {resultado_validacion}")

                    nuevo_prestamo = Prestamo(codigo_prestamo, nombre_alumno, fecha_prestamo)
                    prestamos.append(nuevo_prestamo)
                    print(f"✅ Préstamo del libro '{libro_a_prestar.get_titulo()}' registrado con éxito el {fecha_prestamo}.")

    # ------------------ f) REGISTRAR DEVOLUCIÓN (VALIDACIÓN COMPLETA) ------------------
    elif opcion == 'f':
        codigo_devolver_str = input("Ingrese el CÓDIGO del libro devuelto: ")
        
        
        es_digito_devolver = True
        i = 0
        while i < len(codigo_devolver_str):
            if validador_principal._manual_isdigit(codigo_devolver_str[i]) == False:
                es_digito_devolver = False
                break
            i += 1
            
        
        if es_digito_devolver == False:
            print("❌ ERROR: El código de libro debe ser numérico.")
        else:
            codigo_devolver = int(codigo_devolver_str)
            
            # Buscar el préstamo ACTIVO más reciente
            prestamo_activo = None
            i = len(prestamos) - 1
            while i >= 0:
                p = prestamos[i]
                if p.get_codigo_libro() == codigo_devolver and p.esta_en_prestamo():
                    prestamo_activo = p
                    break
                i -= 1
                    
            
            if prestamo_activo is None:
                print("❌ ERROR: No se encontró un préstamo activo (pendiente de devolución) para ese código de libro.")
            else:
                
                fecha_devolucion_valida = False
                fecha_devolucion = ""
                fecha_prestamo = prestamo_activo._fecha_prestamo
                
                while fecha_devolucion_valida == False: 
                    fecha_devolucion = input(f"Ingrese la FECHA de devolución (dd/mm/aaaa). Préstamo: {fecha_prestamo}: ")
                    
                    # 1. Validar el formato y los días/mes
                    resultado_formato = prestamo_activo.validar_formato_fecha(fecha_devolucion)
                    
                    if resultado_formato is not True:
                        print(f"❌ La fecha de devolución no es válida (Formato/Días): {resultado_formato}")
                        continue # Volver a pedir la fecha
                        
                    # 2. Validar que la fecha de devolución sea posterior o igual a la de préstamo
                    resultado_devolucion = prestamo_activo.validar_fecha_devolucion(fecha_prestamo, fecha_devolucion)
                    
                    if resultado_devolucion is not True:
                        print(f"❌ Error de lógica: {resultado_devolucion}")
                        continue # Volver a pedir la fecha
                        
                    # Si ambos son True, la fecha es válida
                    fecha_devolucion_valida = True
                
                # Registrar la devolución
                prestamo_activo._fecha_regreso = fecha_devolucion
                print(f"✅ Devolución registrada con éxito el {fecha_devolucion}.")
        
    # ------------------ g) MOSTRAR HISTORIAL DE PRÉSTAMOS ------------------
    elif opcion == 'g':
        print("\n📜 Historial Completo de Préstamos:")
        hay_prestamos = False
        i = 0
        while i < len(prestamos):
            prestamos[i].mostrar_datos()
            hay_prestamos = True
            i += 1
            
        if hay_prestamos == False:
            print("ℹ️ No hay registros de préstamos todavía.")

    # ------------------ h) EXTRA: LIBROS PRESTADOS ACTUALMENTE ------------------
    elif opcion == 'h':
        print("\n📖 Libros en Préstamo Actualmente:")
        encontrados = False
        i = 0
        while i < len(prestamos):
            if prestamos[i].esta_en_prestamo():
                prestamos[i].mostrar_datos()
                encontrados = True
            i += 1
            
        if encontrados == False:
            print("✅ No hay libros en préstamo en este momento.")

    # ------------------ 0) SALIR ------------------
    elif opcion == '0':
        print("👋 Saliendo del programa. ¡Hasta luego!")
        
    # ------------------ OPCIÓN INVÁLIDA ------------------
    else:
        print("⚠️ Opción no válida. Intente de nuevo.")