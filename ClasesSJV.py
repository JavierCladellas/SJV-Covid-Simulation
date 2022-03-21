import random

class Canton:
	
	def __init__(self,name,poblacion):
		self._name = name
		self._poblacion=poblacion



class Caserio:
	
	def __init__(self,name,canton,poblacion):
		self._name = name

		self._canton=canton
		
		self._poblacion=poblacion



class Comunidad: 
	
	def __init__(self,name,coordenadas,poblacion):
		self._name = name 
		self.longitud=coordenadas[0]
		self.latitud=coordenadas[1]

		self.poblacion=poblacion

	def updatePopulation(self,habitantes):
		self.susceptibles=0
		self.sospechosos=0
		self.infectados=0
		self.recuperados=0
		self.expuestos=0

		self.poblacion=0

		for hab in habitantes:
			if hab.position==(self.longitud,self.latitud):
				self.poblacion+=1

		for hab in habitantes:
			if hab.position==(self.longitud,self.latitud):	
				if hab.status=="S":
					self.susceptibles+=1
				if hab.status=="Sospechoso":
					self.sospechosos+=1
				if hab.status=="I":
					self.infectados+=1
				if hab.status=="R":
					self.recuperados+=1
				if hab.status=="E":
					self.expuestos+=1
		
		if self.infectados>=1:
			self.status="Infectada"
		elif self.infectados==0 and self.sospechosos>0.5*self.susceptibles:
			self.status="Sospechosa"
		else:
			self.status="Segura"


class Casa:
	
	def __init__(self,id_respuesta,comunidad,habitantes,cantidad_covid):
		#type( coordenadas ) = tuple 
		#type( comunidad ) = Comunidad Obj
		#type( habitantes ) = int
		self.position=(comunidad.longitud,comunidad.latitud)

		#Ubicacion y direccion
		#self._coordenadas=coordenadas
		self._id_respuesta=id_respuesta
		self._comunidad=comunidad
		self._habitantes=habitantes
		self.cantidad_covid=cantidad_covid
		#self._caserio=comunidad._caserio
		#self._canton=comunidad._canton




class Habitante:

	def __init__(self,casa,infected,recovered,bioseguridad,visita_hospital,evento_social,fiebre,tosSeca,rinitis,dolorDeCabeza,disnea,cansancio,perdidaSentidos,diarrea,tiendas,gasolineras,supermercados,pupuserias,comedores,familiares,vecinos,trabajo):
		self._casa=casa
		self.position=casa.position
		self.infected=infected
		
		self.bioseguridad=bioseguridad
		self.visita_hospital=visita_hospital
		self.evento_social=evento_social

		self.tiendas=tiendas
		self.gasolineras=gasolineras
		self.supermercados=supermercados
		self.pupuserias=pupuserias
		self.comedores=comedores
		self.familiares=familiares
		self.vecinos=vecinos
		self.trabajo=trabajo

		self.infection_day=0

		sintomas=[fiebre,tosSeca,rinitis,dolorDeCabeza,disnea,cansancio,perdidaSentidos,diarrea]
		verdades=[]

		for sin in sintomas:
			if sin:
				verdades.append(sin)

		if len(verdades)>=2 and sintomas[0]:
			self.sintomas=True
		else:
			self.sintomas=False

		self.aislado=False
		self.recovery_day=random.randint(7,20)

		self.incubacion=random.randint(4,6)

		if infected==True:
			if recovered=="Sí":
				self.status="R"
			else:
				self.status="I"
		else:
			if self.sintomas or visita_hospital or evento_social:
				self.status="Sospechoso"
			else:
				self.status="S"

		
		if random.random()<0.6:
			self.sintomatico=True
		else:
			self.sintomatico=False

		if self.sintomatico:
			if not bioseguridad:
				self.beta=random.uniform(0.5,0.9)
			else:
				self.beta=random.uniform(0.1,0.5)
		else:
			if not bioseguridad:
				self.beta=random.uniform(0.2,0.4)
			else:
				self.beta=random.uniform(0.0,0.2)
	
	#Métodos de cambio de estado
	def gotExposed(self,infection_day):
		self.status="E"
		self.infection_day=infection_day
		self.aislado=False

	def gotInfected(self):
		self.status="I"
		self.aislado=False
		
	def gotAislated(self,aislation_day):
		self.aislation_day=aislation_day
		self.aislado=True

	def gotRecovered(self):
		self.status="R"
		self.aislado=False

	#Métodos de movimiento
	def goToWork(self):
		self.position=()

	def goToHouse(self):
		self.position=self._casa.position

	def goToLugarComun(self,lugar):
		self.position=lugar._coordenadas


	def goToFamiliar(self,comunidades):
		posiciones=[]
		for com in comunidades:
			posiciones.append((com.longitud,com.latitud))
		if self.position!=():
			self.position=random.choice(posiciones)
		else:
			pass


	def selectLugarComun(self):
		lugar=random.choice(self.lugares_comunes)
		return lugar

class LugarComun:
	def __init__(self,name):
		self._name=name
	
		self.abierto=True
		self.clientes=0

	def cerrar(self):
		self.abierto=False