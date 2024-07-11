from random import*
import csv
import os
import time
with open("Trabajadores.csv","w",newline="")as trabajadores:
    trabajadores_totales_csv=csv.writer(trabajadores)
    trabajadores_totales_csv.writerow(["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"])

def menu():
    
    while True:
        try:
            print("-----Bienvenido a Empresa duocuc-----\n\nPORFAVOR ELIJA UNA DE LAS OPCIONES:\n")
            print("1.-Asignar sueldos aleatorios\n2.-Clasificar sueldos\n3.-Ver estadisticas\n4.-Reporte de sueldos\n5.-Salir del programa\n")
            opc=int(input("Ingrese una de las opciones:"))    
            if opc==1:
                asignarsueldos()
                time.sleep(1)
                os.system("cls")
                print("!Sueldos generados correctamente!")
                time.sleep(1)
                os.system("cls")
            elif opc==2:
                time.sleep(1)
                os.system("cls")
                clasificarsueldos()
                time.sleep(1)
                os.system("cls")
            elif opc==3:
                time.sleep(1)
                os.system("cls")
                verestadisticas()
                time.sleep(1)
                os.system("cls")
            elif opc==4:
                reportedesueldos()
            elif opc==5:
                salirdelprograma()
                break
            else:
                time.sleep(1)
                os.system("cls")
                print("Ingrese una opcion entre 1 y 5")
                time.sleep(1)
                os.system("cls")
        except ValueError:
            time.sleep(1)
            os.system("cls")
            print("Ingrese un valor compatible")
            time.sleep(1)
            os.system("cls")

def asignarsueldos():
    sueldo1=randint(300000,2500000)
    sueldo2=randint(300000,2500000)
    sueldo3=randint(300000,2500000)
    sueldo4=randint(300000,2500000)
    sueldo5=randint(300000,2500000)
    sueldo6=randint(300000,2500000)
    sueldo7=randint(300000,2500000)
    sueldo8=randint(300000,2500000)
    sueldo9=randint(300000,2500000)
    sueldo10=randint(300000,2500000)
    sueldos_aleatorios=([sueldo1,sueldo2,sueldo3,sueldo4,sueldo5,sueldo6,sueldo7,sueldo8,sueldo9,sueldo10])
    with open("Trabajadores.csv","a",newline="") as trabajadores:
        trabajadores_totales_csv=csv.writer(trabajadores)
        trabajadores_totales_csv.writerow(sueldos_aleatorios)

  

                            
def clasificarsueldos():
    print('''Sueldos menores a $800.000-Total=\nNombre del empleado\t\tSueldo\n
          Juan Perez\nMaria Garcia\nElena Fernandez\nSueldos entre $800.000 y $2.000.000-Total=\n
          Nombre del empleado\t\tSueldo\nCarlos Lopez\nAna Martinez\nFrancisco Diaz\n
          Sueldos superiores a $2.000.000-Total=\nNombre empleado\t\tSueldo\nPedro Rodriguez\nLaura Hernandez\nMiguel Sanchez\nIsabel Gomez''')
         


def verestadisticas():
    print("El MAYOR SUELDO ES:")
    print("EL MENOR SUELDO ES:")
    print("EL PROMEDIO ES:")
    print("LA MEDIA GEOMETRICA ES:")
def reportedesueldos():
    print("4")

def salirdelprograma():
    os.system("cls")
    print("Finalizando programa....")
    time.sleep(3)
    print("Desarrollado por Martin Sandoval\nRUT: 21.351.543-8")


menu()        
