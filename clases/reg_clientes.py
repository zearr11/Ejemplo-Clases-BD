from clases.Herencias import Tipo_Doc

class Clientes(Tipo_Doc): 
    
    lst = [0]
    
    def __init__(self, tipo_doc, nombres, apellidos, num_doc, direccion, telefono, email):
        super().__init__(tipo_doc)
        self.__clientes = Clientes.generateCod()
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__num_doc = num_doc
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        
    def generateCod():
        Clientes.lst[0] += 1
        c = Clientes.lst[0]
        return f"COD_00_{c}"
    
    def ShowTD_Cliente(self):
        return super().showTD()
    
    def showElements(self):
        print(f"Codigo Cliente : {self.__clientes}")
        print(f"Nombres : {self.__nombres}")
        print(f"Apellidos : {self.__apellidos}")
        Clientes.ShowTD_Cliente(self)
        print(f"Numero de Documento : {self.__num_doc}")
        print(f"Dirección : {self.__direccion}")
        print(f"Teléfono : {self.__telefono}")
        print(f"Email : {self.__email}")
        