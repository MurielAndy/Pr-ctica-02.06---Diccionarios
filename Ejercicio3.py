
precios = {"pan": 1.40,"huevos": 2.30,"cebolla": 0.85,"aceite ": 4.35,}
Productos = input("Introduce el nombre del Producto: ").lower()

if Productos in precios:
    
    unidades = int(input(f"Introduce el número de unidades del {Productos}: "))
    
    precio_total = precios[Productos] * unidades
    
    
    print(f"El precio total por {unidades} unidades de {Productos} es: {precio_total}€")
else:
    print(f"El artículo {Productos} no está disponible en la tienda.")
