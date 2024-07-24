
class Tipo_Doc:
    def __init__(self, tipo_doc):
        self.tipo_doc = tipo_doc
        
    def Mostrar_TipoDoc(self):
        print(f"Tipo de Documento : {self.tipo_doc}")
        
class Permiso:
    def __init__(self, tipo_permiso):
        self.tipo_permiso = tipo_permiso
        
    def Mostrar_Permiso(self):
        print(f"Tipo de Permiso : {self.tipo_permiso}")
        
    def Cambiar_Permiso(self, tipo_permiso):
        self.tipo_permiso = tipo_permiso
        
        
class Cargo:
    def __init__(self, n_rol):
        self.n_rol = n_rol
        
    def Mostrar_Rol(self):
        print(f"Cargo : {self.n_rol}")
        
    def Cambiar_Permiso(self, n_rol):
        self.n_rol = n_rol
        
                