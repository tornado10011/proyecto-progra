import random 
import os
import time

def estado():
    return random.choice(estados)

def tiempo():
    return random.randint(1, 100) 

#estoy definiendo el pedir fecha con el import time
def fecha():
    fecha_actual = time.strftime("%d-%m-%Y %H:%M:%S")
    return fecha_actual

dispositivos = ["Router", "Switch", "Servidor", "Access Point"]
estados = ("Operativo", "Falla", "Mantenimiento") 
diagnosticos = {}

os.system("cls")
print("Bienvenido al programa de Diagnostico de Redes")
#en lo que sigue se lee una lista para sacar los nombres de los dispositivos y  asignarles el estado y el tiempo con el .choice para el estado y random para el tiempo
for i in range(len(dispositivos)):
            diagnosticos[dispositivos[i]] = {"estado": estado(), "tiempo": tiempo()} 

while True:
    print("=== /Menu Principal\\ === : \n"
          "------------------------------------\n"
          "1. Mostrar el reporte de diagnóstico \n"
          "------------------------------------\n"
          "2. Guardar el reporte \n"
          "------------------------------------\n"
          "3. Mostrar las estadísticas. \n"
          "------------------------------------\n"
          "4. Ejecutar un nuevo diagnóstico \n"
          "------------------------------------\n"
          "5. Desea ver el historial de diagnosticos \n"
          "-------------------------------------\n"
          "6. Salir del programa \n"
          "-------------------------------------\n"
          )
        
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))
    except ValueError:
        print("Se digitaron valores equivocado...")
        os.system("pause")
        os.system("cls")
        continue

    if opcion == 1:
            os.system("cls")
            print("===== REPORTE DE RED =====")
            for dispositivo, informacion in diagnosticos.items():   
             # cuando se termina de imprimir la primera por ejemplo el router, se hace un \n automatico para seguir con el siguiente, por eso la funcion de arriba de recorrer cada dispositivo
                print(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms """)  
            os.system("pause")
            os.system("cls")

    elif opcion==2:
                #lo que se hace aqui es pedirle la fecha definida al inicio del codigo y crear el txt y guarda el reporte hecho anteriormente
                fecha=fecha()
                with open ("historial_red.txt", "a", encoding="utf-8") as historial:
                    historial.write(f"\nfecha: {fecha}\n===== HISTORIAL DE REPORTE DE RED =====\n")
                    #aqui lo que se hace es dividir los dispositivos y la informacion guardados en el diccionario y crear y escribirlo en un archivo llamado historial_red.txt
                    for dispositivo, informacion in diagnosticos.items():   
                        historial.write(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms \n""")
                    os.system("cls")
                    print("Se ah guardado correctanente el registro.")
                    os.system("pause")
                    os.system("cls")
                    continue
                break

    elif opcion == 3:
        operativos=[]
        fallas=[]
        mantenimiento=[]
        tiempos=[]
        # divide la informacion del diccionario en dispositivos e informacion para sacar los estados de los dispositivos 
        for dispositivo, info in diagnosticos.items():
            if info["estado"] == "Operativo":
                operativos.append(dispositivo)
            elif info["estado"] == "Falla":
                fallas.append(dispositivo)
            elif info["estado"] == "Mantenimiento":
                mantenimiento.append(dispositivo)
            tiempos.append(info["tiempo"])
        # esto lo que hace es agarrar todos los tiempos dados a los dispositivos y sacar un promedio general
        promedio_tiemp= sum(tiempos) / len(tiempos)
        os.system("cls")
        print("ESTADÍSTICAS")
        print(f"""Dispositivos operativos: {len(operativos)}
Dispositivos en falla: {len(fallas)}
dispositivos en mantenimiento: {len(mantenimiento)}
Promedio de los tiempos de respuesta: {promedio_tiemp}""")
        os.system("pause")
        os.system("cls")

    elif opcion == 4:
        # esto lo que hace es limpiar el diccionario y meter nuevos datos en el mismo diccionario
        os.system("cls")
        diagnosticos.clear()
        for i in range(len(dispositivos)):
            diagnosticos[dispositivos[i]] = {"estado": estado(), "tiempo": tiempo()}
        print("Se ha ejecutado un nuevo diagnóstico de red.\n")

        while True:
            # esto lo que hace es reemplazar los datos pero en el archivo y con la w borra y escribe los datos nuevos
            try:
                reemplazo=int(input("desea reemplazar todo el archivo de registro? \nEscriba 1 si, 2 no \nDigite: "))
                if reemplazo==1:
                    try:
                        fecha=fecha()
                        with open ("historial_red.txt", "w", encoding="utf-8") as historial:
                            historial.write(f"\nfecha: {fecha}\n===== HISTORIAL DE REPORTE DE RED =====\n")
                            for dispositivo, informacion in diagnosticos.items():   
                                historial.write(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms \n""")
                            historial.write(" ")
                            print("el sistema guardo realizo correctamente el reemplazo")
                            os.system("pause")
                            os.system("cls")
                            break
                    except FileNotFoundError:
                        print("El archivo no existe. O no se ah guardado ningun dato todavia.")
                        os.system("cls")
                elif reemplazo==2:
                    os.system("pause")
                    os.system("cls")
                    break

                elif reemplazo<1 or reemplazo>2:
                    print("no ingreso los datos correctamente. Vuelva a intentarlo.")
                    os.system("pause")
                    os.system("cls")
                    continue
                    
            except (TypeError, ValueError):
                print("no ingreso los datos correctamente. Vuelva a intentarlo.")
                os.system("pause")
                os.system("cls")
                continue

    elif opcion==5:
        # esta opcion es para abrir los datos guardados en el archivo y mostrarlos en la terminal
        try:
            os.system("cls")
            with open ("historial_red.txt", "r", encoding="utf-8") as historial:
                print(historial.read())
                os.system("pause")
                os.system("cls")
        except FileNotFoundError:
            print("El archivo no existe. O no se ah guardado ningun dato todavia.")
            os.system("pause")
            os.system("cls")
                        
    elif opcion == 6:
        #esta opcion es solamente para que el usuario pueda salir del diagnostico
        os.system("cls")
        print("Gracias por usar el programa de Diagnóstico de Redes")
        break

    elif opcion>=7 or opcion<1:
        print("se digito un numero erroneo, se reiniciara el programa")
        os.system("pause")
        os.system("cls")
        continue