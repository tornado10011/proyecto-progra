import random 
import os

dispositivos = ["Router", "Switch", "Servidor", "Access Point"]
estados = ("Operativo", "Falla", "Mantenimiento") 
diagnosticos = {}

def estado():
    return random.choice(estados)

def tiempo():
    return random.randint(1, 100) 

os.system("cls")
print("Bienvenido al programa de Diagnostico de Redes")

for i in range(len(dispositivos)):
            diagnosticos[dispositivos[i]] = {"estado": estado(), "tiempo": tiempo()}

while True:
    
    print("Seleccione una opción: \n"
          "1. Mostrar el reporte de diagnóstico \n"
          "2. Mostrar las estadísticas. \n"
          "3. Ejecutar un nuevo diagnóstico \n"
          "4. Desea ver el historial de diagnosticos \n"
          "5. Salir del programa \n")
    
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))

    except ValueError:
        print("Se digito un dato erroneo...")
        os.system("pause")
        os.system("cls")
        continue

    if opcion == 1:
        os.system("cls")
        print("===== REPORTE DE RED =====")
        for dispositivo, informacion in diagnosticos.items():   
            print(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms """)   # cuando se termina de imprimir la primera por ejemplo el router, se hace un \n automatico para seguir con el siguiente, por eso la funcion de arriba de recorrer cada dispositivo
        os.system("pause")

        histo=input("Desea guardar el historial de este reporte?\n\Digite: si o no: ").lower()


        if histo=="si":
            contador=0
            while histo=="si":
                try:
                    #aqui le indico al usuario que me indique una fecha de registro
                    fecha=input("Digite la fecha para guardar el registro ejemplo:\ndia:22\nmes:05 o 10\naño:26 \nno poner espacios cuando indique la fecha \nDigite: ")
                    if len(fecha) ==6:
                        
                        dia=fecha[:2]
                        mes=fecha[2:4]
                        año=fecha[4:6]

                        fecha=f"{dia}-{mes}-{año}"
                        os.system("pause")
                        os.system("cls")
                    else:
                        print("no ingreso los datos correctamente. Vuelva a intentarlo.")
                        os.system("pause")
                        os.system("cls")
                        continue
                    

                except ValueError:
                    print("indico caracteres invalidos para guardar la fecha. intente de nuevo")
                    continue


                with open ("historial_red.txt", "a", encoding="utf-8") as historial:
                    historial.write(f"fecha: {fecha}\n===== HISTORIAL DE REPORTE DE RED =====\n")
                    for dispositivo, informacion in diagnosticos.items():   
                        historial.write(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms \n""")
                contador+=1

                if contador==1:
                    break

                
        elif histo=="no":
            os.system("pause")
            os.system("cls")
            continue



    elif opcion == 2:
        operativos=[]
        fallas=[]
        mantenimiento=[]
        tiempos=[]

        
        for dispositivo, info  in diagnosticos.items():
            if info["estado"] == "Operativo":
                operativos.append(dispositivo)
            elif info["estado"] == "Falla":
                fallas.append(dispositivo)
            elif info["estado"] == "Mantenimiento":
                mantenimiento.append(dispositivo)

            tiempos.append(info["tiempo"])

        promedio_tiemp= sum(tiempos) / len(tiempos)
        os.system("cls")
        print("ESTADÍSTICAS")
        print(f"""Dispositivos operativos: {len(operativos)}
Dispositivos en falla: {len(fallas)}
dispositivos en mantenimiento: {len(mantenimiento)}
Promedio de los tiempos de respuesta: {promedio_tiemp}""")


        os.system("pause")
        os.system("cls")

    elif opcion == 3:
        os.system("cls")
        diagnosticos.clear()
        for i in range(len(dispositivos)):
            diagnosticos[dispositivos[i]] = {"estado": estado(), "tiempo": tiempo()}
        print("Se ha ejecutado un nuevo diagnóstico de red.\n")

        reemplazo=input("desea reemplazar todo el archivo de registro? \nEscriba si o no \nDigite: ").lower()
        if reemplazo=="si":
            try:
                with open ("historial_red.txt", "w", encoding="utf-8") as historial:
                    print("El sistema guardara el nuevo registro con la ultima fecha indicada")
                    historial.write(f"\n\nfecha: {fecha}\n===== HISTORIAL DE REPORTE DE RED =====\n")
                    for dispositivo, informacion in diagnosticos.items():   
                        historial.write(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms \n""")
            except FileNotFoundError:
                print("El archivo no existe. O no se ah guardado ningun dato todavia.")
                os.system("cls")

        elif reemplazo=="no":
            os.system("cls")
        os.system("pause")
        os.system("cls")



    elif opcion==4:
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
                        
    elif opcion == 5:
        os.system("cls")
        print("Gracias por usar el programa de Diagnóstico de Redes")
        break


    elif opcion>=6 or opcion<1:
        print("se digito un numero erroneo, se reiniciara el programa")
        os.system("pause")
        os.system("cls")
        continue


