print("Bienvenido al programa")
propietarios={}
p=int(input("Ingrese la cantidad de propietarios que desea agregar: "))
for i in range(p):
    print(f"Propietario No.{i+1}")
    nit=int(input("Ingrese su numero de NIT: "))
    name=input("Ingrese el nombre del propietario: ")
    phone=int(input("Ingrese el numero de teléfono del propietario:"))
    cantidad=int(input("Ingrese la cantidad de vehículos que posee: "))
    info_vehiculo = {}
    for j in range(cantidad):
        print(f"\nVehículo No.{j+1}:")
        placa=input("Ingrese el número de placa del vehículo: ")
        marca=input("Ingrese la marca del vehiculo: ")
        modelo=input("Ingrese el modelo del carro:")
        year=int(input("Ingrese el año del vehículo: "))
        estado=input("Ingrese el estado del impuesto (sí-no): ")
        info_vehiculo[placa]={
            "marca":marca,
            "modelo":modelo,
            "año":year,
            "estado":estado
        }

    propietarios[nit]={
        "nombre":name,
        "teléfono":phone,
        "Vehículos":[info_vehiculo]
    }
print("\n--LISTADO DE PRODUCTOS--")
contador1=1
for nit,datos in propietarios.items():
    contador2 = 1
    print(f"Propietario No.{contador1}")
    print(f"NIT: {nit}")
    print(f"Nombre:{datos["nombre"]}")
    print(f"Teléfono:{datos["teléfono"]}")
    for placa,infor in info_vehiculo.items():
        print(f"\nVehículo No.{contador2}")
        print(f"Placa: {placa}")
        print(f"Marca: {infor["marca"]}")
        print(f"Modelo:{infor["modelo"]}")
        print(f"Año:{infor["año"]}")
        print(f"Estado:{infor["estado"]}")
        contador2+=1
    contador1+=1




