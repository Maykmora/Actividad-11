print("Bienvenido al programa")
p=int(input("Ingrese la cantidad de propietarios que desea agregar: "))
for i in range(p):
    print(f"Propietario No.{i+1}")
    nit=int(input("Ingrese su numero de NIT: "))
    name=input("Ingrese el nombre del propietario: ")
    phone=int(input("Ingrese el numero de teléfono del propietario:"))
    cantidad=int(input("Ingrese la cantidad de vehículos que posee: "))
    for j in range(cantidad):
        print("\nVehículo No.1:")
        placa=input("Ingrese el número de placa del vehículo: ")
        marca=input("Ingrese la marca del vehiculo: ")
        year=int(input("Ingrese el modelo del vehículo: "))
        estado=input("Ingrese el estado del impuesto (sí-no): ")

