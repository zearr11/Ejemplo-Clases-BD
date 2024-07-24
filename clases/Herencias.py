#PARA USUARIO, CLIENTES
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
        
#PARA PRODUCTOS

class Marca:
    
    def __init__(self, marca_prod):
        self.__marca_prod = marca_prod
        
    def Mostrar_Prod(self):
        print(f"Marca : {self.__marca_prod}")
        
    def CambiarMarca(self, marca_prod):
        self.__marca_prod = marca_prod
    
class Categoria:
    
    def __init__(self, categ):
        self.__categ = categ
        
    def MostrarCateg(self):
        print(f"Categoria : {self.__categ}")
        
    def CambiarCategoria(self, categ):
        self.__categ = categ

class Medida:
    
    def __init__(self, medida):
        self.__mediDa = medida
        
    def MostrarMedida(self):
        print(f"Medida : {self.__mediDa}")
        
    def CambiarMedida(self, medida):
        self.__mediDa = medida
    
    
class EstadoProducto:
    
    

    

                