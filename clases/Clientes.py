from clases.Herencias import Tipo_Doc

class Clientes(Tipo_Doc): 
    
    lst = [0]
    
    def __init__(self, nombres, apellidos, tipo_doc, num_doc, direccion, telefono, email):
        super().__init__(tipo_doc)
        self.__idCliente = Clientes.generateCod()
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
    
    def Mostrar_TDCliente(self):
        return super().Mostrar_TipoDoc()
    
    def MostrarDTClient(self):
        print(f"Codigo Cliente : {self.__idCliente}")
        print(f"Nombres : {self.__nombres}")
        print(f"Apellidos : {self.__apellidos}")
        Clientes.Mostrar_TDCliente(self)
        print(f"Numero de Documento : {self.__num_doc}")
        print(f"Dirección : {self.__direccion}")
        print(f"Teléfono : {self.__telefono}")
        print(f"Email : {self.__email}")
        