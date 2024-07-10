#Examen
import os
import time
import random
import csv


nuclear=lambda: os.system('cls')
trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
pagados=[]


def aplicacion():
    while True:
        try:
            nuclear()
            print("1.-Asignar sueldos aleatorios\n2.-Clasificar sueldos\n3.-Ver estadisticas\n4.-Reporte de sueldos\n5.-Salir del programa")
            cazador=int(input("Eleccion: "))
            if cazador in [1,2,3,4,5]:
                return cazador
        except ValueError:
            print("Opcion no valida")
            time.sleep(0.2)

def sueldosAleatorios():
    global pagados
    pagados=[]
    for curupeko in trabajadores:
        pago=random.randint(300000,2500000)
        contrato={}
        contrato={"Name":curupeko,"Pago":pago}
        pagados.append(contrato)
        
def clasificarSueldos():
    primero=[i for i in pagados if i["Pago"]<800000]
    segundo=[j for j in pagados if j["Pago"]>799999 and j["Pago"]<2000001]
    tercero=[k for k in pagados if k["Pago"]>2000000]
    print(f"Sueldos menores a $800.000 TOTAL: {len(primero)}\nNombre empleado\tSueldo")
    for rajang in primero:
        print(f"{rajang["Name"]}\t{rajang["Pago"]}")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(segundo)}\nNombre empleado\tSueldo")
    for rajang in segundo:
        print(f"{rajang["Name"]}\t{rajang["Pago"]}")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(tercero)}\nNombre empleado\tSueldo")
    for rajang in tercero:
        print(f"{rajang["Name"]}\t{rajang["Pago"]}")
    totalSueldos=0
    for rajang in pagados:
        totalSueldos+=rajang["Pago"]
    print(f"TOTAL SUELDOS: ${totalSueldos:,}")

def verEstadisticas():
    mayor=max(pagados,key=lambda pepito: pepito["Pago"])
    menor=min(pagados,key=lambda pepito: pepito["Pago"])
    print(f"Sueldo mas alto es de {mayor["Pago"]} que le pertenece a {mayor["Name"]}")
    print(f"Sueldo mas bajo es de {menor["Pago"]} que le pertenece a {menor["Name"]}")
    suma=sum(i["Pago"] for i in pagados)
    promedio=int(suma/10)
    print(f"El promedio de sueldos es de ${promedio}")

def reportecsv():
    with open("plantilla.csv","w",newline="") as meh:
        pluma=csv.writer(meh)
        pluma.writerow(['Nombre empleado','Sueldo Base','Descuento Salud','Descuento AFP','Sueldo Liquido'])
        for calca in pagados:
            pluma.writerow([calca["Name"],calca["Pago"],int(calca["Pago"]*0.07),int(calca["Pago"]*0.12),int(calca["Pago"]*0.81)])
        


def respuesta(parada):
    if parada==1:
        sueldosAleatorios()
    if parada==2:
        clasificarSueldos()
        input()
    if parada==3:
        verEstadisticas()
        input()
    if parada==4:
        reportecsv()
        
while True:
    meta=aplicacion()
    if meta==5:
        print("Finalizando programa...")
        print("Desarrollado por Ignacio Bravo")
        print("RUT 20.121.609-5")
        break
    else:
        respuesta(meta)