class Seguro:
    """
    La clase Seguro contiene los metodos y atributo necesarios para la funcionalidad del programa de seguradora Leon Dorado.
    ----------------------
    Atributos:
    ----------------------
    nombre:str
        Nombre del nuevo clente
    apellido:str
        Apellido del cliente nuevo
    edad:int
        Edad del cliente
    NumeroCedula:int
        Numero de cedula del cliente
    telf:int
        Numero de telefono del cliente
    Nacionalidad:str
        Nacionalidad del cliente
    contrato:float
        tiempo de duracion del contrato
    cuentaBancaria:int
        Cuenta Bancaria del cliente
    -----------------------
    Metodos
    -----------------------
    def __init__(self, nombre, apellido, edad, NumeroCedula, telf, Nacionalidad, cuentaBancaria):
        Metodo constructor de la clase usada para que el cliente pueda registrarse en la seguradora Leon Dorado.

    def ValidacionUsuario(self):
        Metodo usado para validar la edad del cliente registrado.
    """
    def __init__(self, nombre, apellido, edad, NumeroCedula, telf, Nacionalidad, contrato ,cuentaBancaria):
        """
        Metodo constructor de la clase usada para que el cliente pueda registrarse en la seguradora Leon Dorado.
        ----------------------
        Atributos:
        ----------------------
        nombre:str
            Nombre del nuevo clente
        apellido:str
            Apellido del cliente nuevo
        edad:int
            Edad del cliente
        NumeroCedula:int
            Numero de cedula del cliente
        telf:int
            Numero de telefono del cliente
        Nacionalidad:str
            Nacionalidad del cliente
        contrato:float
            tiempo de duracion del contrato
        cuentaBancaria:int
            Cuenta Bancaria del cliente
        """
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.NumeroCedula=NumeroCedula
        self.telf=telf
        self.Nacionalidad=Nacionalidad
        self.contrato=contrato
        self.cuentaBancaria=cuentaBancaria
        

    def ValidacionUsuario(self):
        """
        Metodo de la clase Seguro, sirve para poder validar el tiempo de contrato que desea el cliente.
        -------------------------
        Atributos:
        -------------------------
        nombre:str
            Nombre del nuevo clente
        apellido:str
            Apellido del cliente nuevo
        edad:int
            Edad del cliente
        NumeroCedula:int
            Numero de cedula del cliente
        telf:int
            Numero de telefono del cliente
        Nacionalidad:str
            Nacionalidad del cliente
        contrato:float
            tiempo de duracion del contrato
        cuentaBancaria:int
            Cuenta Bancaria del cliente
        """
        return (self.contrato<2)
    
class TiposSeguros(Seguro):
    """
    Esta clase TiposSeguros heredara los atributos de la la superclase Seguro, en esta clase se determinara si el cliente
    desea contratar algun otro tipo de seguro.
    """
    def __init__(self, nombre, apellido, edad, NumeroCedula, telf ,Nacionalidad ,cuentaBancaria, tiposeguro):
        """
        Metodo constructor de la clase TiposSeguros
        ----------------
        Atributos:
        ----------------
        tiposeguro: str
            El ciente ingresa algun otro tipo de seguro  que desea contratar
        """
        self.seguros = tiposeguro
        """
        Asignar el nuevo tipo de seguro que desea contratar
        """
        super().__init__( nombre, apellido, edad, NumeroCedula, telf ,Nacionalidad ,cuentaBancaria)
        

if __name__ == "__main__":
    """
    En main se pide que el usuario ingrese los datos del cliente para asi completar
    los atributos de la clase Seguro y poderlos instarciar en el objeto DatosClientes
    """
    
    print("==========================================================")
    print("              REGISTRO DE CLIENTE NUEVOS ")
    print("==========================================================")
    print("    INGRESE LOS DATOS DEL CLIENTE      ")
    print("==========================================================")
    #Ingreso de los datos del cliente usando los atributos de la clase.
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    edad=int(input("Ingrese su edad: "))
    NumeroCedula=int(input("Ingrese su nuemro de cedula :"))
    telf=int(input("Ingrese su numero de telefono: "))
    Nacionalidad=input("Ingrese su pais de origen: ")
    contrato=float(input("Ingrese el tiempo de valides de su contrato: "))
    cuentaBancaria=int(input("Ingrese su numero de cuenta bancario: "))
    print("==========================================================")

    DatosCliente=Seguro(nombre, apellido, edad, NumeroCedula, telf, Nacionalidad, contrato ,cuentaBancaria)
    print("==========================================================")
    print("         DATOS DEL CLIENTE        ")
    print("==========================================================")
   #Imprime los datos agragados. 
    print("Nombre           : ", DatosCliente.nombre)
    print("Apellido         : ", DatosCliente.apellido)
    print("Edad             : ", DatosCliente.edad)
    print("Numero de cedula : ", DatosCliente.NumeroCedula)
    print("Telefono celular : ", DatosCliente.telf)
    print("Nacionalidad     : ", DatosCliente.Nacionalidad)
    print("Tiempo del contrato :",DatosCliente.contrato)
    print("Cuenta bancaria  : ", DatosCliente.cuentaBancaria)
    print("==========================================================")
    if DatosCliente.ValidacionUsuario ():
        print("Bienvenidoa estar seguro.")
    else:
        print("Bienvenido, por seleccionar un contrato superior a los")
        print("2 años recive dos meses de libres de cuota.")
    print("==========================================================")