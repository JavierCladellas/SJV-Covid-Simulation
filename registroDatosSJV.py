from ClasesSJV import *
import random
import pandas as pd

casas=[]
habitantes=[]
comunidades=[]

susceptibles=[]
sospechosos=[]
infectados=[]
recuperados=[]

df = pd.read_csv("data/results-survey226857-9-2.csv",sep=";")
df_comunidades= pd.read_csv("data/Ubicaciones San Jose Villanueva nuevo.csv",sep=";")

comunidad_names=list(df_comunidades["Ubicación"])
longitud=list(df_comunidades["Longitud"])
latitud=list(df_comunidades["Latitud"])

for k in range(len(comunidad_names)):
	comunidades.append(Comunidad(comunidad_names[k],(longitud[k],latitud[k]),0))



idRespuesta=[int(i) for i in list(df["ID de respuesta"])]
ubicacion=list(df["Ubicacion"])

for i,ub in enumerate(ubicacion):
	ubicacion[i]=comunidades[comunidad_names.index(ub)]

mujeres=[int(i) for i in list(df["Mujeres"])]
hombres=[int(i) for i in list(df["Hombres"])]

bioseguridad=[False if x=="No" else True for x in list(df["Bioseguridad"])]
hospitales=[False if x=="No" else True for x in list(df["Hospitales"])]
eventosSociales=[False if x=="No" else True for x in list(df["Eventos Sociales"])]

fiebre=[False if x=="No" else True for x in list(df["Fiebre"])]
tosSeca=[False if x=="No" else True for x in list(df["Tos Seca"])]
rinitis=[False if x=="No" else True for x in list(df["Rinitis"])]
dolorDeCabeza=[False if x=="No" else True for x in list(df["Dolor De Cabeza"])]
disnea=[False if x=="No" else True for x in list(df["Disnea"])]
cansancio=[False if x=="No" else True for x in list(df["Cansancio"])]
perdidaSentidos=[False if x=="No" else True for x in list(df["Perdida Sentidos"])]
diarrea=[False if x=="No" else True for x in list(df["Diarrea"])]

covid=[False if x=="No" else True for x in list(df["Covid"])]
cantidadCovid=[int(i) for i in list(df["Cantidad Covid"])]
recuperado=list(df["Recuperado"])


# nunca=0 poco=1 mucho=2
tiendas=[int(i) for i in list(df["Tiendas"])]
gasolineras=[int(i) for i in list(df["Gasolineras"])]
supermercados=[int(i) for i in list(df["Supermercados"])]
pupuserias=[int(i) for i in list(df["Pupuseria"])]
comedores=[int(i) for i in list(df["Comedores"])]
familiares=[int(i) for i in list(df["Familiares"])]
vecinos=[int(i) for i in list(df["Vecinos"])]
trabajo=[int(i) for i in list(df["Trabajo"])]

personasPorCasa=[mujeres[i]+hombres[i] for i in range(len(mujeres))]

for i in range(len(idRespuesta)):
	casas.append(Casa(idRespuesta[i],ubicacion[i],personasPorCasa[i],cantidadCovid[i]))

for i in range(len(idRespuesta)):
	habitantes.append(Habitante(casas[i],covid[i],recuperado[i],bioseguridad[i],hospitales[i],eventosSociales[i],fiebre[i],tosSeca[i],rinitis[i],dolorDeCabeza[i],disnea[i],cansancio[i],perdidaSentidos[i],diarrea[i],tiendas[i],gasolineras[i],supermercados[i],pupuserias[i],comedores[i],familiares[i],vecinos[i],trabajo[i]))


#Cantones
canton_el_escalon=Canton("El Escalón",0)
canton_el_matazano=Canton("El Matazano",0)
canton_el_palomar=Canton("El Palomar",0)
canton_las_dispensas=Canton("Las Dispensas",0)
canton_tula=Canton("Tula",0)

cantones=[canton_el_escalon,
canton_el_matazano,
canton_el_palomar,
canton_las_dispensas,
canton_tula]


"""

#Caserios

#El Escalon
caserio_el_escalon=Caserio("El Escalón",canton_el_escalon,0)
caserio_el_carmen=Caserio("El Carmen",canton_el_escalon,0)
caserio_el_espiritu=Caserio("El Espíritu",canton_el_escalon,0)
caserio_el_cementerio=Caserio("El Cementerio",canton_el_escalon,0)
caserio_las_mercedes=Caserio("Las Mercedes",canton_el_escalon,0)

#El Matazano
caserio_el_matazano=Caserio("El Matazano",canton_el_matazano,0)

#El Palomar
caserio_el_palomar=Caserio("El Palomar",canton_el_palomar,0)
caserio_lotificacion_valle_nuevo=Caserio("Lotificación Valle Nuevo",canton_el_palomar,0)

#Las Dispensas
caserio_las_dispensas=Caserio("Las Dispensas",canton_las_dispensas,0)
caserio_miramar=Caserio("Miramar",canton_las_dispensas,0)
caserio_el_zapote=Caserio("El Zapote",canton_las_dispensas,0)
caserio_san_paulino=Caserio("San Paulino",canton_las_dispensas,0)

#Tula
caserio_tula=Caserio("Tula",canton_tula,0)
caserio_el_mirador=Caserio("El Mirador",canton_tula,0)
caserio_el_guayabo=Caserio("El Guayabo",canton_tula,0)

caserios=[caserio_el_escalon,
caserio_el_carmen,
caserio_el_espiritu,
caserio_el_cementerio,
caserio_las_mercedes,
caserio_el_matazano,
caserio_el_palomar,
caserio_lotificacion_valle_nuevo,
caserio_las_dispensas,
caserio_miramar,
caserio_el_zapote,
caserio_san_paulino,
caserio_tula,
caserio_el_mirador,
caserio_el_guayabo]

#Comunidades
comunidades=[Comunidad(cas._name,cas,0) for cas in caserios]


#LugaresComunes
pupuseria=LugarComun("Pupuseria Conchita",(-1,-1),comunidades[2])
tiendita=LugarComun("Tiendita Dora",(-2,-1),comunidades[1])
comedor=LugarComun("Comedor Papas",(-3,-1),comunidades[0])

lugares_comunes=[]

#Habitantes

habitantes=[Habitante(home,False,False,False,False,False,False,random.choice(lugares_comunes),random.choice([False,True])) for home in casas]
"""