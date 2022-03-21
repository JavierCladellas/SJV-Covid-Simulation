from math import sqrt
from matplotlib import pyplot as plt
def distanciaEuclidiana(p1,p2):
	return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def promedioCurvas(lista_curvas):
	promedio=[]
	for i in range(len(lista_curvas[0])):
		promedio_punto=0
		for curva in lista_curvas:
			promedio_punto+=curva[i]
		promedio.append(promedio_punto/len(lista_curvas))

	return promedio


#Update lists functions
def updateInfectedNoAislados(habitantes):
	infectedNoAislado=[]
	for hab in habitantes: 
		if hab.status=="I" and not hab.aislado:
			infectedNoAislado.append(hab)
	return infectedNoAislado

def updateInfectedAislados(habitantes):
	infectedAislado=[]
	for hab in habitantes:
		if hab.status=="I" and hab.aislado:
			infectedAislado.append(hab)
	return infectedAislado

def updateRecovered(habitantes):
	recovered=[]
	for hab in habitantes:
		if hab.status=="R":
			recovered.append(hab)

	return recovered

def updateExposed(habitantes):
	exposed=[]
	for hab in habitantes:
		if hab.status=="E":
			exposed.append(hab)
	return exposed


def updateSusceptibles(habitantes):
	susceptibles=[]
	for hab in habitantes:
		if hab.status=="S":
			susceptibles.append(hab)

	return susceptibles

def updateSospechosos(habitantes):
	sospechosos=[]
	for hab in habitantes:
		if hab.status=="Sospechoso":
			sospechosos.append(hab)

	return sospechosos

def updateWorkers(habitantes):
	workers=[]
	for hab in habitantes:
		if hab.trabajo>0:
			workers.append(hab)
	return workers

def updateVisitaFamiliares(habitantes):
	visita_familiares=[]
	for hab in habitantes:
		if hab.familiares > 0:
			visita_familiares.append(hab)
	return visita_familiares

def updateVisitaVecinos(habitantes):
	visita_vecinos=[]
	for hab in habitantes:
		if hab.vecinos > 0:
			visita_vecinos.append(hab)
	return visita_vecinos

def printMap(dia,hora,susceptibles,sospechosos,infectadosNoAislados,recuperados,comunidades,counter):
	
	longitudes=[i.longitud for i in comunidades]
	latitudes=[j.latitud for j in comunidades]
	poblaciones=[k.poblacion for k in comunidades]
	colores=[]

	for com in comunidades:
		if com.status=="Segura":
			colores.append('green')
		if com.status=="Infectada":
			colores.append('red')
		if com.status=="Sospechosa":
			colores.append('yellow')


	plt.scatter(longitudes,latitudes,s=poblaciones,c=colores)
	plt.title("dia:{},hora:{}".format(dia,hora))
	plt.xlim(13.52,13.63)
	plt.ylim(-89.29,-89.25)
	plt.savefig("poblaciones/{}.png".format(counter))
	plt.clf()

def printInfected(dia,hora,infectadosNoAislados,comunidades,counter):
	longitudes=[i.longitud for i in comunidades]
	latitudes=[j.latitud for j in comunidades]
	infectados=[k.infectados * 7 for k in comunidades]

	plt.scatter(longitudes,latitudes,s=infectados,c="r")
	plt.title("dia:{},hora:{}".format(dia,hora))
	plt.xlim(13.52,13.63)
	plt.ylim(-89.29,-89.25)
	plt.savefig("infectados/{}.png".format(counter))
	plt.clf()


def promedioCurvas(lista_curvas):
	promedio=[]
	for i in range(len(lista_curvas[0])):
		promedio_punto=0
		for curva in lista_curvas:
			promedio_punto+=curva[i]
		promedio.append(promedio_punto/len(lista_curvas))

	return promedio



