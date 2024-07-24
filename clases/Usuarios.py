from clases.Herencias import Permiso, Tipo_Doc, Cargo

class Usuarios(Cargo, Tipo_Doc, Permiso):
    
    lst = [0]
    
    def __init__(self, nombres, apellidos, tip_doc, celular, nom_usuario, email, contrasenia, n_cargo, tip_permiso):
        Cargo.__init__(self, n_cargo)
        Tipo_Doc.__init__(self, tip_doc)
        Permiso.__init__(self, tip_permiso)
        self.__idUser = Usuarios.generateCod()
        self.nombres = nombres
        self.apellidos = apellidos
        self.celular = celular
        self.nom_usuario = nom_usuario
        self.email = email
        self.contrasenia = contrasenia
        
    def generateCod():
        Usuarios.lst[0] += 1
        c = Usuarios.lst[0]
        return f"COD_00_{c}"

    def MostrarDtUser(self):
        print(f"Codigo Usuario: {self.__idUser}")
        print(f"Nombres : {self.nombres}")
        print(f"Apellidos : {self.apellidos}")
        print(f"Tipo de Documento : {self.tipo_doc}")
        print(f"Numero  : {self.celular}")
        print(f"Nombre de Usuario : {self.nom_usuario}")
        print(f"Email : {self.email}")
        print(f"Contraseña : {self.contrasenia}")
        print(f"Cargo : {self.n_rol}")
        print(f"Permiso : {self.tipo_permiso}")