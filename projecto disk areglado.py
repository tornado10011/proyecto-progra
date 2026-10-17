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
        for dispositivo, informacion in diagnosticos.items():   
            print(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms """)   # cuando se termina de imprimir la primera por ejemplo el router, se hace un \n automatico para seguir con el siguiente, por eso la funcion de arriba de recorrer cada dispositivo
        os.system("pause")
        os.system("cls")

    if opcion == 2:
        operativos=[]
        fallas=[]
        mantenimiento=[]
        tiempos=[]

        
        for dispositivo, info,  in diagnosticos.items():
            if info["estado"] == "Operativo":
                operativos.append(dispositivo)
            elif info["estado"] == "Falla":
                fallas.append(dispositivo)
            elif info["estado"] == "Mantenimiento":
                mantenimiento.append(dispositivo)

            tiempos.append(info["tiempo"])

        promedio_tiemp= sum(tiempos) / len(tiempos)

        print("ESTADÍSTICAS")
        print(f"""Dispositivos operativos: {len(operativos)}
Dispositivos en falla: {len(fallas)}
dispositivos en mantenimiento: {len(mantenimiento)}
Promedio de los tiempos de respuesta: {promedio_tiemp}""")

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