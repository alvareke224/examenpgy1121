from os import system
system ("cls")
asientos=[True,True,True,True,True,True,True,True,True,True
          ,True,True,True,False,False,False,True,True,True,True,
          True,True,True,True,True,True,True,True,True,True,
          True,True,False,True,True,True,True,True,True,True,
          True,True,True,True,False,True,True,True,True,True,
          True,True,True,True,True,True,True,True,True,True,
          True,True,True,True,True,True,True,True,True,True,
          True,True,True,True,True,True,True,True,True,True,
          True,True,True,True,True,True,True,True,True,True,
          True,True,True,True,True,True,True,True,True,True]
asistentes=[]
Total=[]
platinum=[]
gold=[]
silver=[]


def ganancias(tipoentrada,cantidad,total):
    print(f"""
            Resumen de ganancias :
            
            Tipo de entrada: {tipoentrada}
            Cantidad: {cantidad}
            
            Total: {total}
            """)

def salida(nombre,apellido,rut,tipoentrada,cantidad,total):
    print(f"""
            salida del sistema:
            
            Comprador: {nombre} {apellido}
            Rut: {rut}
            Tipo de entrada: {tipoentrada}
            Cantidad: {cantidad}
            fecha: 10/07/2023
            Total: {total}
            """)

def comprar():

    print(""" elija su entrada:
    1.platinium: $120.000 (asientos del 1 al 20)
    2.gold: $80.000 (aientos del 21 al 50)
    3.silver: 50.000 (asientos del 51 al 100)
    
    """)
    print("ingrese el tipo de entrada que desea: ")
    comprar=input
    match comprar:
        case 1:
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa tu apellido: ")
            rut=input("Ingresa tu rut sin puntos y sin digito verificador : ")
            asistentes.append(nombre,apellido,rut,tipoentrada)
            tipoentrada="platinium"
            cantidad=int(input("Ingresa la cantidad de entradas: "))
            total=cantidad*120000
            Total.append(total)
            platinum.append(cantidad)
            
        case 2:
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa tu apellido: ")
            rut=input("Ingresa tu rut sin puntos y sin digito verificador: ")
            asistentes.append(nombre,apellido,rut,tipoentrada)
            tipoentrada="gold"
            cantidad=int(input("Ingresa la cantidad de entradas: "))
            total=cantidad*80000
            Total.append(total)
            gold.append(cantidad)
            
        case 3:
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa tu apellido: ")
            rut=input("Ingresa tu rut sin puntos y sin digito verificador: ")
            asistentes.append(nombre,apellido,rut,tipoentrada)
            tipoentrada="silver"
            cantidad=int(input("Ingresa la cantidad de entradas: "))
            total=cantidad*50000
            Total.append(total)
            silver.append(cantidad)
        
            print("""
            1 2 3 4 5 6 7 8 9 10
            11 12 13 x x x 17 18 19 20
            21 22 23 24 25 26 27 28 29 30 
            31 32 x 34 35 36 37 38 39 40
            41 42 43 44 x 46 47 48 49 50 
            51 52 53 54 55 56 57 58 59 60 
            61 62 63 64 65 66 67 68 69 70
            71 72 73 74 75 76 77 78 79 80 
            81 82 83 84 85 86 87 88 89 90 
            91 92 93 94 95 96 97 98 99 100
            """)
            opcion=input(print("seleccione un asiento disponible"))
            if opcion==True:
                print("la operacion se ha realizado correctamente")
            else opcion==False:
                print("no esta disponible")


def mostrar_ubicaciones():
    for i in asientos:
        print(i)


def ver_listado_asitentes():
    print("listado de asistentes por rut")
    if len(asistentes)==0:
        print("no hay asistentes registrados")
    else:
        for rut, asiento in asistentes:
            print(f"rut{rut}, asiento {asiento} ")






    while True:
        opcion=input("""bienvenido a "CREATIVOS.CL"
                    1. comprar entradas 
                    2. mostrar ubiucaciones disponibles
                    3. ver listado de asistentes 
                    4. mostrar ganancias totales
                    5. salir 
        
        """)

        match opcion:
            case 1:
                comprar()
            case 2:
                mostrar_ubicaciones()
            case 3:
                ver_listado_asitentes()
            case 4:
                ganancias()
            case 5:
                salida()
                
            case other:
                print("opcion no valida")