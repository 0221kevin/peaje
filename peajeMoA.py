'''
Un peaje de la ciudad quiere que usted sistematice el contro de pago de los peajes, por este pasan tres tipos de vehiculos:
1.motos
2.autos
3.camiones
no se sabe cuantos de estos pasan al dia por e lpeake, pero cuando el dia finaliza se registrara un tipo de veiculo "0-cero"
el cobro del tipo de vehiculo es el siguiente:
1.motos $ 3.5 
2.autos $ 12.00
3.camiones $ 16.00
desarroye un programa en python donde conociendo el tipo de vehiculodetermine:
* El valor a pagar por cada vehiculo que pase por el peaje.
* Total recaudado en el peaje ese dia.
* total recaudado por cada vehiculo.
* Cual es el automotor que mas transito en le peaje.
'''

import random

vehiculos=["moto", "auto", "camion"]
precios=[3.5, 12.00, 16.0]
contVehi=[0, 0, 0]
acumPre=[0, 0, 0]
i=1

respuesta=input("Desea ingresar los datos manualmente: (s/si)")
if respuesta=="s" or respuesta=="si":
    vehiculo=input("Que vehiculo ingreso?: moto(1) - auto(2) - camion(3) -salir(0)")
    while vehiculo!=0:
        vehiculo=int(input("Que vehiculo ingreso?: moto(1) - auto(2) - camion(3) -salir(0)"))

        if vehiculo==1:
            acumPre[0]+=precios[0]
            contVehi[0]+=1
            print(vehiculos[0],precios[0])
        elif vehiculo==2:
            acumPre[1]+=precios[1]
            contVehi[1]+=1
            print(vehiculos[1],precios[1])
        elif vehiculo==3:
            acumPre[2]+=precios[2]
            contVehi[2]+=1
            print(vehiculos[2],precios[2])


else:
    while i!=0:
        i=random.randrange(0,200)
        if i>0 and i<=30:
            acumPre[0]+=precios[0]
            contVehi[0]+=1
            print(vehiculos[0],precios[0])
        elif i>30 and i<=60:
            acumPre[1]+=precios[1]
            contVehi[1]+=1
            print(vehiculos[1],precios[1])
        elif i>60 and i<=100:
            acumPre[2]+=precios[2]
            contVehi[2]+=1
            print(vehiculos[2],precios[2])


recaudacion=0
for x in acumPre:
    recaudacion=recaudacion+x

maxTranc=max(contVehi)
posMax=contVehi.index(maxTranc)
print("el vehiculo que mas paso : ",vehiculos[posMax])


print("-------------------------")
print(vehiculos[0]," : ",contVehi[0])
print("monto total: $" ,acumPre[0])
print("-------------------------")

print(vehiculos[1]," : ",contVehi[1])
print("monto total: $" ,acumPre[1])
print("-------------------------")

print(vehiculos[2]," : ",contVehi[2])
print("monto total: $" ,acumPre[2])
print("-------------------------")
print("Recaudacion del dia: $ ",recaudacion)