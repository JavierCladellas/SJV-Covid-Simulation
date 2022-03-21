from registroDatosSJV import *
from MethodsSJV import *
import ClasesSJV
from matplotlib import pyplot as plt
import numpy as np
import copy
import os 

promedio_I_total=[]
promedio_I_aislados_y_no=[]
promedio_E=[]
promedio_I=[]
promedio_A=[]
promedio_R=[]

def createDir(path):
	if not os.path.exists(path):
		os.mkdir(path)

createDir("graficas")
createDir("infectados")
createDir("poblaciones")

def updateAll(habitantes):
	infectados_aislados=updateInfectedAislados(habitantes)
	infectados_no_aislados=updateInfectedNoAislados(habitantes)
	susceptibles=updateSusceptibles(habitantes)
	sospechosos=updateSospechosos(habitantes)
	expuestos=updateExposed(habitantes)
	recuperados=updateRecovered(habitantes)

	return (infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados)


def SJV(habitantes):
	counter=0
	E=[]
	I_total=[]
	I_aislados_y_no=[]
	I=[]
	A=[]
	R=[]

	#Probabilidades (de ser infectado en un dia)
	
	get_infected_at_work=0.03
	get_infected_at_market=0.02
	
	aislarse=0.1
	sopsechoso_sea_infectado=0.05

	visitar_vecino_mucho=1
	visitar_vecino_poco=1/7
	visitar_tienda_mucho=1/2
	visitar_tienda_poco=1/5
	visitar_comedores_mucho=2
	visitar_comedores_poco=1/2
	visitar_market_mucho=1/3.5
	visitar_market_poco=1/14
	#transforma sospechosos en infectados

	for sos in updateSospechosos(habitantes):
		if random.random()<sopsechoso_sea_infectado:
			sos.gotInfected()


	for dia in range(60):

		(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)
		trabajadores=updateWorkers(habitantes)
		visita_familiares=updateVisitaFamiliares(habitantes)
		
		for hora in [i for i in range(24)]:

			updateAll(habitantes)
			for com in comunidades:
				com.updatePopulation(habitantes)

			#Movimiento
			if dia%7!=0 and dia%7!=1: 
				
				if hora==8:
					for w in trabajadores:
						w.goToWork()

				if hora==12:
					for i in range(len(trabajadores)//2):
						random.choice(trabajadores).goToHouse()
					
				if hora==13:
					for w in trabajadores:
						w.goToWork()

				if hora==17:
					for w in trabajadores:
						w.goToHouse()



			#::::::::::#infeccion#:::::::::::#

			#infeccion de personas en trabajo


			for w in trabajadores:
				if w.position==():
					if w.status=="S" or w.status=="Sospechoso":
						if random.random()<get_infected_at_work/8:
							w.gotExposed(dia)

			(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)

			#infeccion por visitar vecino
			if hora>=8 and hora <=22:
				for com in comunidades:
					susceptibles_y_sospechosos=susceptibles.copy()
					susceptibles_y_sospechosos.extend(sospechosos)
					sus_com=[k  for k in susceptibles_y_sospechosos if k.position==(com.longitud,com.latitud)] #susceptibles y sospechosos dentro de la comunidad
					for hab in infectados_no_aislados:
						if hab.position == (com.longitud,com.latitud) and sus_com != []:
							if hab.vecinos == 2:
								if random.random()<visitar_vecino_mucho/14:
									if random.random() < hab.beta:
										random.choice(sus_com).gotExposed(dia)
							elif hab.vecinos == 1:
								if random.random()<visitar_vecino_poco/14:
									if random.random() < hab.beta:
										random.choice(sus_com).gotExposed(dia)

			(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)


			#infeccion por visitar tiendas 
			if hora>=7 and hora <=20:
				for com in comunidades:
					van_a_tiendas_por_comunidad = [h for h in habitantes if (h.position==(com.longitud,com.latitud) and h.tiendas>0)]
					estan_en_tienda=[]
					for per in van_a_tiendas_por_comunidad: 
						if per.tiendas==2:
							if random.random()<visitar_tienda_mucho/13:
								estan_en_tienda.append(per)
						if per.tiendas==1:
							if random.random()<visitar_tienda_poco/13:
								estan_en_tienda.append(per)
					for l in estan_en_tienda:
						if l.status=="I":
							for sano_en_tienda in [i  for i in estan_en_tienda if (i.status=="Sospechoso" or i.status=="S")]:
								if random.random()<l.beta:
									sano_en_tienda.gotExposed(dia)



			
			(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)


			#infeccion por visitar pupuserias y comedores
			if ((hora>=6 and hora<=8) or(hora>=12 and hora<=13) or (hora>=18 and hora<=20)):
				for com in comunidades:
					van_a_comedores_por_comunidad = [h for h in habitantes if (h.position==(com.longitud,com.latitud) and (h.comedores>0 or h.pupuserias>0))]
					estan_en_comedor=[]
					for per in van_a_comedores_por_comunidad: 
						if per.pupuserias==2 or per.comedores==2:
							if random.random()<visitar_comedores_mucho/7:
								estan_en_comedor.append(per)
						if per.pupuserias==1 or per.comedores==1:
							if random.random()<visitar_comedores_poco/7:
								estan_en_comedor.append(per)
					for l in estan_en_comedor:
						if l.status=="I":
							for sano_en_comedor in [i for i in estan_en_comedor if (i.status=="Sospechoso" or i.status=="S")]:
								if random.random()<l.beta:
									sano_en_comedor.gotExposed(dia)
			
			
			(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)


			#infecicon por visitar supermercados y gasolineras
			if hora>=7 and hora<=22:
				susceptibles_y_sospechosos=susceptibles.copy()
				susceptibles_y_sospechosos.extend(sospechosos)
				for hab in susceptibles_y_sospechosos:
					if hab.supermercados==2 or hab.gasolineras==2:
						if random.random()<visitar_market_mucho/15:
							if random.random()<get_infected_at_market/15:
								hab.gotExposed(dia)
					elif hab.supermercados==1 or hab.gasolineras==1:
						if random.random()<visitar_market_poco/15:
							if random.random()<get_infected_at_market/15:
								hab.gotExposed(dia)
			

			for com in comunidades:
				com.updatePopulation(habitantes)


			(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)

			#presencia de sintomas en expuestos
			for ex in expuestos:
				if dia==ex.infection_day + ex.incubacion:
					ex.gotInfected()


			#aislamiento de infectado
			for inf in infectados_no_aislados:
				if inf.sintomatico:
					if random.random() < aislarse/24:
						inf.gotAislated(dia)


			#recuperacion de personas aisladas
			for inf_ais in infectados_aislados:
				if dia==inf_ais.infection_day + inf_ais.recovery_day:
					inf_ais.gotRecovered()

			#recuperacion de personas no aisladas
			for inf in infectados_no_aislados:
				if dia==inf.infection_day + inf.recovery_day:
					inf.gotRecovered()


			(infectados_aislados,infectados_no_aislados,susceptibles,sospechosos,expuestos,recuperados) = updateAll(habitantes)

			#printMap(dia,hora,susceptibles,sospechosos,infectados_no_aislados,recuperados,comunidades,counter)
			#printInfected(dia,hora,infectados_no_aislados,comunidades,counter)


			I_total.append(len(infectados_aislados)+len(infectados_no_aislados)+len(recuperados))
			I_aislados_y_no.append(len(infectados_aislados)+len(infectados_no_aislados))
			E.append(len(expuestos))
			I.append(len(infectados_no_aislados))
			A.append(len(infectados_aislados))
			R.append(len(recuperados))
			counter+=1
		print(dia)

	return(I_total,I_aislados_y_no,E,I,A,R,counter)


for k in range(1):
	population=copy.deepcopy(habitantes)
	print("sim: ")
	print(k)
	(I_total,I_aislados_y_no,E,I,A,R,counter)=SJV(population)
	
	promedio_I_total.append(I_total)
	promedio_I_aislados_y_no.append(I_aislados_y_no)
	promedio_E.append(E)
	promedio_I.append(I)
	promedio_A.append(A)
	promedio_R.append(R)


plt.plot([i for i in range(counter)],promedioCurvas(promedio_I_total),c='orange')
plt.plot([i for i in range(counter)],promedioCurvas(promedio_I_aislados_y_no),c='red')
plt.xlabel("Tiempo en horas")
plt.title("Casos activos y confirmados")
plt.savefig('graficas/activos y confirmados promedio 60 dias.png')
plt.clf()

plt.plot([i for i in range(counter)],promedioCurvas(promedio_E),c='blue')
plt.xlabel("Tiempo en horas")
plt.title("Expuestos")
plt.savefig('graficas/expuestos 60 dias.png')
plt.clf()

plt.plot([i for i in range(counter)],promedioCurvas(promedio_I),c='orange')
plt.plot([i for i in range(counter)],promedioCurvas(promedio_A),c='yellow')
plt.xlabel("Tiempo en horas")
plt.title("Infectados aislados y no aislados")
plt.savefig('graficas/infectados aislados y no aislados 60 dias.png')
plt.clf()

plt.plot([i for i in range(counter)],promedioCurvas(promedio_R),c='green')
plt.xlabel("Tiempo en horas")
plt.title("Recuperados")
plt.savefig('graficas/recuperados 60 dias.png')
plt.clf()

