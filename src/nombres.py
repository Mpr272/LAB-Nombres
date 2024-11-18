import csv
from collections import namedtuple

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(ruta):
    res = []
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for año,nombre,frecuencia,genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            tupla = FrecuenciaNombre(año,nombre,frecuencia,genero)
            res.append(tupla)
    return res

def filtrar_por_genero(lista: list[FrecuenciaNombre],genero: str)->list[tuple]:
    res = []
    for r in lista:
        if r.genero == genero:
            res.append(r)
    return res

def calcular_nombre(lista: list[FrecuenciaNombre],genero: str)->set[str]:
    res = set()
    
    for r in lista:
        if r.genero == genero:
            res.add(r.nombre)
        elif genero == None:
            res.add(r.nombre)
    res2 = sorted(res)
    return res2

def calcular_top_nombres_de_año(lista:list[FrecuenciaNombre],año:int,limite:int,genero:str)->list[tuple]:
    print("test")