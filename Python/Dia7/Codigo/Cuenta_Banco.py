class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self,nombre,apellido,ncuenta,balance):
        super().__init__(nombre,apellido)
        self.ncuenta = ncuenta
        self.balance = balance
        
    def __str__(self):
        return f"Nombre completo {self.nombre} {self.apellido} \n Numero cuenta :{self.ncuenta} \n Balance = {self.balance} €"
    
    
    def depositar(self,balance,cantidad_depositada):
        self.balance = int(balance) + int(cantidad_depositada)
    
    def retirar(self,balance,cantidad_retirada):
        self.balance = int(balance) - int(cantidad_retirada)
    
        
        
        
nombre= input("Nombre ")
apellido=input("Apeliidos ")
ncuenta= 321032
balance =input("Balance= ")


cliente1 = Cliente(nombre,apellido,ncuenta,balance)


bucle = True





def consultar(cliente):
    print(cliente)


def depositar(cliente,cantidad,balance):
    cliente.depositar(balance,cantidad)
    print(f"El saldo actual es de {cliente.balance}")

def retirar(cliente,cantidad,balance):
    cliente.retirar(balance,cantidad)
    print(f"El saldo actual es de {cliente.balance}")


eleccion = int(input("""Que desea hacer
1-Consultar credenciales
2-Depositar dinero
3-Retirar dinero
4-Cerrar Sesión
"""))

while bucle == True:
    
    match eleccion:
        case 1:
            consultar(cliente1)
            seguir = input("Seguir S/N,\n").lower()
            if seguir == "s":
                eleccion = 0
            else:
                bucle = False
        case 2:
            cantidad = int(input("Cuanto deseas depositar\n"))
            depositar(cliente1,cantidad,cliente1.balance)
            seguir = input("Seguir S/N,\n").lower()
            if seguir == "s":
                eleccion = 0
            else:
                bucle = False
        case 3:
            cantidaret= int(input("Cuanto dinero desea retirar \n"))
            retirar(cliente1,cantidaret,cliente1.balance)
            seguir = input("Seguir S/N,\n").lower()
            if seguir == "s":
                eleccion = 0
            else:
                bucle = False
        case 4:
            bucle = False
        case 0:
            eleccion = int(input("""Que desea hacer
1-Consultar credenciales
2-Depositar dinero
3-Retirar dinero
4-Cerrar Sesión
"""))