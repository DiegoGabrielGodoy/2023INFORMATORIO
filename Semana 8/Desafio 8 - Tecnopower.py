# Desafio 8 - Tecnopower
# Integrantes:
# Godoy, Diego Gabriel 
# Ortiz Kovalek, Emanuel 
# Baibiene, Facundo
# Alarcón, Julieta Guadalupe 
# Agudo, Néstor Adrian
# Bernardis, Mariela Iris
# Sagania, Facundo
# Maidana, Emiliano
# Roldán, Ignacio
# Nasir, Yamil Alí

#Clase Usuario
#atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online
#métodos: login(), registrar()

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

    def login(self): # Lógica para realizar el inicio de sesión
        pass

    def registrar(self): # Lógica para realizar el registro
        pass

#Clase Publico(Usuario)
#atributo: es_publico
#métodos: registrar(), comentar()
class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = True

    def comentar(self): # Lógica para realizar un comentario
        pass

#clase Colaborador(Usuario)
#atributos: es_colaborador
#métodos: registrar(), comentar(), publicar()
class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = True

    def comentar(self): # Lógica para realizar un comentario
        pass

    def publicar(self): # Lógica para publicar un artículo
        pass

#clase Articulo
# id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado

#clase Comentario
# id, id_articulo, id_usuario, contenido, fecha_hora, estado
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado

#Código para elegir entre registrar usuarios o hacer login (si ya está registrado). 
#Una vez registrado y logueado, código que permita comentar al Publico y además publicar al Colaborador.
def elegir_accion():
    opcion = input("¿Deseas 'registrar' un usuario o 'login'?\n")
    if opcion == 'registrar':
        registrar_usuario()
    elif opcion == 'login':
        login_usuario()
    else:
        print("Opción no válida.")

def registrar_usuario():
    # Solicitar información del usuario
    id = input("ID: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    username = input("Username: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    fecha_registro = input("Fecha de registro: ")
    avatar = input("Avatar: ")
    estado = input("Estado: ")
    online = input("¿Está online? (Sí/No): ").lower() == "sí"

    # Crear una instancia de la clase Usuario
    usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)

    # Llamar al método registrar
    usuario.registrar()

    # Comprobar si el usuario es de tipo Publico o Colaborador
    if isinstance(usuario, Publico):
        comentario_publico(usuario)
    elif isinstance(usuario, Colaborador):
        publicar_colaborador(usuario)

def login_usuario():
    # Solicitar credenciales al usuario
    username = input("Username: ")
    contraseña = input("Contraseña: ")

    # Verificar si el usuario está registrado
    usuario_registrado = False  # Bandera para indicar si el usuario está registrado

    # Aquí puedes agregar la lógica para verificar si el usuario está registrado en tu sistema
    # Puedes consultar una base de datos, una lista de usuarios, etc.

    if not usuario_registrado:
        print("El username no está registrado. Por favor, ingrese un usuario registrado.")
        return

    # Crear una instancia de la clase Usuario
    usuario = Usuario(None, None, None, None, username, None, contraseña, None, None, None, None)

    # Llamar al método login
    usuario.login()

    # Comprobar si el usuario es de tipo Publico o Colaborador
    if isinstance(usuario, Publico):
        comentario_publico(usuario)
    elif isinstance(usuario, Colaborador):
        publicar_colaborador(usuario)

def comentario_publico(usuario):
    # Verificar si el usuario es de tipo Publico
    if isinstance(usuario, Publico):
        # Crear una instancia de la clase Publico
        publico = Publico(usuario.id, usuario.nombre, usuario.apellido, ..., ..., ...)

        # Llamar al método comentar de la clase Publico
        publico.comentar()
    else:
        print("Acción no válida. Se requiere un usuario Publico.")

def publicar_colaborador(usuario):
    # Verificar si el usuario es de tipo Colaborador
    if isinstance(usuario, Colaborador):
        # Crear una instancia de la clase Colaborador
        colaborador = Colaborador(usuario.id, usuario.nombre, usuario.apellido, ..., ..., ...)

        # Llamar al método publicar de la clase Colaborador
        colaborador.publicar()
    else:
        print("Acción no válida. Se requiere un usuario Colaborador.")

# Resto del código...

# Llamar a la función para elegir la acción deseada
elegir_accion()
