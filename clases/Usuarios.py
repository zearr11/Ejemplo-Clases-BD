from clases.Herencias import Permiso, Tipo_Doc, Cargo

class Usuarios(Cargo, Tipo_Doc, Permiso):
    
    lst = [0]
    
    def __init__(self, nombres, apellidos, tip_doc, num_doc, telefono, nom_usuario, email, contrasenia, n_cargo, tip_permiso):
        Cargo.__init__(self, n_cargo)
        Tipo_Doc.__init__(self, tip_doc)
        Permiso.__init__(self, tip_permiso)
        self.__idUser = Usuarios.generateCod()
        self.__nombresUser = nombres
        self.__apellidosUser = apellidos
        self.__num_docUser = num_doc
        self.__telfUser = telefono
        self.__nom_User = nom_usuario
        self.__emailUser = email
        self.__contraseniaUser = contrasenia
        
    def generateCod():
        Usuarios.lst[0] += 1
        c = Usuarios.lst[0]
        return f"COD_00_{c}"

    def MostrarDtUser(self):
        print(f"Codigo Usuario: {self.__idUser}")
        print(f"Nombres : {self.__nombresUser}")
        print(f"Apellidos : {self.__apellidosUser}")
        print(f"Teléfono  : {self.__telfUser}")
        print(f"Tipo de Documento : {self.tipo_doc}")
        print(f"Numero de Documento {self.__num_docUser}")
        print(f"Nombre de Usuario : {self.__nom_User}")
        print(f"Email : {self.__emailUser}")
        print(f"Contraseña : {self.__contraseniaUser}")
        print(f"Cargo : {self.n_rol}")
        print(f"Permiso : {self.tipo_permiso}")