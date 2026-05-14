#Se han realizado cambios desde que se creó la rama desarrollo-seguro

import unittest 
 
def cadena_mas_larga(lista_cadenas): 
  
    #Comprobación simple de si la lista está vacía  
    if len(lista_cadenas) == 0: 
        return "" 
    #Creamos la lista para almacenar las cadenas más largas 
    cadenas_mas_largas = [] 
    longitud_maxima = 0 
 
    #Recorremos la lista 
    for cadena_actual in lista_cadenas: 
        #Nos aseguramos de que la cadena sea un string 
        if isinstance(cadena_actual, str): 
            #Contamos las letras de la cadena actual 
            longitud = len(cadena_actual) 
 
            #Guardamos la cadena más larga 
            if longitud > longitud_maxima: 
                longitud_maxima = longitud 
                cadenas_mas_largas = [cadena_actual] 
            #Añadimos las cadenas con la misma longitud 
            elif longitud == longitud_maxima: 
                cadenas_mas_largas.append(cadena_actual) 
 
    #Ordenamos alfabéticamente y devolvemos la primera 
    cadenas_mas_largas.sort() 
    #Nos aseguramos de que no esté vacío 
    if len(cadenas_mas_largas) == 0: 
        return "" 
    else: 
        return cadenas_mas_largas[0] 
 
 
#Programa principal para introducir las 5 palabras 
def introduce_palabras(): 
    palabras = [] 
    print("Introduce 5 palabras:") 
    while len(palabras) < 5: 
        palabra = input(f"Palabra {len(palabras) + 1}: ") 
        if " " in palabra: 
            print("Error: Solo se permite escribir una palabra, no puedes usar espacios.") 
        else: 
            palabras.append(palabra) 
     
    resultado = cadena_mas_larga(palabras) 
    print("La palabra más larga es:", resultado) 
 
class Test(unittest.TestCase): 
 
    def test_1_lista_enunciado(self): 
        lista = ["a", "ab", "abc", "dddd", "abcd"] 
        print("Lista introducida: ", lista) 
        resultado = cadena_mas_larga(lista) 
        print("Lista del enunciado: ", lista, "\nResultado: ", resultado) 
        self.assertEqual(resultado, "abcd") 
 
    def test_2_misma_longitud(self): 
        lista = ["palo", "hola", "lata"] 
        print("Lista introducida: ", lista) 
        resultado = cadena_mas_larga(lista) 
        # Todas tienen la misma longitud, debe devolver la primera alfabéticamente 
        print("Lista con la misma longitud: ",lista, "\nResultado: ", resultado) 
        self.assertEqual(resultado, "hola") 
 
    def test_3_lista_vacia(self): 
        lista = [] 
        print("Lista introducida: ", lista) 
        resultado = cadena_mas_larga(lista) 
        print("Se ha introducido una lista vacía: ", lista, "\nResultado: ", resultado) 
        self.assertEqual(resultado, "") 
    def test_4_valor_nulo(self): 
        lista = ["Rojo", None, "Azul"] 
        print("Lista introducida: ", lista) 
        resultado = cadena_mas_larga(lista) 
        print("Lista con un valor nulo: ", lista, "\nResultado: ", resultado) 
        self.assertEqual(resultado, "Azul") 

#introduce_palabras() 
#Comenta el programa anterior y descomenta el siguiente para realizar las pruebas 
unittest.main() 