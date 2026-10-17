import random 
import os

dispositivos = ["Router", "Switch", "Servidor", "Access Point"]
estados = ("Operativo", "Falla", "Mantenimiento") 
diagnosticos = {}

def estado():
    return random.choice(estados)

def tiempo():
    return random.randint(1, 100) 

print("Bienvenido al programa de Diagnostico de Redes")

for i in range(len(dispositivos)):
            diagnosticos[dispositivos[i]] = {"estado": estado(), "tiempo": tiempo()}

while True:
    print("Seleccione una opción: \n"
          "1. Mostrar el reporte de diagnóstico \n"
          "2. Mostrar las estadísticas. \n"
          "3. Ejecutar un nuevo diagnóstico \n"
          "4. Salir del programa ")
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))

    except ValueError:
        print("Se digito un dato erroneo...")
        os.system("pause")
        os.system("cls")
        continue

    if opcion == 1:
        print("===== REPORTE DE RED =====")
        print(f"{diagnosticos}\n")
        os.system("pause")
        os.system("cls")

    if opcion == 2:
        operativos=[]
        fallas=[]
        mantenimiento=[]
        
        for dispositivo, info in diagnosticos.items():
            if info["estado"] == "Operativo":
                operativos.append(dispositivo)
            elif info["estado"] == "Falla":
                fallas.append(dispositivo)
            elif info["estado"] == "Mantenimiento":
                mantenimiento.append(dispositivo)

        print("ESTADÍSTICAS")
        print(f"Dispositivos operativos: {len(operativos)}")
        print(f"Dispositivos en falla: {len(fallas)}")
        print(f"Dispositivos en mantenimiento: {len(mantenimiento)}\n")
        os.system("pause")
        os.system("cls")

    if opcion == 3:
        diagnosticos.clear()
        for i in range(len(dispositivos)):
            diagnosticos[dispositivos[i]] = {"estado": estado(), "tiempo": tiempo()}
        print("Se ha ejecutado un nuevo diagnóstico de red.\n")
        os.system("pause")
        os.system("cls")


    if opcion == 4:
        print("Gracias por usar el programa de Diagnóstico de Redes")
        os.system("pause")
        break

    if opcion>4 or opcion<1:
        print("se digito un numero erroneo, se reiniciara el programa")
        os.system("pause")
        os.system("cls")
        continue