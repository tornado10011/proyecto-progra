import random 
import os

dispositivos = ["Router", "Switch", "Servidor", "Access Point"]
estados = ("Operativo", "Falla", "Mantenimiento") 
diagnosticos = {}

def estado():
    return random.choice(estados)

def tiempo():
    return random.randint(1, 100) 

#estoy definiendo el pedir fecha para no escribir todo el codigo varias veces
def pedir_fecha():
    while True:
            fecha=input("\nDigite la fecha para guardar el registro ejemplo:"" 221026 ""=DD/MM/YY \nno poner espacios cuando indique la fecha \nDigite: ")
            #aqui lo que hago es dividir los datos ingresados por el usuario y los divido entre dia mes y año y luego lo formateo con un - por medio
            if len(fecha) == 6:
                try:
                    #el valor del input son letras entonces lo siguiente es pasarlo a numeros y si no son numeros enteros pasara lo que dice el siguiente except 
                    dia=int(fecha[:2])
                    mes=int(fecha[2:4])
                    año=int(fecha[4:6])
                
                    fecha=f"{dia}-{mes}-{año}"
                    os.system("pause")
                    os.system("cls")
                    return fecha
                
                except (ValueError, TypeError):
                    print("no ingreso los datos correctamente. Vuelva a intentarlo.")
                    os.system("pause")
                    os.system("cls")
                    continue
                
            else:
                print("no ingreso los datos correctamente. Vuelva a intentarlo.")
                os.system("pause")
                os.system("cls")
                continue

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

            while True:
                try:
                    histo=int(input("Desea guardar el historial de este reporte?\nDigite: 1 si o 2 no: "))
                    if histo<1 or histo>2:
                        print("no indico que desea realizar correctamente") 
                        os.system("pause")
                        os.system("cls")
                        continue
                    break
                except ValueError:
                    print("indico caracteres invalidos. intente de nuevo")
                    os.system("pause") 
                    os.system("cls")
                    continue

            if histo==1:
                fecha=pedir_fecha()
                with open ("historial_red.txt", "a", encoding="utf-8") as historial:
                    historial.write(f"\nfecha: {fecha}\n===== HISTORIAL DE REPORTE DE RED =====\n")
                    for dispositivo, informacion in diagnosticos.items():   
                        historial.write(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms \n""")
                    continue
                break
            elif histo==2:
                os.system("pause")
                os.system("cls")
                continue

    elif opcion == 2:
        operativos=[]
        fallas=[]
        mantenimiento=[]
        tiempos=[]

        for dispositivo, info in diagnosticos.items():
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

        while True:
            try:
                reemplazo=int(input("desea reemplazar todo el archivo de registro? \nEscriba 1 si, 2 no \nDigite: "))
                if reemplazo==1:
                    try:
                        fecha=pedir_fecha()
                        with open ("historial_red.txt", "w", encoding="utf-8") as historial:
                            historial.write(f"\nfecha: {fecha}\n===== HISTORIAL DE REPORTE DE RED =====\n")
                            for dispositivo, informacion in diagnosticos.items():   
                                historial.write(f"""{dispositivo}: {informacion["estado"]} - {informacion["tiempo"]} ms \n""")
                            historial.write(" ")
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