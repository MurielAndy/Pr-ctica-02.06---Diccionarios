diccionario = {}

print("Introduce las palabras en español e inglés separadas por dos puntos (<palabra>:<traducción>). Para terminar, escribe 'terminar'.")

while True:
    entrada = input("Introduce palabra en español: ")
    
    if entrada.lower() == "terminar":
        break
    
    
    if ":" in entrada:
        
        palabra, traduccion = entrada.split(":")
        
        diccionario[palabra.strip()] = traduccion.strip()
    else:
        print("Formato incorrecto. Debes usar 'palabra:traducción'. Intenta nuevamente.")


print("\nDiccionario de traducción completo:")
print(diccionario)


frase_espanol = input("\nIntroduce una frase en español para traducir: ")


frase_traducida = []


for palabra in frase_espanol.split():
    
    if palabra in diccionario:
        frase_traducida.append(diccionario[palabra])
    else:
        frase_traducida.append(palabra)

print("\nFrase traducida:")
print(" ".join(frase_traducida))

