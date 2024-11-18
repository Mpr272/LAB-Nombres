from nombres import *

def imprimir_datos_test(datos):
    print(f"Leido {len(datos)} registros")
    print("Mostrando los 3 primeros:")
    print(datos[0:3])
    print("Mostrando los 3 ultimos:")
    print(datos[-3:])

def test_filtrar_por_genero(datos):
    print("-Numero de registros para 'Hombre':", len(filtrar_por_genero(datos,"Hombre")))
    print("-Numero de registros para 'Mujer':",len(filtrar_por_genero(datos,"Mujer")))

def test_calcular_nombres(datos):
    listaHombre = calcular_nombre(datos,"Hombre")
    listaMujer = calcular_nombre(datos,"Mujer")
    listaNone = calcular_nombre(datos,None)
    print("-Ambos generos:", listaNone[0:10])
    print("-Hombres:", listaHombre[0:10])
    print("-Mujeres:",listaMujer[0:10])

def test_calcular_top_nombres_año(datos):
    listaNone = calcular_top_nombres_de_año(datos,2008,10,None)
    listaHombre = calcular_top_nombres_de_año(datos,2008,10,"Hombre")
    listaMujer = calcular_top_nombres_de_año(datos,2008,10,"Mujer")
    print("-Ambos generos:",listaNone)
    print("-Hombres:",listaHombre)
    print("-Mujeres:",listaMujer)

def test_calcular_nombres_ambos_generos(datos):
    print("-Nombres:",calcular_nombres_ambos_generos(datos))

if __name__ == "__main__":
    datos = leer_frecuencias_nombres("data/frecuencias_nombres.csv")
    #imprimir_datos_test(datos)
    #test_filtrar_por_genero(datos)
    #test_calcular_nombres(datos)
    #test_calcular_top_nombres_año(datos)
    test_calcular_nombres_ambos_generos(datos)
