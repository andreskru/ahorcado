import random

import string

import os

from palabras import palabras

from ahorcado_diagramas import vidas_diccionario_visual

#Ahorcado para Santu
# https://github.com/andreskru/ahorcado

def obtener_palabra_valida(palabras):
    #seleccionar uan palabra al azaar de la li8sta
    palabra = random.choice(palabras)

    #evitar guiones o espacioe en la palabra
    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
        
    return palabra.upper()

def ahorcado():

    print ("====================================")
    print( "!Bienvenido al Juego del Ahorcado!!")
    print ("====================================")
    print ()      
    print ("Tenes 7 vidas para adivinar una palabra elegida por la compu")
    
    palabra = obtener_palabra_valida(palabras)
    
    #    definir conjunto de elementos (caracteres) sin repeticiones  
    letras_por_adivinar = set(palabra)
    # 
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print ()
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
                     
        # Mostar estado actual palabra    
        palabra_lista = [letra if letra in letras_adivinadas else"-" for letra in palabra]

        # Mostrar estado actual de la horca
        print (vidas_diccionario_visual [vidas])

        #Mostrar letras separadas por espacio
        print("----------------------------------------------------")
        print(f"Palabra a adivinar: {' '.join(palabra_lista)}")
        print("----------------------------------------------------")
        print()
        letra_usuario = input ("Escoge una letra: ").upper()

        os.system ('clear')

        #si la letra escogida esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se añade al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
               #Si la letra esta en la palabra, quitarla del conjunto de letras pendientes por adivinar
               # Si no esta en la palabra quitar una vida
            
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(" ")
            else:
                vidas = vidas - 1
                print ()
                print(f"Tu letra, {letra_usuario} no esta en la palabra.")
                
        #si la letra escogida ya fue usaada:
        elif letra_usuario in letras_adivinadas:
            print()
            print("Ya escogiste esa letra. Por favor escoge una nueva")
    
        else:
            print ()
            print("\nesta letra no es valida")
        
    if vidas ==0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado, perdiste, la palabra era:{palabra}")
        
    else:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(f"!!EXCELENTE!!!, adivinaste la palabra {palabra}")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        
       
ahorcado()
     
   
